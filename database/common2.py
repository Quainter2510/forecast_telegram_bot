from sqlalchemy import create_engine, func, or_
from sqlalchemy.orm import sessionmaker
from time import time 

from typedDicts import *

from models import Base, Match, User, Forecast

from hello import *

def is_admin(id):
    return False

class DataBase:
    def __init__(self):
        engine = create_engine('sqlite:///forecast_bot.db')
        Session = sessionmaker(bind=engine)
        self.session = Session()
        Base.metadata.create_all(engine)

    def add_match(self, match_data: DataMatch) -> None:
        new_match = Match(match_id=match_data['match_id'],
                          tour=match_data['tour'],
                          league_id=match_data['league_id'],
                          status=match_data['status'],
                          team_home=match_data['team_home'],
                          team_away=match_data['team_away'],
                          goals_home=match_data['goals_home'],
                          goals_away=match_data['goals_away'],
                          datetime=match_data['datetime'])
        self.session.add(new_match)
        self.session.commit()
        all_users_id = self.get_all_users_id()
        for user_id in all_users_id:
            self.add_forecast(match_data['match_id'], user_id[0])

    def delete_match(self, match_id: int):
        self.session.query(Forecast).filter(Forecast.match_id == match_id).delete()
        self.session.query(Match).filter(Match.match_id == match_id).delete()
        self.session.commit()
        users_id = self.get_all_users_id()
        for user_id in users_id:
            self.update_sum_points_for_user(user_id[0])


    def check_user_in_tournament(self, tg_id: int) -> bool:
        return self.session.get(User, tg_id) != None

    def add_user(self, tg_id: int, username: str) -> None:
        if self.check_user_in_tournament(tg_id):
            # Сказать, что такой уже есть
            # вернуть False? -1? Исключение?
            return
        if is_admin(tg_id):
            status = "superadmin"
        else:
            status = "owe"

        new_user = User(telegram_id=tg_id,
                        username=username,
                        status=status)
        self.session.add(new_user)
        self.session.commit()

        matches_id = self.get_all_matches_id()
        for match_id in matches_id:
            self.add_forecast(match_id[0], tg_id)

    def add_forecast(self, match_id: int, user_id: int):
        forecast = Forecast(match_id=match_id,
                            user_id=user_id,
                            match_point=0)
        self.session.add(forecast)
        self.session.commit()

    def get_all_matches_id(self):
        return self.session.query(Match.match_id).all()
    
    def get_all_users_id(self):
        return self.session.query(User.telegram_id).all()
        
    def set_forecast(self, user_id: int, match_id: int, goals_home_pred: int, goals_away_pred: int):
        self.session.query(Forecast).filter(Forecast.match_id == match_id,
                                            Forecast.user_id == user_id).\
                                            update({"goals_home_predict": goals_home_pred,
                                                    "goals_away_predict": goals_away_pred})
        self.session.commit()

    def delete_user(self, user_id: int):
        self.session.query(User).filter(User.telegram_id == user_id).delete()
        self.session.query(Forecast).filter(Forecast.user_id == user_id).delete()
        self.session.commit()

    def get_tour_matches(self, tour: str):
        '''Список матчей в туре
        (team_home, team_away, datetime, status)'''
        return self.session.query(Match.team_home, Match.team_away, Match.datetime, Match.status).\
            filter(Match.tour == tour).all()
    
    def get_predict_match(self, user_id: int, match_id: int):
        return self.session.query(Forecast.goals_home_predict, Forecast.goals_away_predict).\
            filter(Forecast.match_id == match_id, Forecast.user_id == user_id).first()
    
    def get_palyers_info(self):
        return self.session.query(User.telegram_id, User.username, User.status).all()
    
    def get_now_tour(self):
        # t = time()
        return self.session.query(Match.tour).filter(Match.datetime > time()).first()[0]

    def reminder(self, tour: str):
        return self.session.query(Forecast.user_id).join(Match, Match.match_id == Forecast.match_id).\
            filter(or_(Forecast.goals_away_predict == None, Forecast.goals_home_predict == None), Match.tour == tour).distinct().all()

    def get_points_match_for_user(self, user_id: int, match_id: int) -> int:
        return self.session.query(Forecast.match_point).filter(Forecast.match_id == match_id,
                                                               Forecast.user_id == user_id).first()[0]

    def get_sum_points_tour_for_user(self, user_id: int, tour: str) -> int:
        return self.session.query(func.sum(Forecast.match_point)).filter(Forecast.user_id == user_id).\
                join(Match, Match.match_id == Forecast.match_id).filter(Match.tour == tour).first()[0]
    
    def get_result_tour_for_user(self, user_id: int, tour: str):
        return self.session.query(Match.team_home, Match.team_away, 
                                  Match.goals_home, Match.goals_away, Forecast.goals_home_predict,
                                   Forecast.goals_away_predict, Forecast.match_point).\
                                    join(Forecast, Match.match_id == Forecast.match_id).\
                                   filter(Forecast.user_id == user_id, Match.tour == tour).all()
    
    def set_user_status(self, user_id: int, status: str):
        self.session.query(User).filter(User.telegram_id == user_id).update({"status": status})
        self.session.commit()

    def get_all_tour_name(self):
        return self.session.query(Match.tour).distinct().all()
    
    def update_sum_points_for_user(self, user_id: int):
        sum_points = self.session.query(func.sum(Forecast.match_point)).filter(Forecast.user_id == user_id).first()[0]
        self.session.query(User).filter(User.telegram_id == user_id).update({"points_sum": sum_points})
        self.session.commit()

    def get_count_matches_in_tour(self, tour: str):
        return self.session.query(Match).filter(Match.tour == tour).count()



# db = DataBase()
# # db.add_match(parse()[-2])
# # db.add_user(1233, "Paul")
# # db.set_forecast(1234, 1149524, 9, 4)
# # db.delete_user(123)
# # print(db.get_tour_matches("Round of 16"))
# # print(db.get_predict_match(1234, 1149524))
# # print(db.get_palyers_info())
# # print(db.check_user_in_tournament(1234))
# # print(db.check_user_in_tournament(1233))
# # print(db.check_user_in_tournament(123))
# # print(db.get_sum_points_tour_for_user(1233, "Round of 16"))
# # print(db.get_points_match_for_user(1234, 1149524))
# # print(db.get_result_tour_for_user(1234, "Round of 16"))
# # db.set_user_status(1234, "hui")
# # print(db.get_all_tour_name())
# # db.update_sum_points_for_user(1234)
# # print(db.get_count_matches_in_tour("Round of 16"))
# print(db.reminder("Round of 16"))

import sqlite3
from typing import List, Tuple
from config_data import relations, config
from matches_parser.parser import parser
from helper_function import helper_func

CREATE_TABLES_MATCHES = '''
CREATE TABLE IF NOT EXISTS matches(tour INTEGER, date DATETIME, match TEXT, result TEXT);
'''
CREATE_TABLES_FORECAST = '''
CREATE TABLE IF NOT EXISTS forecast(date DATE, match TEXT, id_player BIGINT, result TEXT);
'''
CREATE_TABLES_USERS = '''
CREATE TABLE IF NOT EXISTS users(nickname TEXT, id_player BIGINT, lastPosition INTEGER DEFAULT 0, tour1 INTEGER DEFAULT 0, tour2 INTEGER DEFAULT 0,
         tour3 INTEGER DEFAULT 0, tour4 INTEGER DEFAULT 0, tour5 INTEGER DEFAULT 0,  tour6 INTEGER DEFAULT 0, tour7 INTEGER DEFAULT 0, tour8 INTEGER DEFAULT 0, tour9 INTEGER DEFAULT 0, tour10 INTEGER DEFAULT 0, tour11 INTEGER DEFAULT 0, tour12 INTEGER DEFAULT 0, sum INTEGER DEFAULT 0);
'''
class MyDataBase:
    def __init__(self):
        try: 
            # self.db = sqlite3.connect('/root/rfpl23/cl_db.db', check_same_thread=False)
            self.db = sqlite3.connect('rfpl_db.db', check_same_thread=False)
            self.cursor = self.db.cursor() 
            self.cursor.execute(CREATE_TABLES_FORECAST)
            self.cursor.execute(CREATE_TABLES_MATCHES)
            self.cursor.execute(CREATE_TABLES_USERS)
            matches_count = self.cursor.execute("SELECT count(*) FROM matches").fetchone()[0]
            if matches_count == 0:
                self.update_matches()
        except sqlite3.Error as error:
            print(error)


    def fill_matches(self, matches: Tuple) -> None:
        # Заполнение таблицы матчей
        # matches: (tour, datetime, match, result)
        self.cursor.executemany("INSERT INTO matches VALUES(?, ?, ?, ?)", matches)
        self.db.commit()


    def complement_forecast(self, matches: Tuple) ->None:
        # Дополнить талбицу матчей (для плей-офф)
        for id, nick in self.get_all_id_player():
            for match in matches:
                date = match[1].split()[0]
                self.cursor.execute(
                    f'INSERT INTO forecast VALUES("{date}", "{match[2]}", "{id}", "–:–")')
        self.db.commit()

    def add_player(self, id_player: int, nickname: str) -> None:
        # Добавить игрока в таблицу и создать для него матчи
        if self.cursor.execute(
                f"SELECT id_player FROM users WHERE id_player = {id_player}").fetchone() is None:
            self.cursor.execute(
                f'INSERT INTO users(id_player, nickname) VALUES("{id_player}", "{nickname}")')
            self.cursor.execute(f'SELECT match, date FROM matches')
            for match in self.cursor.fetchall():
                date = match[1].split()[0]
                self.cursor.execute(
                    f'INSERT INTO forecast VALUES("{date}", "{match[0]}", "{id_player}", "–:–")')
            self.db.commit()

    def check_player_in_tournament(self, id_player: int) -> bool:
        # Проверить присмктствие игрока в таблице
        if self.cursor.execute(
                f"SELECT id_player FROM users WHERE id_player = {id_player}").fetchone() is None:
            return False
        return True

    def delete_player(self, id_player: int) -> None:
        # Удалить игрока
        if self.cursor.execute(
                f"SELECT COUNT(id_player) FROM users WHERE id_player = {id_player}").fetchone() != 0:
            self.cursor.execute(f'DELETE FROM users WHERE id_player = "{id_player}"')
            self.cursor.execute(f'DELETE FROM forecast WHERE id_player = "{id_player}"')
            self.db.commit()

    def change_forecast(self, id_player: int, match: str, res: str) -> bool:
        # Изменить прогноз игрока на матч
        # Вернуть результат выполнения действия
        self.cursor.execute(
            f'''SELECT match FROM matches WHERE match = "{match} AND date < datetime('now','localtime')"''')
        if not self.cursor.fetchone() is None:
            return False
        self.cursor.execute(
            f'''UPDATE forecast SET result = "{res}" WHERE match = "{match}"
             AND id_player = "{id_player}"''')
        self.db.commit()
        return True

    def get_tour_matches(self, tour: int) -> Tuple:
        # Вернуть кортеж матчей заданного тура 
        self.cursor.execute(
            f"SELECT match FROM matches WHERE tour = '{tour}' AND date > datetime('now','localtime')")
        return self.cursor.fetchall()

    def get_forecast_match(self, id_player: int, match: str) -> str: # !!!!!!!!!!!!!!!!!!
        # Вернуть прогноз на заданный матч от пользователя
        self.cursor.execute(
            f'SELECT result FROM forecast WHERE id_player = "{id_player}" AND match = "{match}"')
        ans = self.cursor.fetchone()
        return ans[0]

    def get_other_forecast_match(self, id_player: int, match: str) -> str:
        # Вернуть прогноз пользователя на заданный матч
        self.cursor.execute(
            f"SELECT match FROM matches WHERE match = '{match}' AND date < datetime('now','localtime')")
        if self.cursor.fetchone() is None:
            return "-:-"
        self.cursor.execute(
            f'SELECT result FROM  forecast WHERE id_player = "{id_player}" AND match = "{match}"')
        return self.cursor.fetchone()[0]

    def get_all_tour_matches(self, tour: int) -> Tuple:
        # Вернуть все матчи тура
        self.cursor.execute(f"SELECT match FROM matches WHERE tour = '{tour}'")
        return self.cursor.fetchall()

    def get_forecast_tour(self, id_player: int, tour: int) -> List:
        # Вернуть прогноз на весь тур определенного пользователя 
        all_matches = self.get_all_tour_matches(tour)
        res = []
        for match in all_matches:
            res.append(match[0] + "—" + self.get_forecast_match(id_player, match[0]))
        return res

    def get_result_tournament(self) -> Tuple:
        # Вернуть всю таблицу пользователей
        # nick, id, last_pos, tourN, sum
        self.cursor.execute(f'SELECT * from users')
        return self.cursor.fetchall()

    def get_result_tour(self, tour: int) -> Tuple:
        # Вернуть кортеж с реальными результатами матчей заданного тура
        # матч, счет
        self.cursor.execute(f'SELECT match, result FROM matches WHERE tour = "{tour}"')
        return self.cursor.fetchall()

    def get_points_of_tour(self, tour: int) -> Tuple:
        # Вернуть кортеж ников и очков за тур
        self.cursor.execute(f'SELECT nickname, {tour} FROM users')
        return sorted(self.cursor.fetchall(), key=lambda x: (int(x[1]), x[0]), reverse=True)

    def update_result_tour(self) -> None:
        res = parser()  # [1, '2022-11-20 19:00', 'Катар—Эквадор', '–:–']
        for match in res:
            status = helper_func.get_match_status(match[1])
            self.cursor.execute(f'UPDATE matches SET result = "{match[3]}", status = "{status}" WHERE match = "{match[2]}"')
        self.db.commit()

    def update_tournament_table(self, id_player:int, tour:int, points: int) -> None:
        if not tour:
            return
        self.cursor.execute(
            f'UPDATE users SET {relations.TOUR_DCT[tour]} = "{points}" WHERE id_player = "{id_player}"')
        self.db.commit()
        self.cursor.execute(f'SELECT * from users WHERE id_player = "{id_player}"')
        q = self.cursor.fetchall()
        sum_points = 0
        for i in range(config.TOUR1_COLUMN, config.TOUR1_COLUMN + config.NUMBER_OF_TOUR):
            sum_points += q[0][i]
        self.cursor.execute(
            f'UPDATE users SET sum = "{sum_points}" WHERE id_player = "{id_player}"')
        self.db.commit()

    def get_now_tour(self) -> int:
        # Вернуть текущий тур
        self.cursor.execute(f"SELECT tour FROM matches WHERE date >= datetime('now','localtime')")
        if self.cursor.fetchone() is None:
            return config.NUMBER_OF_TOUR + 1
        return self.cursor.fetchone()[0]

    def get_all_id_player(self) -> Tuple:
        # Вернуть кортеж с таблицей пользователей
        # id, nick
        self.cursor.execute(f'SELECT id_player, nickname from users ORDER BY sum DESC')
        return self.cursor.fetchall()

    def get_nickname_player(self, id_player: int) -> str:
        # Вернуть ник по id
        self.cursor.execute(f'SELECT nickname from users WHERE  id_player = "{id_player}"')
        return self.cursor.fetchone()[0]

    def update_matches(self) -> None:
        # перезаписать матчи

        self.cursor.execute(f'DELETE from matches')
        res = parser()
        self.fill_matches(res)

    def reminder(self, tour: int) -> List[int]:
        # Напоминалка
        self.cursor.execute(f'SELECT match FROM matches WHERE tour = "{tour}"')
        matches = self.cursor.fetchall()
        ans = []
        for match in matches:
            self.cursor.execute(f'''SELECT id_player FROM forecast WHERE result = "–:–" 
            AND match = "{match[0]}"''')
            ans += [*self.cursor.fetchall()]
        return list(set(ans))

    def clear(self) -> None:
        # Удалить бд
        self.cursor.execute(f'DELETE from matches')
        self.cursor.execute(f'DELETE from users')
        self.cursor.execute(f'DELETE from forecast')
        self.db.commit()

    def statistic(self, id_player: int) -> Tuple:
        # Статистика на будущее
        self.cursor.execute(f"SELECT result FROM forecast WHERE id_player = '{id_player}'")
        return self.cursor.fetchall()

    def number_of_points_per_tour(self, id_player: int, tour: int) -> int:
        result = self.get_result_tour(tour)
        ans = 0
        for elem in result:
            forecast = self.get_forecast_match(id_player, elem[0])
            ans += helper_func.counting_of_points(elem[1], forecast)
        return ans
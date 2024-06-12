from loader import bot, base
from keyboards.reply import my_marcup
from image_creator import table_creator
from config_data import config
from telebot.types import Message


def show_player_list(id: int):
    msg = 'Текущий список участников: \n'
    for num, player in enumerate(base.get_all_id_player(), start=1):
        msg += str(num) + " " + player[1] + '\n'
    bot.send_message(id, msg)

def measure_difference(res, now_tour):
    ans = {}
    ss1 = sorted(res, key=lambda x: sum(x[config.TOUR1_COLUMN:now_tour - 1]))
    sss1 = {player[config.NICKNAME_COLUMN]: i for i, player in enumerate(ss1)}
    ss2 = sorted(res, key=lambda x: sum(x[config.TOUR1_COLUMN:now_tour - 2]))
    sss2 = {player[config.NICKNAME_COLUMN]: i for i, player in enumerate(ss2)}

    for player in res:
        nick = player[config.NICKNAME_COLUMN]
        ans[nick] = sss1[nick] - sss2[nick]
    return ans

    
    

@bot.message_handler(regexp="Посмотреть турнирную таблицу")
def check_result_tournament(message: Message) -> None:
    if not config.ALL_FUNCTION_READY:
        bot.send_message(message.chat.id, "Функция временно недоступна", reply_markup=my_marcup.main_menu_marcup())
        show_player_list(message.chat.id)
        return
    
    res = base.get_result_tournament()
    now_tour = base.get_now_tour()
    diff = measure_difference(res, now_tour)
    res.sort(key=lambda x: x[config.SUM_COLUMN], reverse=True)
    ans = []
    # player: nick, id, last_pos, tourN, sum
    for player in res:
        # user_data = [str(player[0])] + list(map(str, player[8:23])) + [str(player[33])]
        user_data = [str(player[config.NICKNAME_COLUMN])] + \
                    list(map(str, player[config.START_SHOW_TOUR_COLUMN:config.START_SHOW_TOUR_COLUMN + config.COUNT_TOUR_IN_TABLE])) + \
                    [str(player[config.SUM_COLUMN])]
        ans.append(user_data)
    table_creator.main_table(ans, now_tour, diff)
    bot.send_photo(message.chat.id, open("images/ready_tables/main_table.png", 'rb'))
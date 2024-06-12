from loader import bot, base
from telebot.types import Message
from config_data import config

@bot.message_handler(commands=["delete_user"])
def delete_user(message: Message) -> None:
    if str(message.chat.id) != config.ADMIN_ID:
        return
    if len(message.text.split() != 2):
        bot.send_message(config.ADMIN_ID, "Некорректная команда \n /delete_user <id>")
    user_id = message.text.split()[1]
    res = base.delete_player(user_id)
    if res:
        bot.send_message(user_id, "Вы удалены из турнира")
        bot.send_message(config.ADMIN_ID, "Аккаунт удален")
    else:
        bot.send_message(config.ADMIN_ID, "Аккаунт не найден")


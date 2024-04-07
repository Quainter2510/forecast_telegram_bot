from loader import bot, base
from telebot.types import Message

@bot.message_handler(commands=["delete"])
def delete_user(message: Message):
    base.delete_user(message.chat.id)
    bot.send_message(message.chat.id, "Вы успешно удалены")
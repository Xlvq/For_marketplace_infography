import sqlite3

import telebot

bot = telebot.TeleBot('Token')
name = None


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.reply_to(message, 'К сожалению данная функция пока недоступна')


@bot.message_handler(commands=['info'])
def main(message):
    bot.send_message(message.chat.id, 'Позже добавим информацию')


@bot.message_handler(commands=['price'])
def main(message):
    bot.send_message(message.chat.id, '1 слайд - 200 рублей(Обычно требуется 5-7 карточек)')


@bot.message_handler(commands=['portfolio'])
def main(message):
    with open('./Portfolio(1).pptx', 'rb') as f:
        file = f.read()
    bot.send_document(message.chat.id, file)


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет! Я работаю по направлению "Инфографика"')


bot.polling(none_stop=True)

# https://t.me/MyUNHelpBot

import telebot

from telebot import types

bot = telebot.TeleBot('6920375156:AAEKC-Q4hiZRNLBWS2IOT4r_2LVse13D9gU')

@bot.message_handler(commands=["start"])
def main(message):
    bot.send_message(message.chat.id, f'Привет, <b>{message.from_user.first_name}</b>!', parse_mode='html')


@bot.message_handler(commands=["help"])
def main(message):
    bot.send_message(message.chat.id, "<b>Справка по функциям бота</b>", parse_mode='html')
    

@bot.message_handler(content_types=["voice"])
def get_voice(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Напечатать сообщение в виде текста", callback_data="convert to text"))
    bot.send_message(message.chat.id, 'Выберите действие', reply_markup=markup)
    
@bot.message_handler(content_types=["text"])
def get_text(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Озвучить текст", callback_data="convert to voice"))
    bot.reply_to(message, 'Выберите действие', reply_markup=markup)

bot.polling(none_stop=True)
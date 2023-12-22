# https://t.me/MyUNHelpBot
import os
import subprocess
import logging
import telebot
from telebot import types
from txt2audio import text_to_audio
from audio2text import audio_to_text
from telebot.types import InputFile
from pathlib import Path

h_teg = ' '

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define the Telegram bot token
TOKEN = ''

# Initialize the bot
bot = telebot.TeleBot(TOKEN)


# Command handler for /start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Welcome to the UniHelper Bot!')

# Command handler for /switchmode command
@bot.message_handler(commands=['switchmode'])
def switch_mode(message):
    bot.reply_to(message, 'Switched')
# Message handler for audio input
@bot.message_handler(content_types=['voice'])
def voice_processing(message):
#    bot.reply_to(message, 'Audio-to-Text')
    os.remove('output_audio.wav')
    file_id = message.voice.file_id
    file = bot.get_file(file_id)
    file_path = file.file_path
    downloaded_file = bot.download_file(file_path)
    with open('input_audio.ogg', 'wb') as new_file:
        new_file.write(downloaded_file)
    subprocess.run(["ffmpeg-git-20231128-amd64-static/ffmpeg",
             "-loglevel", "quiet",
             "-i", "input_audio.ogg",
             "-ar", "16000",   # частота выборки
             "-ac", "1",       # кол-во каналов
             "-f", "s16le",    # кодек для перекодирования в wav
             "-", "output_audio.wav"]) 
    audio_text = audio_to_text('output_audio.wav')
    try:
        result_text = audio_text["text"]+h_teg 
        bot.reply_to(message, result_text)
#        bot.reply_to(message, h_teg)

    except KeyError as ke:
        bot.reply_to(message, 'error1')

# Message handler for text input 
@bot.message_handler(content_types=['text'])
def voice_processing(message):
#    bot.reply_to(message, 'Text-to-audio')
    text_input = message.text
    if "#" in text_input:
        global h_teg
        h_teg = '\n' + text_input
        bot.reply_to(message, h_teg)
    else:
        audio_waveform = text_to_audio(text_input)
        bot.send_voice(message.chat.id, InputFile(audio_waveform))

# Polling loop to keep the bot running
bot.polling(none_stop=True)

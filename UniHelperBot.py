import logging
import telebot
from telebot import types
from txt2audio import text_to_audio
from audio2text import audio_to_text

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define the Telegram bot token
TOKEN = ''

# Initialize the bot
bot = telebot.TeleBot(TOKEN)

# Define modes
TEXT_TO_AUDIO_MODE = 'text_to_audio'
AUDIO_TO_TEXT_MODE = 'audio_to_text'

# Initial mode
current_mode = TEXT_TO_AUDIO_MODE

# Command handler for /start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Welcome to the Text-to-Audio Bot!')

# Command handler for /switchmode command
@bot.message_handler(commands=['switchmode'])
def switch_mode(message):
    global current_mode
    if current_mode == TEXT_TO_AUDIO_MODE:
        current_mode = AUDIO_TO_TEXT_MODE
        bot.reply_to(message, 'Switched to Audio-to-Text mode. Send me an audio message for conversion.')
    else:
        current_mode = TEXT_TO_AUDIO_MODE
        bot.reply_to(message, 'Switched to Text-to-Audio mode. Send me text or a PDF file for conversion.')

# Message handler for text input or audio input based on the current mode
@bot.message_handler(func=lambda message: True)
def handle_input(message):
    if current_mode == TEXT_TO_AUDIO_MODE:
        handle_text_input(message)
    elif current_mode == AUDIO_TO_TEXT_MODE:
        handle_audio_input(message)

# Message handler for text input
def handle_text_input(message):
    text_input = message.text
    # Replace the following line with the actual logic from your text_to_audio module
    audio_waveform = text_to_audio(text_input)
    # Send the audio file to the user
    bot.send_voice(message.chat.id, audio_waveform)

# Message handler for audio input
def handle_audio_input(message):
    # Download the audio file
    if message.voice and message.voice.file_id:
        audio_file = bot.get_file(message.voice.file_id)
        audio_file.download('input_audio.ogg')

    # Use audio_to_text module to convert audio to text
    audio_text = audio_to_text('input_audio.ogg')

    # Replace the following line with the actual logic from your text_to_audio module
    audio_waveform = text_to_audio(audio_text)
    # Send the audio file to the user
    bot.send_voice(message.chat.id, audio_waveform)

# Polling loop to keep the bot running
bot.polling(none_stop=True)

import logging
import telebot
from telebot import types
from txt2audio import text_to_audio
from audio2text import audio_to_text

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Определение токена для Telegram бота
TOKEN = ''

# Инициализация бота
bot = telebot.TeleBot(TOKEN)

# Определение режимов
TEXT_TO_AUDIO_MODE = 'text_to_audio'
AUDIO_TO_TEXT_MODE = 'audio_to_text'

# Текущий режим
current_mode = TEXT_TO_AUDIO_MODE

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Добро пожаловать в бот Text-to-Audio!')

# Обработчик команды /switchmode
@bot.message_handler(commands=['switchmode'])
def switch_mode(message):
    global current_mode
    if current_mode == TEXT_TO_AUDIO_MODE:
        current_mode = AUDIO_TO_TEXT_MODE
        bot.reply_to(message, 'Переключено в режим Audio-to-Text. Отправьте мне аудиосообщение для преобразования.')
    else:
        current_mode = TEXT_TO_AUDIO_MODE
        bot.reply_to(message, 'Переключено в режим Text-to-Audio. Отправьте мне текст или файл PDF для преобразования.')

# Обработчик сообщений для текстового ввода или аудиоввода в зависимости от текущего режима
@bot.message_handler(func=lambda message: True)
def handle_input(message):
    if current_mode == TEXT_TO_AUDIO_MODE:
        handle_text_input(message)
    elif current_mode == AUDIO_TO_TEXT_MODE:
        handle_audio_input(message)

# Обработчик сообщений для текстового ввода
def handle_text_input(message):
    text_input = message.text
    # Замените следующую строку на фактическую логику из вашего модуля text_to_audio
    audio_waveform = text_to_audio(text_input)
    # Отправить аудиофайл пользователю
    bot.send_voice(message.chat.id, audio_waveform)

# Обработчик сообщений для аудиоввода
def handle_audio_input(message):
    # Загрузка аудиофайла
    if message.voice and message.voice.file_id:
        audio_file = bot.get_file(message.voice.file_id)
        audio_file.download('input_audio.ogg')

    # Использование модуля audio_to_text для преобразования аудио в текст
    audio_text = audio_to_text('input_audio.ogg')

    # Замените следующую строку на фактическую логику из вашего модуля text_to_audio
    audio_waveform = text_to_audio(audio_text)
    # Отправить аудиофайл пользователю
    bot.send_voice(message.chat.id, audio_waveform)

# Цикл опроса для продолжения работы бота
bot.polling(none_stop=True)

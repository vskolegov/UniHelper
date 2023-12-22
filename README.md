## Программа для автоматизированного создания заметок
Программа, которая помогает студентам эффективно работать с большим объемом
информации и литературы. Приложение предоставляет возможность создавать
заметки, фиксировать важные моменты и идеи по книгам и темам.

Телеграм-бот для преобразования текста в звук и обратно
Ссылка на телеграм-бот https://t.me/MyUNHelpBot
![OIG.jpeg](https://github.com/santerr80/UniHelper/blob/main/OIG.jpeg)

### Начало работы:
#### Описание:
```import logging
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
```
Данный код представляет собой пример простого телеграм-бота, написанного на Python
с использованием библиотеки telebot. Бот реагирует на команды /start и /help, а также
обрабатывает голосовые и текстовые сообщения, предлагая пользователю различные варианты действий.
#### Установка:
Для работы с данным кодом необходимо установить библиотеку telebot. Это можно сделать с помощью pip:
```pip install pyTelegramBotAPI```
#### Использование:
-  Зарегистрируйте нового бота в Telegram через @BotFather и получите токен.
-  Вставьте токен в строку ```bot = telebot.TeleBot('YOUR_TOKEN_HERE')``` .
-  Запустите код.
#### Функционал:
- При получении команды /start бот отправляет приветственное сообщение с именем пользователя.
- При получении команды /help бот отправляет справку по функциям.
- При получении голосового сообщения бот предлагает конвертировать его в текст.
- При получении текстового сообщения бот предлагает озвучить его.
#### Запуск:
Для запуска бота необходимо вызвать метод:
``` bot.polling(none_stop=True) ```
#### Требования к окружению:
- Python 3.x
- Библиотека telebot
### Основные функции приложения:
Создание заметок, приложение предоставляет удобный интерфейс, который
позволяет создавать заметки с помощью печатного ввода или голосового ввода
с автоматическим переводом в текстовый формат. Это
дает возможность быстро и удобно запечатлеть все важные моменты и идеи,
даже если у вас нет возможности печатать.
Организация заметок существующие заметки автоматически сортируются по
темам и книгам, что позволяет быстро находить нужную информацию.Можно
просматривать заметки в текстовом формате или воспроизводить их в аудио
формате. Это делает процесс повторения и освоения материала более удобным и
эффективным.


### Команда проекта
- **Менеджер проекта/Scrum-мастер:** Красильников М.Н.
- **Аналитик данных/Data Scientist:** Колегов В.С.
- **Инженер по машинному обучению (ML Engineer):** Ибатулин А.А. 
- **Full Stack-разработчик:** Горбунов А.В.
- **Тестировщик-QA инженер:** Черенков К.Н. 
- **Документалист/технический писатель:** Тимонин И.Л., Бондаренко Н.А.
### Лицензия
![LICENSE](https://github.com/santerr80/UniHelper/blob/main/LICENSE)

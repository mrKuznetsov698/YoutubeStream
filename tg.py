import config
import parsing
from telebot import TeleBot
from telebot.types import *
bot: TeleBot = None


def setup(set_p, clr_p):
    global bot
    bot = TeleBot(config.BOT_TOKEN)

    @bot.message_handler(commands=['set'], regexp=r"/set \d+ \d+", func=lambda x: x.chat.id == config.ALLOWED_ID)
    def set_pix(ms: Message):
        error, x, y = parsing.parse_string(ms.text[5:])
        if error != 0:
            return
        set_p(x, y)
        print(ms.chat.id)

    @bot.message_handler(commands=['clr'], regexp=r"/clr \d+ \d+", func=lambda x: x.chat.id == config.ALLOWED_ID)
    def clr_pix(ms: Message):
        error, x, y = parsing.parse_string(ms.text[5:])
        if error != 0:
            return
        clr_p(x, y)
        print(ms.chat.id)


def polling():
    bot.polling(interval=1, logger_level=logging.INFO)

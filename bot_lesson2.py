# Импортируем нужные компоненты
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Настройки прокси
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080', 'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
					level=logging.INFO,
					filename='logs/bot.log'
					)

def greet_user(bot, update):
	text = 'Привет!'
	print(text)
	update.message.reply_text(text)
	# print('Привет!')

def talk_to_me(bot, update):
	user_text = update.message.text
	print('Пользователь написал: ' + user_text)
	update.message.reply_text('Ваше обращение будет обработано')

# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
def main():
	mybot = Updater("587083051:AAEjr2LTJc224qZjRyuFTED059vnYHJ0Qt8", request_kwargs=PROXY)

	dp = mybot.dispatcher
	dp.add_handler(CommandHandler("start", greet_user))
	dp.add_handler(MessageHandler(Filters.text, talk_to_me))
	mybot.start_polling()
	mybot.idle()

# Вызываем функцию - эта строчка собственно запускает бота
main()

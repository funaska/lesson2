# Написать функцию ask_user() чтобы с помощью input() спрашивать пользователя “Как дела?”, пока он не ответит “Хорошо”
# При помощи функции get_answer() отвечать на вопросы пользователя в ask_user(), пока он не скажет “Пока!”

# Переписать функцию ask_user(), добавив обработку exception-ов
# Добавить перехват ctrl+C и прощание

from lesson_one import get_answer
import sys

while True:
	try:
		answer = input()
		print( get_answer(answer) )
		if answer.lower() == 'пока!':
			sys.exit('До встречи!')
	except KeyboardInterrupt:
		sys.exit('\nЗря ты так...')

# Написать функцию ask_user() чтобы с помощью input() спрашивать пользователя “Как дела?”, пока он не ответит “Хорошо”
# При помощи функции get_answer() отвечать на вопросы пользователя в ask_user(), пока он не скажет “Пока!”

from from_lesson_one import get_answer
import sys

while True:
	answer = input()
	print(get_answer(answer))
	if answer.lower() == 'пока!':
		sys.exit('До встречи!')

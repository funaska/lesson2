import string

def get_answer(question):
	answers_dict = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
	# table = question.maketrans({key: None for key in string.punctuation})
	# new_question = question.translate(table, string.punctuation)
	exclude = set(string.punctuation)
	question = ''.join(ch for ch in question if ch not in exclude)
	return answers_dict.get(question.lower(),'я тебя не понимаю')

if __name__ == '__main__':
	answers_dict = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}

	user_question = input('Введите слово: ')

	print(get_answer(user_question,answers_dict))

# Сравнение строк
# Написать функцию, которая принимает на вход две строки.
# Если строки одинаковые, возвращает 1.
# Если строки разные и первая длиннее, возвращает 2.
# Если строки разные и вторая строка 'learn', возвращает 3.

def str_compare(first_str,second_str):
	if first_str ==  second_str:
		return(1)
	elif len(first_str) > len(second_str):
		return(2)
	elif second_str == 'learn':
		return(3)

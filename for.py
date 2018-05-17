# Оценки
# Создать список с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
# Посчитать и вывести средний балл по всей школе.
# Посчитать и вывести средний балл по каждому классу.

def avg_grade(grades_dict,is_whole=0):
	all_grade = 0
	all_length = 0
	for cur_class in grades_dict:
		# print(cur_class)
		if not is_whole:
			print('Средний балл по классу',cur_class['school_class'],sum(cur_class['scores'])/len(cur_class['scores']))
		else:
			all_grade += sum(cur_class['scores'])
			all_length += len(cur_class['scores'])
	if is_whole:
		all_avg_grade = all_grade/all_length
		print('Средний балл по всей школе:',all_avg_grade)

grades_dict = [{'school_class': '4a', 'scores': [3,4,4,5,2]},
{'school_class': '3a', 'scores': [3,3,2,1,4]},
{'school_class': '2a', 'scores': [5,5,5,3,4]},
{'school_class': '1a', 'scores': [2,5,4,4,3]}
]

avg_grade(grades_dict)
avg_grade(grades_dict,1)

# Возраст
# Попросить пользователя ввести возраст.
# По возрасту определить, чем он должен заниматься: учиться в детском саду, школе, ВУЗе или работать.
# Вывести занятие на экран.

age = int(input('Введите возраст:'))
if age < 4:
	print('Иди в детский сад!')
elif age < 18:
	print('Иди в школу!')
elif age < 22:
	print('Иди в ВУЗ!')
else:
	print('Иди работать!')

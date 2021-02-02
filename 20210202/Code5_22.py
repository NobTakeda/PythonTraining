def eat(breakfast,lunch='ラーメン',dinner='カレー'):
	print(f'朝は{breakfast}を食べました')
	print(f'昼は{lunch}を食べました')
	print(f'夜は{dinner}を食べました')

eat('トースト','おにぎり')
print('********')
eat('バナナ','蕎麦','焼肉')
print('********')
eat('トースト')
print('********')
eat('トースト',dinner='焼きそば')

def eat(breakfast,lunch,dinner='カレー',desserts=()):
	print(f'朝は{breakfast}を食べました')
	print(f'昼は{lunch}を食べました')
	print(f'夜は{dinner}を食べました')
	for d in desserts:
		print(f'おやつに{d}を食べました')

"""
eat(breakfast='納豆ご飯',dinner='カレーうどん')
eat(dinner='カレーうどん',breakfast='納豆ご飯')
eat('納豆ご飯',dinner='カレーうどん')
"""
"""
error
eat(dinner='カレーうどん','納豆ご飯')
"""
print('hoge','huga',sep='&',end='!')
print()

eat('トースト','パスタ','カレー',('アイス','チョコ','パフェ'))

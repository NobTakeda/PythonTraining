name='松田'
def change_name():
	global name
	#この宣言で、関数内のnameをグローバル変数として扱うことができる。
	#宣言と同時に中身を代入できないことに注意
	name='浅木'
	print(name)
	
def hello():
	print('こんにちは'+name+'さん')

change_name()
hello()

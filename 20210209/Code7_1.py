text=input('何を記録しますか?>>')
#'a'で追記する
with open('diary.txt','a') as file:
	file.write(text+'\n')

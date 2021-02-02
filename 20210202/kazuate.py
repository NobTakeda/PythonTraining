import random

ans=random.randint(1,100)
max_count=5
print('1~100の数字の中から一つ選んだよ')
print('その数字を',max_count,'回以内に当ててね')

for i in range(1,max_count+1):#i回目、と表示したいので1から回している
	print(i,'回目、いくつかな?')
	num=int(input())
	if num==ans:
		print('当たり！')
		break
	#処理なしの時はpassすること
	elif i==max_count:
		pass
	elif num>ans:
		print('もっと下だよ')
	else:
		print('もっと上だよ')
#Pythonではfor-elseでfor文が回りきった後の処理を書くことができる。
else:
	print('残念、正解は',ans,'でした')

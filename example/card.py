import random
#0=奴隷,1=市民,2=皇帝とする
mycards=[0,1,1,1,1]
pccards=[2,1,1,1,1]

print('ようこそeカードゲームへ')
input('enter>>')
count=1
while True:
	print('{}戦目'.format(count))
	slave,civ=0,0
	for i in range(len(mycards)):
		if mycards[i]==0:
			slave+=1
		elif mycards[i]==1:
			civ+=1
	print('手持ちのカード:市民{}枚　奴隷{}枚'.format(civ,slave))
	hand=int(input('カード選択、「市民」なら「0」、「奴隷」なら「1」を入力>>'))
	print('カードオープン！')
	input('enter>>')
	pchand=random.randrange(2)
	if pchand==0:
		if hand==0:
			print('あなた:市民  PC:皇帝')
			print('あなたの負け!')
			print('GameOver')
			break
		else:
			print('あなた:奴隷  PC:皇帝')
			print('あなたの勝ち!')
			print('コングラッチュレーション…！')
			break
	else:
		if hand==1:
			print('あなた:奴隷  PC:市民')
			print('あなたの負け!')
			print('GameOver')
			break
		else:
			print('あなた:市民  PC:市民')
			print('引き分け!')
			mycards.pop(-1)
			pccards.pop(-1)
			count+=1
			input('enter>>')

import random
handlist=['グー','チョキ','パー']
while True:
	hand=int(input('手を入力[0:グー,1:チョキ,2:パー]>>'))
	pcHand=random.randrange(0,2)
	if (hand-pcHand+3)%3==0:
		print(f'あなたは{handlist[hand]},PCは{handlist[pcHand]}')
		print('あいこ')
	elif (hand+pcHand+3)%3==1:
		print(f'あなたは{handlist[hand]},PCは{handlist[pcHand]}')
		print('あなたの負け')
		break
	else:
		print(f'あなたは{handlist[hand]},PCは{handlist[pcHand]}')
		print('あなたの勝ち')
		break

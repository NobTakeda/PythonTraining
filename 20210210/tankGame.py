import random 
damage=0
MAX_DAYS=100
total_kill=0
titles=['鉄十字勲章','騎士鉄十字勲章','柏葉付騎士鉄十字勲章','柏葉・剣付騎士鉄十字勲章','柏葉・剣・ダイヤモンド付騎士鉄十字勲章','黄金柏葉・剣・ダイヤモンド付騎士鉄十字勲章']

for i in range(MAX_DAYS):
	if damage>0:damage-=1
	print(f'{i}日めの行動')
	if damage>0:
		print(f'あと{damage}日の入院が必要です')
		input(f'今は休んでくださいね(Enter)')
	else:
		print('出撃!')
		kill=random.randint(1,15)
		total_kill+=kill
		print(f'戦功報告:{kill}輛の戦車を撃破しました!')
		health=random.randrange(100)
		if health==0:
			print('あなたは戦死してしまいました…')
			break
		elif 1<= health <=10:
			damage=7
			print(f'あなたは撃墜され、怪我をしてしまいました。{damage}日間の入院が必要です')
		else:
			input('明日も頑張りましょう!(Enter)')
else:
	print('戦争は終結しました！')
print(f'最終戦果報告!! あなたは{total_kill}輌の戦車を破壊した功績により{titles[min(total_kill//100,5)]}を授与されました!!')

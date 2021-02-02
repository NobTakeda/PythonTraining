food='カレーライス'
if 'カレー' in food:
	print('カレーが含まれています')

food2='寿司'
if not 'カレー' in food2:
	print('カレーが含まれていません')

if 'カレー' not in food2:
	print('カレーが含まれていません')

score=80
if 60 < score < 80: #条件への挟み込みができる
	print('60点より大きく80点より小さい')

isError=False
n=50
if isError and n<100:
	pass

num=10
if num%2==0:
	print('偶数です')

aisatsu='さようなら'
if aisatsu=='こんにちは':
	print('ようこそ')
elif aisatsu=='景気は?':
	print('ぼちぼちです')
elif aisatsu=='さようなら':
	print('お元気で')
else:
	print('どうしました')

month =int(input('今は何月ですか？>>'))
if month in[1,3,5,7,8,10,12]:
	print('31日までありますね')
else:
	if month != 2:
		print('30日までですね')
	else:
		print('1年で一番寒い月ですね')
	print('年が明けてから')
print('{}ヶ月が過ぎました'.format(month))

#三項演算子
div='偶数' if number%2==0 else '奇数'
print(f'{div}です')

result='優' if score >= 80 else '良' if score >= 60 else '可'if score >=40 else '不可'

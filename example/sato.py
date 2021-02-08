import random,pprint

nums=[[(3*i+j) for j in range(1,4)] for i in range(3)]
print('***宝探し***')
"""
for i in range(len(nums)):
	print(nums[i])
"""
target=nums[random.randrange(3)][random.randrange(3)]
#print(target)

count=1
isHit=True
while isHit:
	for i in range(len(nums)):
		print(nums[i])
	chosen_num=int(input('好きな場所の数字を選んで入力してください>>'))
	for i in range(3):
		if isHit==False:
			break
		else:
			for j in range(3):
				if chosen_num==3*i+j+1:
					if chosen_num == target:
						nums[i][j]='O'
						for i in range(len(nums)):
							print(nums[i])
						print('お宝を見つけました！')
						print(f'あなたはお宝を{count}回で発見しました！')
						isHit=False
						break
					elif nums[i][j] == 'X':
						print('選択済みの場所です')
						count+=1
					elif chosen_num > target:
						print('ハズレです。ここより小さな数字の場所にあります')
						nums[i][j]='X'
						count+=1
					elif chosen_num < target:
						print('ハズレです。ここより大きな数字の場所にあります')
						nums[i][j]='X'
						count+=1

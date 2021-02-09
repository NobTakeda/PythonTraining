import random
import sys
print('数当てゲーム！3桁の数を当ててください！')
answer=[random.randint(0,9) for _ in range(3)]
#print(answer)
is_continue=True
while is_continue:
	hit=0
	ball=0
	prediction=[]
	for i in range(3):
		prediction.append(int(input(f'{i+1}桁目の数字を入力>>')))
	for i in range(3):
		is_hit=False	
		for j in range(3):
			if prediction[i]==answer[i]:
				is_hit=True		
			elif prediction[j]==answer[i]:
				ball+=1
		if is_hit==True:
			hit+=1
	if hit==3:
#		print(f'正解>>{answer}')
#		print(f'あなたの入力>>{prediction}')
		print('正解です！')
		is_continue=False
		break
	else:
#		print(f'あなたの入力>>{prediction}')
		print(f'{hit}ヒット！{ball}ボール！！')
		is_play=(int(input('続けますか？ 1:続ける 2:終了>>')))
		if is_play==2:
			is_continue=False
		else:
			is_continue=True	

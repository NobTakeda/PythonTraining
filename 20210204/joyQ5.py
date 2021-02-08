import random
randomBalls=[random.randrange(1,99) for _ in range(99)]
balls=[randomBalls[i] for i in range(99)]
#ballsにランダムな数字を順番に格納
count=1
winA=0
winB=0
for i in range(5):
	n1=balls.pop(random.randrange(99-i*2))
	n2=balls.pop(random.randrange(98-i*2))
	if n1>n2:
		print(f'{count}回戦')		
		print(f'A:{n1},B;{n2}…Aの勝ち')
		count+=1
		winA+=1
	elif n2>n1:
		print(f'{count}回戦')		
		print(f'A:{n1},B;{n2}…Bの勝ち')
		count+=1
		winB+=1
result='Aの勝ち' if winA>winB else 'Bの勝ち'
print(f'{winA}対{winB}で{result}')

	

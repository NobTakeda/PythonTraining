import random

answers=[]
isAppear=False
index=0;
for i in range(100):
	ele=random.randint(1,100)	
	answers.append(ele)
	if ele==77:
		if isAppear==False:
			index=i
			isAppear=True	
		else:
			pass
else:
	print(answers)
	if isAppear==True:
		print('77が最初に格納されたindexは',index,'です')
	else:
		print('77->なし')

for i in range(1,10):
	for j in range(1,10):
		if i%2==0:
			continue
		elif i*j>50:
			continue
		else:
			if i*j<10:
				print('',i*j,end=' ')
			else:
				print(i*j,end=' ')
	print('')	

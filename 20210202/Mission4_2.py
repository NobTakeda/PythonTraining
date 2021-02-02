height=int(input('何段の階段を作る?>>'))
count=height-1
for i in range(height):
	for j in range(1,height+1):
		if(i+j)>=height:
			print('*',end='')
		else:
			print(' ',end='')
	print('')
"""
for i in range(height):
	for j in range(height):
		print(' ' if j<height-i-1 else '*',end='')
	print()
"""

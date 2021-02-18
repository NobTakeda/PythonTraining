import string

letters=string.ascii_letters
width=int(input('何幅>>'))
#divide=len(letters)//width if len(letters)%width == 0 else len(letters)//width+1

data=[]
for i in range(0,len(letters),width):
	letter=letters[i:i+width]
	print(letter)
	data.append(letter)
	
row=int(input(f'何行目(1-{len(data)})>>'))
print(data[row-1])

"""
ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(divide):
	for j in range(width):
		if (width*i+j)<len(ascii_letters):
			print(ascii_letters[width*i+j],end='')
		else:
			break
	print()
"""
"""
for i in range(len(letters)):
	print(letters[i],end='')
	if (i+1) % width ==0:
		print()
print()

for i,c in enumerate(letters):
	print(c,end='')
	if (i+1)%width==0:
		print()
print()
"""


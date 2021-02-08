import random
import pprint
table=[[random.randint(0,9) for j in range(3)]for i in range(3)]
for row in table:
	print(row)
print('******')	

vertical=[[table[j][i] for j in range(3)] for i in range(3)]
for row in vertical:
	print(row)
print('******')	
	
closs=[[table[j][j] if i==0 else table[j][2-j]  for j in range(3)]for i in range(2)]
for row in closs:
	print(row)

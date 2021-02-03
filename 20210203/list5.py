import pprint

x=[n for n in range(1,8)]
print(x)

x=[n**2 for n in range(1,8)]
print(x)

x=[n for n in range(1,8) if n%2==0]
print(x)
"""
x=list()
for n in range(1,8):
	if n%2==0:
		x.append(n)
"""

x=[i*10+j for i in range(1,3) for j in range(2,5)]
print(x)
"""
x=list()
for n in range(1,3):
	for j in range(2,5)
		x.append(i*10+j)
"""

x=[[i*10+j for j in range(7,10)] for i in range(1,3)]
print(x)

row=col=3
matrix=[[1 if i==j else 0 for j in range(col)] for i in range(row)]
"""
matrix2=[]
for i in range(row):
	temp=[]
	for j in range(col):
		temp.append(1 if i==j else 0)
	matrix2.append(temp)
"""


print('********')
W=10
H=10
data=[[(i*10)+(j+1) for j in range(W)] for i in range(H)]
pprint.pprint(data)

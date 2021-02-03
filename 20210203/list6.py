import pprint
W=10
H=10
"""
藤村さん
data=[[(i*10)-(j*10) for j in range(W)]for i in range(H)]
"""
"""
佐久間さん
data=[[100-i*10-j for j in range(W)] for i in range(H)]
"""
"""
自分
data=[[1 if i==j or (i+j)==4 else 0 for j in range(5)]for i in range(5)]
"""
"""
佐藤さん
data=[]
for i in range(5):
	temp=[]
	for j in range(5):
		if i==j:
			temp.append(1)
		elif i>j:
			temp.append(2)
		else:
			temp.append(0)
	data.append(temp)
"""
"""
野本さん
data=[[i+1 if i==j else 0 for j in range(4)]for i in range(3)]
"""
"""
松尾さん
data=[[(60+i*10)+j for j in range(9)] for i in range(4)]
"""
"""
廣瀬さん
data=[[i*j for j in range(1,10)]for i in range(1,10)]
"""
"""
端本
data=[[3 if i*j==1 else 7 for j in range(3)]for i in range(3)]
"""
"""
狩野さん
data=[[i*(j+1) for j in range(9)]for i in range(3,10) if i%2==1]
"""
"""
古屋さん
data=[[(j+1)*2 if i==0 else j*2+1 for j in range(5)]for i in range(2)]
"""
"""
上杉さん
data=[['*' if i%2==0 and j%2==1 else '_' for j in range(10)]for i in range(10)]
"""
"""
早坂さん
data=[[i*i+j for j in range(10)]for i in range(10)]
"""

pprint.pprint(data)

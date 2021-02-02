tuple1=(3,5,7)
#タプルは中身の修正ができない。
print(len(tuple1))
print(tuple1[1])
print(sum(tuple1))

list1=list(tuple1) #タプルをリストに変換することは可能
print(list1)
list1.append(10)
print(list1)

a,b,c=tuple1
print(a,b,c)

x=10
y=20
x,y=y,x #2値の入れ替えが1行で済む
print(x)
print(y)

userinfo = input('名前と血液型をカンマで区切って1行で入力>>')
[name,blood]=userinfo.split(',')
blood=blood.upper().strip()
name=name.title()
sumName=name.count(name)
print(f'{name}さんは{blood}型なので大吉です')
print(f'{name}さんは{sumName}回出てきました')

l1=['3','5','6']
print('&'.join(l1))
#splitの反対。結合

str=('abeakoegaekaogeakajoegoawgje')
print(str.count('a'))
print(str.replace('a','&'))

for s in 'hello':
	print(s)

#enumerateで、第一引数の文字列のindex0を第二引数で指定した数として回す
for i,s in enumerate('hello',1):
	print(f'{i}文字目は{s}です')

s1='hello'
s2=list(reversed(s1))
print(s2)
print(''.join(s2))

s3=s1[::-1]
print(s3)

print(len(s1))

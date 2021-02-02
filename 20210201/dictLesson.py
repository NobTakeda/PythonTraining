dict1=dict() #要素が空のディクショナリを宣言
dict1['apple']='りんご' #keyとvalueを指定しながらディクショナリに追加
dict1['orange']='オレンジ'
print(dict1)

print(len(dict1)) #要素数を取得
dict1['banana']='バナナ'

del dict1['orange']
print(dict1)

print(dict1['apple']) #keyを指定でvalueを表示

#print(dict1['pine']) #error
print(dict1.get('pine')) #.get(key)だと、中身がなかったらNoneが返る

if 'apple' in dict1:
	print('含まれている')

if 'pine' not in dict1:
	print('含まれていません')

if 'りんご' in dict1.values(): #valueを判定
	print('含まれています')

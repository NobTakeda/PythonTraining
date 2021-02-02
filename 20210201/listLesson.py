list1=[] #からのリスト
list2=list() #空のリストその2

list1.append(3)
print(list1)
list1.append(5)
print(list1)
print(list1[0])

list2.append(10)
list2.append(20)
print(list2)

list3=list1+list2
print(list3) #リスト同士を足すと、中身を結合したリストになる

list4=list3*3
print(list4) #リストを掛けると、中身をその数だけ繰り返したリストになる

print(len(list4)) #要素数
print(sum(list4)) #リスト内の合計

del list4[0] #指定indexの要素を消す
print(list4)

list4.remove(5) #指定した引数の最初の1個を消す
print(list4)

list5=list4[3:8] #list4のindex3以上8未満を指定
print(list5)

print(list5[-1]) #indexを負の数にすると、後ろから取得

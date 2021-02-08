import random
playNum=int(input('サイコロを何回振る?>>'))
dicelist=[(random.randrange(6)+1) for i in range(playNum)]
dices={dicelist[i] for i in range(len(dicelist)) }
print(dicelist)
print(f'合計は{dices}の{len(dices)}種類でした')

import random
playNum=int(input('サイコロを何回振る?>>'))
dices=[(random.randrange(6)+1) for i in range(playNum)]
print(dices)
print(f'合計は{sum(dices)}でした')

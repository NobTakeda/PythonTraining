import random
playNum=int(input('100~1000の範囲の偶数をいくつ生成する?>>'))
data=[random.randrange(100,1000,2) for i in range(playNum)]
data.sort(reverse=True)
print(f'{playNum}個生成しました！降順表示すると{data}')
		

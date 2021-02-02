def calc_average(scores):
	avg=sum(scores)/len(scores)
	print(f'平均点は{avg}です')

calc_average([10,20,33])
calc_average((10,20,33))
calc_average(range(100))
calc_average({20,20,30,10,40})

def plus(x,y):
	answer=x+y
	return answer

ans=plus(8,19)
print(ans)

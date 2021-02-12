def sum_num(num):
	result=[i for i in range(1,num+1)]
	#result=0
	#for i in range(1,num+1):
	#	result+=i
	print(sum(result))

def sumof(n):
	return sum(range(1,n+1))

def sumof2(n):
	ls=[i for i in range(1,n+1)]
	return (sum(ls))

def sumof3(n):
	if n<=1:
		return n
	else:
		return n+sumof3(n-1)

sum_num(int(input('正の整数>>')))
num=sumof(int(input('もう一度正の整数>>')))
print(num)
number=sumof3(int(input('再帰処理>>')))
print(number)

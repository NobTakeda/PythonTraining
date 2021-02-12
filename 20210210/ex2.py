def factorial(num):
	if num<=1:
		return num
	else:
		return num*factorial(num-1)

result=factorial(int(input('正の整数>>')))
print(result)

def get_gcd(x,y):
	if x%y==0:
		return y
	else:
		return get_gcd(y,x%y)

"""
	r=x%y
	while True:
		num=y%r
		if num==0:
			return r
			break
		else:
			y,r=r,num
"""	

x=(int(input('長辺を入力>>')))
y=(int(input('短辺を入力>>')))
gcd=get_gcd(x,y)
print(gcd)

import turtle
t1=turtle.Turtle()
t1.shape('turtle')
t1.color('blue')
t2=turtle.Turtle()
t2.shape('turtle')
t2.color('red')
t3=turtle.Turtle()
t3.shape('turtle')
t3.color('green')

ts=[t1,t2]
ts[1].right(5)
def make_square2(ts):
	for i in range(4):
		for j in range(2):
			ts[j].forward(100)
			ts[j].right(90)
		else:
			ts[j].right(10)

def make_spiral(ts):
	for j in range(2):
		for i in range(36):
			make_square2(ts)

make_spiral(ts)
turtle.mainloop()

import random
import turtle
ts=[]

def setup():
	global ts
	startline=-620
	screen=turtle.Screen()
	screen.setup(1290,720)
	screen.bgpic('pavement.gif')
	
	t_y=[-40,-20,0,20,40]
	t_color=['deepskyblue','red','orchid','yellow','lime']

	for i in range(len(t_y)):
		t=turtle.Turtle()
		t.shape('turtle')
		t.penup()
		t.setpos(startline,t_y[i])
		t.color(t_color[i])
		t.pendown()
		ts.append(t)

def race():
	global ts
	finishline=440

	while True:
		for current_t in ts:
			move=random.randint(1,50)
			current_t.forward(move)

			x=current_t.xcor()
			if x >=finishline:
				winner_color=current_t.color()
				current_t.write('WIN!! '+winner_color[0],font=('HackGen35',20,'normal'))
				break
		else:
			continue
		break

setup()
race()
turtle.mainloop()

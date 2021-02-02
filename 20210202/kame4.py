import turtle
t=turtle.Turtle()
t.shape('turtle')
for i in range(5):
	t.forward(100)#向いている方向に100移動
	t.right(144)#90度回転
t.home() #原点に移動し、デフォルトの方向を向く(右側)
turtle.mainloop()

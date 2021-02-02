import turtle
t=turtle.Turtle()
t.shape('turtle')
t.circle(100)#円を描く
t.forward(100)#向いている方向に100移動
t.right(90)#90度回転
t.forward(100)
t.home() #原点に移動し、デフォルトの方向を向く(右側)
turtle.mainloop()

import tkinter as tk
root=tk.Tk()
root.title('My Window')#Windowのタイトル
root.geometry('600x400')#Windowの大きさ
#文字出力のためのラベルを作成
label=tk.Label(root,text='Hello World!',font=('HackGen35',50))
#labelを配置
label.place(x=100,y=100)

btn=tk.Button(root,text='Click Me!',font=('HackGen35',50))
btn.place(x=100,y=200)
root.mainloop()

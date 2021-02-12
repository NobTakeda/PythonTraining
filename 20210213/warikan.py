import tkinter as tk

FNT=("Times New Roman",16)

root=tk.Tk()
root.title('割り勘くん')
canvas=tk.Canvas(root,width=300,height=600)
canvas.pack()
label=tk.Label(root,text='金額',anchor=tk.NW)
label.pack()
total_price=tk.Entry(width=30,font=FNT)
total_price.place(x=20,y=40)
label2=tk.Label(root,text='金額',anchor=tk.NW)
label2.pack()
member=tk.Entry(width=30,font=FNT)
member.place(x=20,y=80)
button=tk.Button(text='計算する',font=FNT)
button.place(x=20,y=120)

root.mainloop()

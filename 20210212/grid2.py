import tkinter

root=tkinter.Tk()
root.geometry('300x200')

la=tkinter.Label(root,text='Hello everyBody',relief=tkinter.RIDGE,bg='yellow')
la.place(x=10,y=30)

lb=tkinter.Label(root,text='Oh My God',bg='red',bd=2)
lb.place(x=10,y=10)

lc=tkinter.Label(root,text='See you tomorrow',bg='LightSkyBlue')
lc.place(x=30,y=40)

root.mainloop()

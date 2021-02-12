import tkinter

root=tkinter.Tk()
root.geometry('300x200')

la=tkinter.Label(root,text='Hello everyBody',relief=tkinter.RIDGE,bg='yellow')
la.grid(row=0,column=0,columnspan=2,padx=5,pady=5,sticky=tkinter.W+tkinter.E)
la=tkinter.Label(root,text='Oh My God',bg='red',bd=2)
la.grid(row=1,column=0,padx=5,pady=5)
la=tkinter.Label(root,text='See you tomorrow',bg='LightSkyBlue')
la.grid(row=1,column=1,padx=5,pady=5)
root.mainloop()

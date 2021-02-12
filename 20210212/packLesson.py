import tkinter

root=tkinter.Tk()
root.geometry('300x200')

btn=tkinter.Button(root,text='開始',width=14)
btn.pack(fill='x',padx=20,side='left')
btn=tkinter.Button(root,text='終了',width=14)
btn.pack(fill='x',padx=30,pady=10,ipady=20,side='left')
#fill>>指定した軸に対して一杯にする

root.mainloop()

import tkinter as tk

root=tk.Tk()
root.title('UI Test')
root.geometry('800x600')
root['bg']='#333'

main=tk.Frame(root,width=600,height=400,bd=5,relief='sunken',bg='#333')
main.grid(row=0,column=0,sticky=tk.NW)
player=tk.Frame(root,width=200,height=400,bd=3,relief='raised',bg='#555')
player.grid(row=0,column=1,sticky=tk.NE)
inventry=tk.Frame(root,width=200,height=200,bd=3,relief='raised',bg='tan')
inventry.grid(row=1,column=1,sticky=tk.SE)
status=tk.Frame(root,width=600,height=200,bd=3,relief='raised',bg='#4682b4')
status.grid(row=1,column=0,sticky=tk.SW)


root.mainloop()

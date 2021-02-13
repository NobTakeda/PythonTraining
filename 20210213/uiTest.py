import tkinter as tk

FNT=('HackGen35',10)
root=tk.Tk()
root.geometry('800x640')
root.title('UItest')
root.bg=['#333']

main=tk.Label(root,width=600,height=400,bg='#666')
main.place(x=0,y=0)
player=tk.Label(root,width=200,height=300,bg='#555')
player.place(x=600,y=0)
inventry=tk.Label(root,width=200,height=150,bg='brown')
inventry.place(x=600,y=300)
status=tk.Label(root,width=450,height=150,bg='#55c')
status.place(x=0,y=400)

health=tk.Label(status,text='health',width=50,height=20,font=FNT,relief=tk.RIDGE,bg='LightSkyBlue')
mana=tk.Label(status,text='mana',width=50,height=20,font=FNT,relief=tk.RIDGE,bg='LightSkyBlue')
stamina=tk.Label(status,text='stamina',width=50,height=20,font=FNT,relief=tk.RIDGE,bg='LightSkyBlue')

health_num=tk.Label(status,text='100',width=50,height=20,font=FNT,relief=tk.RIDGE,bg='LightSkyBlue')
mana_num=tk.Label(status,text='100',width=50,height=20,font=FNT,relief=tk.RIDGE,bg='LightSkyBlue')
stamina_num=tk.Label(status,text='25',width=50,height=20,font=FNT,relief=tk.RIDGE,bg='LightSkyBlue')

strength=tk.Label(status,text='strength',width=50,height=20,font=FNT,relief=tk.RIDGE,bg='LightSkyBlue')
inteligence=tk.Label(status,text='inteligence',width=50,height=20,font=FNT,relief=tk.RIDGE,bg='LightSkyBlue')
dexterity=tk.Label(status,text='dexterity',width=50,height=20,font=FNT,relief=tk.RIDGE,bg='LightSkyBlue')

strength_num=tk.Label(status,text='100',width=100,height=20,font=FNT,relief=tk.RIDGE,bg='LightSkyBlue')
inteligence_num=tk.Label(status,text='100',width=100,height=20,font=FNT,relief=tk.RIDGE,bg='LightSkyBlue')
dexterity_num=tk.Label(status,text='25',width=100,height=20,font=FNT,relief=tk.RIDGE,bg='LightSkyBlue')

health.place(x=100,y=420,height=20)
mana.place(x=100,y=420,height=20)
stamina.place(x=100,y=420,height=20)

health_num.place(x=100,y=440,height=20)
mana_num.place(x=100,y=440,height=20)
stamina_num.place(x=100,y=440,height=20)
"""
health_num.grid(row=1,column=0,columnspan=3,padx=2,pady=2,sticky=tk.W)
mana_num.grid(row=1,column=1,columnspan=3,padx=2,pady=2,sticky=tk.W)
stamina_num.grid(row=1,column=2,columnspan=3,padx=2,pady=2,sticky=tk.W)

strength.grid(row=2,column=0,columnspan=3,padx=2,pady=2,sticky=tk.W)
inteligence.grid(row=2,column=1,columnspan=3,padx=2,pady=2,sticky=tk.W)
dexterity.grid(row=2,column=2,columnspan=3,padx=2,pady=2,sticky=tk.W)

strength_num.grid(row=3,column=0,columnspan=3,padx=2,pady=2,sticky=tk.W)
inteligence_num.grid(row=3,column=1,columnspan=3,padx=2,pady=2,sticky=tk.W)
dexterity_num.grid(row=3,column=2,columnspan=3,padx=2,pady=2,sticky=tk.W)
"""
root.mainloop()

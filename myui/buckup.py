import tkinter as tk

root=tk.Tk()
root.title('UI Test')
root.geometry('800x600')
root['bg']='#333'

#基本のフレームを5種配置
main=tk.Canvas(root,width=600,height=400,bd=0,highlightthickness=0)
main.grid(row=0,column=0,sticky=tk.NW)
canvas=tk.Canvas(root,width=200,height=200,bd=0,highlightthickness=0)
canvas.grid(row=0,column=1,sticky=tk.NE)
player=tk.Frame(root,width=200,height=200,bd=3,relief='raised',bg='#555')
player.grid(row=0,column=1,sticky=tk.SE)
inventry=tk.Frame(root,width=200,height=200,bd=3,relief='raised',bg='tan')
inventry.grid(row=1,column=1,sticky=tk.SE)
status=tk.Frame(root,width=600,height=200,bd=3,relief='raised',bg='#4682b4')
status.grid(row=1,column=0,sticky=tk.SW)

mainphoto=tk.PhotoImage(file='back.png')
main.create_image(300,200,image=mainphoto)
#キャラクター情報を載せる
photo1=tk.PhotoImage(file='yoroi.png')
canvas.create_image(100,100,image=photo1)
#ステータスのラベルを作り、placeで配置
player_name=tk.Label(player,text='さむらい:Lv8',width=18,height=2,font=('HackGen35',16),fg='white',bg='#555')
player_name.place(x=4,y=2)
player_health=tk.Label(player,text='たいりょく:255',width=18,height=2,font=('HackGen35',16),fg='white',bg='#555')
player_health.place(x=4,y=35)
player_weapon=tk.Label(player,text='ぶき:きくいちもんじ',width=18,height=2,font=('HackGen35',16),fg='white',bg='#555')
player_weapon.place(x=4,y=70)
player_armor=tk.Label(player,text='ぼうぐ:おおよろい',width=18,height=2,font=('HackGen35',16),fg='white',bg='#555')
player_armor.place(x=4,y=105)
player_condition=tk.Label(player,text='じょうたい:けんこう',width=18,height=2,font=('HackGen35',16),fg='white',bg='#555')
player_condition.place(x=4,y=140)



root.mainloop()

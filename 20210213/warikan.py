import tkinter as tk

def click_btn():
	amount=int(total_price.get())
	people=int(member.get())
	dnum=amount/people
	pay=dnum//100*100
	if dnum>pay:
		pay=int(pay+100)
	
	payorg=amount-pay*(people-1)
	print('***支払額***')
	print(f'1人当たり{pay}円({people}人),幹事は{payorg}円です')

FNT=("Times New Roman",16)
root=tk.Tk()
root.geometry('300x600')
root.title('割り勘くん')
root['bg']='LightSkyBlue'
label=tk.Label(root,text='金額',bg='LightSkyBlue')
label.grid(row=0,column=0,columnspan=1,padx=5,sticky=tk.W)

total_price=tk.Entry(root,width=30,font=FNT)
total_price.grid(row=1,column=0,columnspan=1,padx=5,sticky=tk.W)

label2=tk.Label(root,text='人数',bg='LightSkyBlue')
label2.grid(row=2,column=0,columnspan=1,padx=5,sticky=tk.W)

member=tk.Entry(root,width=30,font=FNT)
member.grid(row=3,column=0,columnspan=1,padx=5,sticky=tk.W)

button=tk.Button(root,text='計算する',font=FNT,command=click_btn)
button.grid(row=4,column=0,columnspan=1,pady=30,padx=5,sticky=tk.W)

root.mainloop()

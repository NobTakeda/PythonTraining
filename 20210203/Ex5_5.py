def int_input(msg):
	return int(input(msg+'を入力してください'))

def calc_payment(amount,people=2):
	dnum=amount/people
	pay=dnum// 100*100

	if dnum>pay:
		pay=int(pay+100)

	payorg=amount-pay*(people-1)
	return pay,payorg	

def show_payment(pay,payorg,people=2):
	print('***支払額***')
	print(f'1人当たり{pay}円({people}人)、幹事は{payorg}円です')
	

amount=int_input('支払総額')
people=int_input('参加人数')

pay,payorg=calc_payment(amount,people)
show_payment(pay,payorg,people)





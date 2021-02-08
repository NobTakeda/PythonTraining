import random
import time
def make_tickets(playNum):
	ticket_list=[make_number() for i in range(playNum)]
	#print(ticket_list)
	return ticket_list

def make_number():
	nums=[str(random.randrange(10)) for _ in range(4)]
	#print(nums)
	ticket=''.join(nums)
	#print(ticket)
	return ticket	

def check_winning(ticket_list,winning_number):
	#チケットリストから1枚ずつ取り出して抽選番号と確認

#ここからメイン処理
playNum=int(input('宝くじを何枚買いますか?>>'))
lottery_tickets=make_tickets(playNum)
#lotteryTickets=[random.randrange(9999) for _ in range(playNum)]
print(lottery_tickets)
win_num=make_number()
print('抽選開始…')
for i in range(len(win_num)):
	time.sleep(1)
	print(win_num[i])
print(f'当選番号は{win_num}です！')

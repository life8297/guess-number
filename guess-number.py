# 產生一個隨機整數1~100(不要印出來)
# 讓使用者重複數字去猜
# 猜對的話印出"終於猜對了"
# 猜錯的話要告訴他比答案大/小
import random
r = random.randint(1, 100)
while True:
	guess_num = input('請猜數字(1~100):')
	guess_num = int(guess_num)
	if guess_num == r:
		print('終於猜對了!! 答案為', r)
		break
	elif guess_num > r and guess_num > 0 and guess_num < 100:
		print('比答案大', '答案',  '~', guess_num, '請繼續猜')
	elif guess_num < r and guess_num > 0 and guess_num < 100:
		print('比答案大', guess_num, '~', '答案', '請繼續猜')
	else:
		print('超出範圍, 請輸入範圍1~100')
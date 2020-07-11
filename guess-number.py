# 產生一個隨機整數1~100(不要印出來)
# 讓使用者重複數字去猜
# 猜對的話印出"終於猜對了"
# 猜錯的話要告訴他比答案大/小
import random
print('歡迎來到猜數字遊戲')
start = input('請輸入最小值:')
end = input('請輸入最大值:')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	guess_num = input('請開始猜數字:')
	guess_num = int(guess_num)
	count += 1 # 同於count = count + 1之快寫法
	if guess_num == r:
		print('猜對了!! 答案為', r, ', 總共猜了', count, '次!')
		break
	elif guess_num > r and guess_num > start and guess_num < end:
		print('比答案大', '答案',  '~', guess_num, '請繼續猜')
	elif guess_num < r and guess_num > start and guess_num < end:
		print('比答案大', guess_num, '~', '答案', '請繼續猜')
	else:
		print('超出範圍, 請輸入範圍', start, '~', end)
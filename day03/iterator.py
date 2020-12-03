
import time
# def get_score():
# 	s = input('请输入学生成绩（0～100）：')
# 	n = int(s)
# 	if 0 <= n <= 100:
# 		return n
# 	else:
# 		return 0

# score = get_score();
# print('最终输入的成绩', score)
# try:
# 	score = get_score()
# except:
# 	score = 0
# else:
# 	print('出现异常啦')
# finally:
# 	print('最终输入的成绩', score)



# 闹钟程序，启动时设置定时时间（小时和分钟），到时间后打印“时间到”然后退出程序
# def alerm():
# 	h = int(input('请输入小时：'))
# 	m = int(input('请输入分钟：'))
# 	while True:
# 		curtime = time.localtime() #获取当前时间的元组
# 		if (h, m) == curtime[3:5]:
# 			print('\n时间到...')
# 			return
# 		print('\r%02d:%02d:%02d' % curtime[3:6], end='')
# 		time.sleep(1)

# alerm()

import random
def get_new_poker():
	kinds = ['\u2660', '\u2663', '\u2665', '\u2666']

	numbers = ['A']
	numbers += [str(x) for x in range(2,11)]
	numbers += ['J', 'Q', 'K']

	L = [k + n for k in kinds for n in numbers]
	L += ['大王', '小王']
	return L

def play():
	poker = get_new_poker()	
	random.shuffle(poker)
	input('按任意键发第一个人的牌：')
	print('第一个人的牌是：', poker[:17])
	input('按任意键发第二个人的牌：')
	print('第二个人的牌是：', poker[17:34])
	input('按任意键发第三个人的牌：')
	print('第三个人的牌是：', poker[34:51])
	input('按任意键看底牌：')
	print('底牌是：', poker[51:])

# play()	




s = {'工商银行', '建设银行', '中国银行', '农业银行'}
for item in s:
	print (item)

it = iter(s)
while True:
		try:
			item1 = next(it)
			print(item1)
		except StopIteration:
			break



def my_integer(n):
	i = 1
	while i < n:
		yield i
		i += 1

for x in my_integer(5):
	print(x)	


names = ['中国移动', '中国联通', '中国电信'];
for k, n in enumerate(names, 1):
	print('序号：', k, '------>', n)

it = iter(enumerate(names, 1))	
while True:
	try:
		k, n = next(it)
		print('序号：', k, '------>', n)
	except StopIteration:
		break



# L = [];
# while True:
# 	value = input('请输入：')
# 	if len(value) == 0:
# 		print(L)
# 		get_print(L)
# 		break
# 	else:
# 		L += value

# print(L)
# def get_print(L):
# 	for value, n in enumerate(L, 1):
# 		print('第', n, '行：', value)


# def input_text():
# 	L = []
# 	while True:
# 		s = input('请输入：')
# 		if not s:
# 			break
# 		L.append(s)
# 	return L


# def output_text(L):
# 	for t in enumerate(L, 1):
# 		print('第%d行：%s' % t)

# def output_text(L):
# 	for t in enumerate(L, 1):
# 		print('第%d行：%s' % t)

# def main():
# 	texts = input_text()
# 	print(texts)
# 	output_text(texts)

# main()


bytearray(4)

for i in range(1,10):
	for j in range(1, i+1):
		print('%dx%d=%d' % (j, i, j * i), end = ' ')

	print()		
	























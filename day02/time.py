import time

# print(time.altZone) 

# def show_time():
# 	while True:
# 		t = time.localtime() #绑定时间元组
# 		s = '\r %02d:%02d:%02d' % (t[3], t[4], t[5])
# 		# s = '\r %02d:%02d:%02d' % t[3:6]
# 		print(s, end='')
# 		time.sleep(1)

# show_time()		
# 
# 输入生日。计算出生那天是周几。已经出生了多少天

y = int(input("输出年："))
m = int(input("输出月："))
d = int(input("输出日："))
t = time.mktime((y, m, d, 0, 0, 0, 0, 0, 0))
print('UTC的秒数:', t)
time_tuple = time.localtime(t)
week = time_tuple[6]
L = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日',]
print('这一天是：', L[week])

t = time.time() - t #从生日到现在过了多少秒
d = t / (60 * 60 * 24)
print('您一出生', d, '天')
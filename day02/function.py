#! /usr/bin/python3

fx = lambda n: (n ** 2 + 1) % 5 == 0

print(fx(4))
print(fx(3))


# mymax = lambda a, b: max(a, b) #方法一
mymax = lambda a, b: a if a > b else b #方法二
print(mymax(55, 63))



# g = {}
# l = {}
# while True:
# 	s = input("请输入语句 $ >>>")
# 	if s == "bye":
# 		break
# 	exec(s, g, l)	

# print(g)
# print(l)



# 函数式编程
n = 100
print(sum(range(n + 1)))


# 求：1 + 1/2 + 1/4 + 1/8 + ... + 1/2**n
n = 100
print(sum([1/2**x for x in range(n+1)]))



# 求 1**2 + 2**2 + 3**2 + ... 9**2的和
# def f2(x):
# 	print(sum(map(lambda x: x ** 2, range(1, 10))))
# 	return x ** 2
# s = sum(map(f2, range(1, 10)))
# print(s)
print(sum(map(lambda x: x ** 2, range(1, 10))))
# 求 1**9 + 2**8 + 3**7 + ... 9**1的和
print(sum(map(pow, range(1, 10), range(9, 0, -1))))





# isodd函数判断是否是奇数，是奇数返回True
def  isodd(x):
	return x % 2 == 1 
# 打印10以内的奇数
# 
for x in filter(isodd, range(10)):
		print(x)	

# 打印10以内的偶数
L = [x for x in filter(lambda x: x % 2 == 0, range(10))]
print(L)

# 求：100 + 99 + 98 + 97 + ... + 1的和
def mysum(x):
	if x == 1:
		return 1
	return x + mysum(x - 1)	
print(mysum(100))

# 写入一个函数 input_number放入列表L中
# L = []
# def input_number():
# 	lst = []
# 	while True:
# 		i = int(input("请输入数字（-1结束）："))
# 		if i == -1:
# 			break
# 		# L.append(i)
# 		lst.append(i)
# 		global L
# 		L = lst
# input_number()
# print("您刚才输入的整数值是：", L)		


def priv_check(fn):
	def fx(name, x):
		fn(name, x)
		print("正在验证权限...")
	return fx

def message_send(fn):
		def fy(name, x):
				# 先办理其他业务
				fn(name, x)	
				print("短信", name, "发生了", x, "元的操作，余额XXX")
		return fy				


# 存钱对应的函数
@priv_check
def save_money(name, x):
	print(name, "存钱", x, "元")

# 取钱对应的函数
@message_send
@priv_check
def withdraw(name, x):
	print(name, "正在办理取钱", x, "元的业务")

save_money("Tom", 200)
save_money("Honey", 20)
withdraw("Jarry", 3000)	


import math
# r = float(input("请输入圆半径："))
# s = math.pi * r ** 2
# print("圆的面积是：", s)


# Sn = 1 * 1/1! + 1/2! + 1/3! + 1/4! + ... + 1/n!

def fun(n):
	# return sum([x / math.factorial(x) for x in range(1,n)])#方法一
	return sum(map(lambda i: 1 / math.factorial(i), range(n + 1)))#方法二
	# s = 0#方法三 
	# for i in range(n + 1):
	# 	s += 1 / math.factorial(i)
	print(s)	
print(fun(20)) 	
# 
# 
# s = 1 + x + x**2/2! + x**3/3! + x**n/n!
def fun(x, n):
	s = sum(map(lambda i: x**i / math.factorial(i), range(n + 1)))
	return s
print(fun(3.1, 10))


















			

	
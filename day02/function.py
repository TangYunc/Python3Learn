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
	
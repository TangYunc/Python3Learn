#! /usr/bin/python3

print("hello world!")
print("this is my first python lanague!")
print("开始学习python")
print("#######")
print("#     #")
print("#######")
print("c=", (6+4)*2, "s=", 6*4)
r = 3
c = 2 * 3.14 * r
s = 3.14 * r ** 2
print(c, s)
r = 10
print(c, s)

a, b = 10, 20
print(a, b)
c = a
a = b
b = c
print(a, b)

pi = 3.14
i = int(pi)
f = pi - i
print(i)
print(f)
print(f is 0.14)
del pi, i, f

g = 2
p = 4
# a - a / g + a / p = 10 / 2
# print(a)

# s = input("请输入一个正整数")
# n = int(s)

# if n % 2 == 1:
# 	print("是奇数")
# elif n % 2 == 0:
# 	print("是偶数")
# print("这是最后一行")





# x = input("请输入月份：")
# y = x

# if y >= 1 && y <4:
# 	print(y + "是春季")
# elif y >= 4 && y < 7:
# 	print(y + "是夏季")
# elif y >= 7 && y < 10:
# 	print(y + "是秋季")
# else:
# 	print(y + "是冬季")

# x = input("请输入月份：")
# y = int(x)
# print(y)

# if y == 1:
# 	print("是春季有1，2，3月份")
# elif y == 2:
# 	print(y, "是夏季有4，5，6月份")
# elif y == 3:
# 	print(y, "是秋季有7，8，9月份")
# elif y == 4:
# 	print(y, "是冬季有10，11，12月份")
# else: 
	# print("您的输入有误")


# value = int(input("请输入一个数："))
# if value >= 0:
# 	print("您输入的是：", value)
# else:
# 	print("你输入的是：", - value)
# value = int(input("请输入一个数："))

# print("您输入的是：", value if value > 0 else (- value))


# n = int(input("请输入矩形宽度："))
# w = "#" 
# h = w
# w1 = w * n
# h1 = h + " " * (n - 2) + h
# print(w1)
# print(h1)
# print(h1)
# print(w1)


a = "扫黄打非健身房看看地方"
print(a[0], a[-1])
if len(a) % 2 == 0:
	print("|")
else:
	print(a[(len(a)//2)])
	print(a[int(len(a)/2)])



print(a[1:3])


b = "上海自来水来自海上"
b1 = b[::-1]
if b == b1:
	print(b, "是回文")
else:
	print(b, "不是回文")


c = "发哈技术发挥空间啊手机费"
if len(c) != 0:
	print(ord(c[0]))
else:
	print(c, "为空")


# d = int(input("请输入一个整数值："))
# d1 = ord(str(d)[0])
# print(d1)



# e = input("请输入第一行内容：")
# e1 = input("请输入第二行内容：")
# e11 = input("请输入第三行内容：")
# print("%10s" % e)
# print("%10s" % e1)
# print("%10s" % e11)


# ml = max(len(e), len(e1), len(e11))
# #方法一
# print(" " * (ml - len(e)) + e)
# print(" " * (ml - len(e1)) + e1)
# print(" " * (ml - len(e11)) + e11)

# # 方法二
# # fml = "%" + str(ml) + "s"
# fml = "%%%ds" % ml
# print(fml % e)
# print(fml % e1)
# print(fml % e11)







# f = int(input("请输入一个整数:"))
# i = 2
# while i < f:
# 	print(i)
# 	i += 2

# i = 0
# while i < 10:
# 	print(i)
# 	i += 0.5

# j = 1
# while j <= 20:
# 	print(j, end=" ")
# 	j += 1






# i = 1
# while i <= 20:
# 	print(i, end=" ")
# 	if i % 5 == 0:
# 		print('\n')
# 	i += 1



# i = 10
# while i >= 1:
# 	print(i)
# 	i -= 1


# h = int(input("请输入三角形宽度："))
# i = 1 
# while i <= h:
# 	print("*" * i)
# 	i += 1



# n = int(input("请输入一个整数:"))
# i = 0
# while i < n:
# 	j = 1
# 	while j <= n:
# 		print(j, end=" ")
# 		j += 1
# 	print()
# 	i += 1




s = "AB C D E  F   FD"	

i = 0
for x in s:
	print("----->", x)
	if x == " ":
		i+=1
else:
	print("for循环因迭代结束而终止")	

# j = 0
# count = 0
# while j < len(s):
# 	y = s[j]
# 	print("----->", x)
# 	if y == " ":
# 		count+= 1
# 	j+=1		
# print(count)


# value1 = int(input("请输入开始值："))
# value2 = int(input("请输入结束值："))
# result = range(value1, value2)
# j = 0
# count = 0
# for x in result:
# 	print(x, end=" ")
# 	count+=1
# 	if count % 5 == 0:
# 		print()
# 	j+=1


# i = value1
# count = 0
# while i < value2:
# 		print(i, end=" ")
# 		count+=1
# 		if count % 5 ==0:
# 			print()
# 		i+=1
# else:
# 	print()		
# 	
# for x in range(value1,value2):
# 		print(x , end= "")
# 		if (x + 1 - value1) % 5 == 0:
# 			print()


# i = 10
# for x in range(1,i):
# 	print(x)
# 	i-=2

# value1 = int(input("请输入："))
# for x in range(1,value1):
# 	print(x, end=" ")
# 	if (x + 1 - value1) % 5 == 0:
# 		print()


az = "" #用于累加字符
#方法一
# i = ord("A") #65 # 0x41
# end = ord("Z") #ord("A") + 26 - 1
# while i<= end:
# 	az += chr(i)
# 	i += 1
# else:
# 	print(az)

#方法二
for i in range(ord("A"), ord("Z") + 1):
	az += chr(i)
else:
	print(az)			



az = ""
#方法一
# i = ord("A")
# while i <=  end:
# 	az += chr(i) #加一个大写字母
# 	# az += chr(i + (ord("a") - ord("A")))
# 	az += chr(i + 0x20)
# 	i += 1
# else:
# 	print(az)

#方法二
for i in range(ord("A"), ord("Z") + 26):
	az += chr(i) + chr(i + 0x20)
else:
	print(az)	



# n = int(input("请输入一个数："))	
# for i in range(1, n + 1):
# 	for j in range(i, i + n):
# 		print(j, end = "")
# 	else:
# 		print()		


# content = input("请输入文本内容：")
# list1 = []
# for i in content:
# 	print("ssss%sss" % i)
# 	if i == " ":
# 		break 

# print("循环结束")		
# 


# L = []
# while True:
# 	n = int(input("请输入一个数："))	
# 	if n < 0:
# 		break
# 	L.append(n)
# print(L)	
# result1 = sum(L) #求和
# print(result1)
# L2 = L.copy()
# L2.sort(reverse = True)
# print(L2[0], L2[1]) #输出最大和第二大的数
# result2 = min(L)
# print(result2)
# result3 = L.remove(result2) #删除最小的数
# print(result3)
# for i in L: #按原来的顺序打印剩余的数
# 	print(i)




# s = "hello, hi"
# s1 = s.split(",")
# print(s1)
# print(" ".join(s))
# # s2 = s.split("-")
# print("-".join(s))


# [1,4,9,16,25,...81]
# 方法一
# L = []
# for x in range(1,10):
# 	L.append(x ** 2)
# #方法二 用列表推到式生成
# L = [x ** 2 for x in range(1,10)]


#用列表推导式生成1～100内奇数的列表
# L = [x for x in range(1,100, 2)] #方法一
# L = [x for x in range(1,100) if (x % 2 == 1)] #方法二
# print(L)

# # 生成【1，9，25，49，81】列表，跳过所有的偶数
# L = [x ** 2 for x in range(1,10) if x % 2 == 1]
# print(L)


# [A1,A2,A3,B1,B2,B3,C1,C2,C3]
# L = [x + y for x in "ABC" for y in "123"]
# print(L)




# n = int(input("请输入一个数："))	

 #打印树冠
 #方法一
# for i in range(1,n + 1):
#  	starts = "*" * (2 * i - 1) #星号个数
#  	blanks = " " * (n - i) #计算空格个数
#  	print(blanks + starts)
# for _ in range(n):
# 	print(" " * (n - 1) + "*")

#方法二
# for i in range(1,n + 1):
#  	starts = "*" * (2 * i - 1) #星号个数
#  	print(starts.center(2 * n - 1))
# for _ in range(n):
# 	print(" " * (n - 1) + "*")	



#打印输入的数是否是素数（质数） 素数：2，3，5，7，11，13，17，19...
# n = int(input("请输入一个数："))	
# if n < 2:
# 	print(n, "不是素数")
# else:
# 	for i in range(2, n):
# 		if n % i == 0:
# 			print(n, "不是素数")
# 			break
# 	else: #循环结束，不能再获取数据时
# 		print(n, "是素数")		
# type(n)




L = [3.1, 3.2]
t = (1,2,L)
print(t)
L[0] = 3.14
print(t)
# t[0] = 1.2#元组不能改变不可变数据
# print(t)





# d = {"0": "周日", "1": "周一", "2": "周二", "3": "周三", "4": "周四", "5": "周五", "6": "周六", "日": "周日", "一": "周一", "二": "周二", "三": "周三", "四": "周四", "五": "周五", "六": "周六"}
# while True:
# 	s = input("请输入星期的内容：")
# 	if not s:#当用户输入空字符串时结束输入
# 		break
# 	if s in d:#判断s是否是d的键
# 		print("你输入的是：", d[s])
# 	else:
# 		print("你输入不正确，请重新输入～")	




# L = ["abc", "defoo", "g"]
# value = [3, 5, 1]		
# d = {x: len(x) for x in L}
# print(d)


# no = [1001, 1002, 1003, 1004]
# names = ["Tom", "Jerry", "Speck", "Tyke"]
# d = {no[x]: names[x] for x in range(len(no))}
# print(d)



s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {1, 2}
print(s1 & s2)#交集
print(s1 | s2)#并集
print(s1 - s2, s2 - s1)#补集
print(s1 ^ s2)#两个集合的对称补集
print(s1 > s3)#超集
print(s3 < s1)#子集













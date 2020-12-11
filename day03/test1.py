# 1.用生成器函数生成斐波那契数列的前n个数：
# 		1 1 2 3 5 8 13 ...

# 		def fibonacci(n):
# 			...
# 			yield ..
# 			1)输出前20个数
# 			2）求前30个数的和

# 方法一
def fibonacci1(n):
	count = 0 #记录当前已生成的数的个数
	#判断当前已生成的个数大于等于需要的个数时，直接返回
	if count >= n: 
		returen
	yield 1 #生成1
	count += 1 #已生成的个数+1

	if count >= n: #再次判断已生成的数的个数
		returen #生成一个1
	yield 1
	count += 1 #已生成个数+1

	# 用列表生成第三个起的书
	L = [1, 1]
	# 如果一生成的个数小于需要的个数，则继续生成
	while count < n:
		# 从第三个起
		L.append(L[-1] + L[-2]) #生下一个数
		yield L[-1] #返回刚生成的数
		count += 1 #已生成的个数+1

# for x in fibonacci1(20):
# 	print(x)
# 方法二
def fibonacci2(n):
	count = 0 #记录当前已生成的数的个数
	#判断当前已生成的个数大于等于需要的个数时，直接返回
	if count >= n: 
		returen
	yield 1 #生成1
	count += 1 #已生成的个数+1

	if count >= n: #再次判断已生成的数的个数
		returen #生成一个1
	yield 1
	count += 1 #已生成个数+1

	# 用列表生成第三个起的书
	a = 1 #a代表倒数第二个数
	b = 1 #b代表倒数第一个数
	# 如果一生成的个数小于需要的个数，则继续生成
	while count < n:
		# 从第三个起
		a, b = b, a + b
		yield b #返回刚生成的数
		count += 1 #已生成的个数+1
for x in fibonacci2(20):
	print(x)


print(sum(fibonacci2(30)))	





# 2.写程序打印杨辉三角（只打印6层）
# 			1
# 		   1 1
# 		  1	2 1
# 	     1 3 3 1
# 	    1 4 6 4 1
# 	   1 5 1010 5 1   

def get_next_line(lst):
	# 先放入1
	next_line = [1] #先把最左的数放入
	# 计算中间的依赖上一层的那写数
	for i in range(len(lst) - 1):
		next_line.append(lst[i] + lst[i + 1])
	# 在最后放一个1
	next_line.append(1)
	return next_line


def get_yanghui_list(n):
	L = [1]
	yhlist = [] # 创建一个空列表
	for _ in range(n): # 控制n次循环
		yhlist.append(L) # 把当前L存储的一行放入列表
		L = get_next_line(L) #用当前行来计算出下一行
	return yhlist

L = get_yanghui_list(6)
for x in L:
	print(x)

		

class Human:
 	"""docstring for ClassName"""
 	def __init__(self, n, a ,addr='未填写'):
 		super(Human, self).__init__()
 		self.name = n
 		self.age = a
 		self.address = addr
 	
 	def show_info(self):
 		print(self.name, self.age, '岁', '家住', self.address)
 	
 	def update_age(self):
 		self.age += 1
			


def input_human():
	humans = []
	while True:
		n = input('请输入姓名：')
		if not n:
			break
		a = int(input('请输入年龄：'))
		addr = input('请输入家庭住址：')
		man = Human(n, a ,addr) 
		humans.append(man)
		
	return humans

def main():
	docs = input_human()
	for h in docs:
		h.show_info()
	for h in docs:
		h.update_age()
	for h in docs:
		h.show_info()	
		 	
main()		 			 	
		    	   



















			
			
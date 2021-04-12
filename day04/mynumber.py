#此程序示意运算符重载
# class MyNumber():
# 	"""docstring for MyNumber"""
# 	def __init__(self, v):
# 		self.data = v

# 	def __repr__(self):
# 		return "MyNumber(%d)" % self.data

# 	def __add__(self, other):
# 		print("__add__方法被调用")
# 		obj = MyNumber(self.data + other.data)
# 		return obj

# 	def __sub__(self, other):
# 		print("__add__方法被调用")
# 		obj = MyNumber(self.data - other.data)
# 		return obj

# n1 = MyNumber(100)		
# n2 = MyNumber(200)
# #n3 = n1.__add__(n2)
# n3 = n1 + n2
# print(n3)

# n4 = n2.__sub__(n1)
# #n4 = n2 - n1
# print('n4 = ', n4)



#实现两个自定义表的相加
class MyList():
	"""docstring for MyList"""
	#运算符重载
	def __init__(self, iterable):
		self.data = [x for x in iterable]
	
	def __repr__(self):
		return "MyList(%r)" % self.data
	def __add__(self, rhs):
		print("__add__方法被调用")
		obj = MyList(self.data + rhs.data)
		return obj
	def __mul__(self, rhs):
		print("__mul__方法被调用")
		obj = MyList(self.data * rhs)
		return obj
	#反向 运算符重载
	def __rmul__(self, lhs):
		print("__rmul__方法被调用, lhs=", lhs)
		obj = MyList(self.data * lhs)
		return obj


	#复合运算符重载
	def __iadd__(self, rhs):
		print("__iadd__方法被调用")
		self.data.extend(rhs.data)
		return self

	#getitem,setitem重载
	def __getitem__(self, i):
		print("__getitem__方法被调用")
		return self.data[i]
	def __setitem__(self, i, v):
		print("__setitem__方法被调用")
		self.data[i] = v

L1 = MyList([1,2,3])
L2 = MyList(range(4,7))
L3 = L1 + L2
print('L3 = ' , L3) # MyList([1,2,3,4,5,6])
L4 = L1 * 2 #实现乘法运算
print('L4 = ', L4) # MyList([1,2,3,1,2,3])
L5 = 2 * L1
print(L5)
L6 = MyList([1,3,5])
print("id(L6) = ", id(L6))
L6 += L2
print("L6 = ", L6)
print("id(L6) = ", id(L6))











			
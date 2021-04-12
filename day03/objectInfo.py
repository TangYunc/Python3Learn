
class Student:
	"""docstring for Student"""
	# 限定此类创建的对象只能有name和age两个属性
	__slots__ = ['name', 'age']
	def __init__(self, n, a):
		super(Student, self).__init__()
		self.name = n
		self.age = a

s1 = Student('肖打', 20)		
# s1.Age = 21
# print(s1.__dict__)




# 类方法classmethod
class A:
	"""docstring for A"""
	v = 0 #类变量
	@classmethod
	def get_v(cls):
		return cls.v

	@classmethod #（一次只能针对一个函数）
	def set_v(cls, value):
		cls.v = value
	
print(A.get_v)
A.v = 1
print(A.get_v)
A.set_v(100)
print(A.get_v)



# 静态方法@staticmethod
class A:
	@staticmethod
	def myadd(a, b):
		return a + b

print(A.myadd(100, 200))
a = A()
print(a.myadd(300, 400))		



# 对象转字符串函数重写
class MyNumber:
	"""docstring for MyNumber """
	def __init__(self, value):
	 	self.data = value
	
	def __str__(self):
		return '数字：%d' % self.data

n1 = MyNumber(100)		
print(str(n1))
print(n1)
print(repr(n1)) #调用n1.__repr__()方法



class MyNumber1:

	def __init__(self, v):
		self.data = v
	
	def __repr__(self):
		return 'MyNumber1(%d)' % self.data

	def __int__(self):
		return int(self.data)

n2 = MyNumber1(100)
print('n1 = ', n1)
print(int(n2))				











































































		
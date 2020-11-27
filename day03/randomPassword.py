# 假设可以作为密码的字符有：
# A-Z
# a-z
# 0-9
# 写一个程序，随机生成六位密码8在_A63

import random as r 

def get_random_passwd(n):
	''' 生成n位的随机密码'''
	source = getSourceFromAZaz09('A', 26) + getSourceFromAZaz09('a', 26) + getSourceFromAZaz09('0', 10) + '_'
	# print(source)
	s = ''
	for _ in range(n):
		s += r.choice(source)
		# print(s)
	return s


def getSourceFromAZaz09(value, step):
	return ''.join([chr(x) for x in range(ord(value), ord(value) + step)])

# print(getSourceFromAZaz09('0', 10))
print('现在生产6位的随机密码是：', get_random_passwd(6))

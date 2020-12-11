def read_data():
	f = open('fileOperation.txt')
	L = []
	while True:
		s = f.readline()
		if not s:
			f.close() #关闭文件
			return L
		s = s.rstrip() #去掉s尾部的换行符
		index = s.find('  ')
		name = s[:index] #用切片获取名字
		number = s[index + 1:]
		L.append((name, number))
		# print('姓名：', name, 'number：', number)

		print(s)			

lst = read_data()			
print(lst)

def print_phone_book(L):
	for name, number in L:
		print('姓名：', name, '电话：', number)

print_phone_book(read_data())	




try:

	f = open('mydata.txt', 'w')
	print('打开文件成功')
	f.write('我是第一行\n')
	f.write('我是第二行\n')
	f.writelines(['我是第三行', '我是第四行\n', '我是第五行'])
	f.close()
except IOError:
	print('打开文件失败')




def read_input():
	L = []
	while True:
		s = input('请输入：')
		if not s:
			break
		L.append(s)
		return L

def write_input(L):
	try:
		f = open('input.txt', 'w')
		for line in L:
			f.write(line)
			f.write('\n')

		f.close()
	except IOError:
		print('写文件失败')
	


def main():
	lst = read_input()
	print(lst)
	write_input(lst)

main()	


def read_input_file(filename='input.txt'):
	f = open(filename)
	L = []
	while True:
		s = f.readline()
		if not s:
			break
		s = s.rstrip()
		L.append(s)
	f.close()
	return L	


def print_file_info(L):
	for line in enumerate(L, 1):
		print('第%d行：%s' % line)

def main1():
	lst = read_input_file()
	print(lst)
	print_file_info(lst)

main1()	


















































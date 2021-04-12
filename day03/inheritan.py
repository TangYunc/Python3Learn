#练习：
#实现文件的复制（建议使用二进制方式进行操作）
# python3 mycp.py
# 	请输入源文件：/etc/passwd
# 	请输入目标文件：./mypass.txt
# 	提示：‘文件复制成功’或‘文件复制失败’
# 	建议使用with语句打开文件

def mycp(src_file, dst_file):
	'''
	src_file源文件名
	dst_file目标文件名
	'''

	fr = open(src_file, 'rb')	
	fw = open(dst_file, 'wb')
	b = fr.read()
	fw.write(b)
	return true
def main():
	src = input('请输入源文件名：')
	dst = input('请输入源目标文件名：')
	if mycp(src, dst):
		print('复制文件成功')
	else:
		print('复制文件失败')


main()
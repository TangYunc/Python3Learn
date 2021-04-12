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
	try:
		with open(src_file, 'rb') as fr:
			with open(dst_file, 'wb') as fw:
				#如果文件太大则分次进行搬移
				while True:
					b = fr.read(4096) #如果此文件大怎么办
					if not b: #如果字节串为空，停止复制
						break
					fw.write(b)
	except:
		return False
	
	return True
def main():
	src = input('请输入源文件名：')
	dst = input('请输入源目标文件名：')
	if mycp(src, dst):
		print('复制文件成功')
	else:
		print('复制文件失败')


main()
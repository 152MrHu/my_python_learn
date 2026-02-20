

# 打开文件open(name,mode,encoding)  name:文件名  mode:打开模式
# 1. 打开文件  f是一个特殊类型
f = open("C:/Users/24553/Desktop/新建 文本文档.txt", "r",encoding="utf-8") # r: 只读模式  w: 写入模式  a: 追加模式  b: 二进制模式

print(type(f))

# 2. 读取文件内容
content = f.read(5)  # 读取三个字符
print(type(content),content)
print()

# content = f.read() # 读取文件内容  read()方法会把文件内容全部
# print(type(content),content)
# print()
#
# content = f.read()
# print(type(content),content) # 读取文件内容  read()方法会把文件内容全部读取完毕，第二次调用read()方法时，文件指针已经指向文件末尾，所以返回空字符串
# print()

# readline()方法会读取文件的一行内容，返回一个字符串
line1 = f.readline() # 读取文件的一行内容
print(type(line1),line1)

# readlines() 方法会读取文件的所有行内容，返回一个列表，每一行内容作为列表的一个元素
lines = f.readlines() # 读取文件的所有行内容
print(type(lines),lines)
for line in lines:
    print(line) # 打印每一行内容

for line in lines:
    print(line.strip()) # strip()方法会去掉字符串两端的空白字符，包括换行符

# 3. 关闭文件
f.close() # 关闭文件  释放资源
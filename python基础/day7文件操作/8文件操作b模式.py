
fr = open("C:/Users/24553/Desktop/新建 文本文档.txt", "rb")
fw = open("C:/Users/24553/Desktop/新建 文本文档.txt", "wb")
# 以二进制模式打开文件，读取文件内容时会返回一个bytes类型的对象
# 只有文件可以rwa
# 其他类型用b打开，读取文件内容时会返回一个bytes类型的对象
content = fr.read()
print(type(content),content)
fr.close()
fw.close()

f = open("C:/Users/24553/Desktop/新建 文本文档.txt", "w",encoding="utf-8")
# w 模式会覆盖原有文件内容，如果文件不存在会创建一个新文件
f.write("helasd asdasdwlo    world") # write()方法会把字符串写入缓冲区，返回写入的字符数
# f.flush() # flush()方法会把缓冲区的内容写入文件，保证数据的完整性
f.flush()

while True:
    pass
f.close()  # 之前会自动flush
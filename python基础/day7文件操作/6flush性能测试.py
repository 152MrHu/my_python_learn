import time

s = time.time()
f = open("C:/Users/24553/Desktop/新建 文本文档.txt", "w",encoding="utf-8")
for i in range(100000):
     f.write(str(i)+"\n")
     f.flush() # flush()方法会把缓冲区的内容立即写入文件，保证数据的及时性
end = time.time()
print(f"写入100000行数据的时间：{end-s}秒")


s = time.time()
f = open("C:/Users/24553/Desktop/新建 文本文档.txt", "w",encoding="utf-8")
for i in range(100000):
     f.write(str(i)+"\n")
f.flush() # flush()方法会把缓冲区的内容立即写入文件，保证数据的及时性
end = time.time()
print(f"写入100000行数据的时间：{end-s}秒")
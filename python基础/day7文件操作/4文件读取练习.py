
f = open("C:/Users/24553/Desktop/新建 文本文档.txt", "r",encoding="utf-8")
content = f.read()
print(content.count("学生"))

f.close()


f = open("C:/Users/24553/Desktop/新建 文本文档.txt", "r",encoding="utf-8")
num = 0
for line in f:

        num+=1
print(f"学生出现了{num}次")

f.close()
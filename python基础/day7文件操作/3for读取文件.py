

f = open("C:/Users/24553/Desktop/新建 文本文档.txt", "r",encoding="utf-8")
for line in f:
    print(line.strip())
    print(type(line))
f.close()

for line in open("C:/Users/24553/Desktop/新建 文本文档.txt", "r",encoding="utf-8"):
    print(line.strip())
    # 循环结束后会自动关闭文件

with open("C:/Users/24553/Desktop/新建 文本文档.txt", "r",encoding="utf-8") as f:
    for line in f:
        print(line.strip())
    # 循环结束后会自动关闭文件

#PYTHON中任何with xxx as xxx 语句都可以做到不要close。

fr = open("C:/Users/24553/Desktop/新建 文本文档.txt", "r",encoding="utf-8")
fw = open("C:/Users/24553/Desktop/新建 文本文档2.txt", "w",encoding="utf-8")
for line in fr:
    fw.write(line.strip()+"\n") # strip()方法会去掉字符串两端的空白字符，包括换行符

fr.close()
fw.close()
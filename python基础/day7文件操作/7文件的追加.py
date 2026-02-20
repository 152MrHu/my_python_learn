f = open("C:/Users/24553/Desktop/新建 文本文档.txt", "a",encoding="utf-8")
# a: 追加模式  w: 写入模式  a: 追加模式  b: 二进制模式
# 追加模式会在文件末尾添加内容，而不会覆盖原有内容

f.write("这是追加的内容\n") # write()方法会把字符串写入文件中 不自动换行
f.flush()

f.close()
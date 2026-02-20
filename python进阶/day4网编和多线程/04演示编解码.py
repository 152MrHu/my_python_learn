"""
案例：

细节：
    1，编码 = 把我们看得懂的 转成  我们看不懂的
          "字符串".encode(码表)
    2，解码 = 把我们看不懂的 转成  我们看得懂的
            二进制.decode(码表)
    3，乱码原因是编解码不同
    4，英文字母，数字，特殊符号无论什么编码都只占一个字节
            中文在gbk中战2字节，utf-8中3个字节
    5，二进制写法，即：b" 数字字母，特殊符号 "  该方式不能有中文
"""

s1 = "黑马123"
print(s1.encode())   #
print(s1.encode("utf-8"))  #
print(s1.encode("gbk"))
print("----"*15)

# 解码
bys = b'\xe9\xbb\x91\xe9\xa9\xac123a@!'
print(type(bys))
s2 = bys.decode()
s3 = bys.decode("utf-8")
print(s2)
print(s3)
s4 = bys.decode("gbk")
print(s4)
print("----"*15)

def mylen(s):
    length = 0
    for i in s:
        length += 1
    return length

name = "itheima"
print(f"{name}长度是{len(name)}")

length = 0
for i in name:
    length += 1
print(f"{name}长度是{length}")

s = "itheima"
print(f"{s}长度是{mylen(s)}")
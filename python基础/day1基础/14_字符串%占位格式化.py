name = "周杰伦"
age = 11
height = 172.55
# 传统拼接
message = "我是" + name + ",今年"+str(age)+"岁,身高:"+str(height)+"(cm)"
print(message)
# %占位符 自动转为字符串
message2 = "我是%s,今年%s岁,身高:%s(cm)" % (name,age,height)
print(message2)

message3 = "我是%s,今年%s岁,身高:%d(cm)" % (name,age,height)
print(message3)

message4 = "我是%s,今年%d岁,身高:%f(cm)" % (name,age,height)
print(message4)

message5 = "我是%s,今年%d岁,身高:%.2f(cm)" % (name,age,height) # 四舍五入到小数点后2位
# %b  %o  %d   %h 对应 2 8 10 16 进制整数
print(message5)
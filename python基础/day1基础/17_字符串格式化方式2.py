name = "周杰伦"
age = 11
height = 172.55
# 全部变量都转为字符串
message = f"我是{name},今年{age}岁,身高{height}厘米"
print(message)
# 格式控制
message = f"我是{name},今年{age:10.1f}岁,身高{height:3.21}厘米"
print(message)
# self是对象本身
class Car:
    # 属性
    brand = "奔驰"
    color = "黑色"
    # 方法
    def run(self):
        print(f"汽车在跑,{self}")


c1 = Car()
c2 = Car()
print(c1)
print(c2)
c1.run()
c2.run()
#self = c1或者c2是一个对象
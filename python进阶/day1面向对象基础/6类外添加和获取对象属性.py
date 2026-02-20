class A:
    pass


class Car:
    # 属性  类内添加属性  所有对象都有
    brand = "奔驰"
    color = "黑色"
    # 方法
    def run(self):
        print(f"汽车在跑,")


c1 = Car()  #c1指向堆中的一个对象
c2 = Car()
# 对象类外添加属性只给该对象加
c1.shape = "圆的";

print(c1.brand, c1.color, c1.shape )  # 通过对象访问属性
print(c2.brand, c2.color,)  # 通过对象访问属性

c1.run()
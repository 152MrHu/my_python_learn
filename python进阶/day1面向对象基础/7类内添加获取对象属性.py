class Car:
    # 属性  类内添加属性  所有对象都有
    brand = "奔驰"
    color = "黑色"
    # 方法
    def run(self):
        print(f"汽车在跑,")
    def prt(self):
        print(f"我的brand属性值为: {self.brand}")
        print(f"我的color属性值为: {self.color}")
    def show(self):
        print(f"我的brand属性值为: {self.brand}")
        print(f"我的color属性值为: {self.color}")
        print(f"我的shape属性值为: {self.shape}")

c1 = Car()
c1.color="白色"
c1.prt()  # 通过对象访问属性

c2 = Car()
c2.shape = "圆的"
c2.prt()  # 通过对象访问属性
c2.show()  # 通过类访问属性
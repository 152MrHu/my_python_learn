class Car:
    # 属性
    brand = "奔驰"
    color = "黑色"
    # 方法
    def run(self):
        print(f"{self}汽车在跑,")
    def work(self  ):
        self.run()
        print(f"我是work，我的self值为: {self}")


c1 = Car()
c1.work()
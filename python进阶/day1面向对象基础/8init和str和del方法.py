class Car:
    def __init__(self, brand, color):
        """

        :param brand:  车的品牌
        :param color:   车的颜色
        """
        print("这是init方法,创建对象自动调用")
        self.brand = brand
        self.color = color
    def show(self):
        print(f"我的brand属性值为: {self.brand}")
        print(f"我的color属性值为: {self.color}")

c1 = Car([1,2,3,4,5,6], "黑色")
c1.show()



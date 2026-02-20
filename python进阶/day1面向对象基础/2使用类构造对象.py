class Car:
    # 属性
    brand = "奔驰"
    color = "黑色"
    # 方法
    def run(self):
        print("汽车在跑")

# 创建对象
car1 = Car()
print(car1.brand)  # 通过对象访问属性
car1.run()  # 通过对象访问方法
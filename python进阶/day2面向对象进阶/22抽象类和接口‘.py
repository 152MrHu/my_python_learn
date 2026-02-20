"""
有抽象方法的类叫抽象类（接口），子类必须重写父类的抽象方法，否则子类也会变成抽象类。
抽象方法：在父类中定义一个方法，但不实现它的功能，子类必须重写这个方法来实现它的功能。
    def abstract_method(self):
        pass
父类确定了方法有哪些
子类来具体实现这些方法
"""

class AC:
    def cool_wind(self):
        pass
    def hot_wind(self):
        pass
    def swing_wind(self):
        pass
class Haier(AC):
    def cool_wind(self):
        print("海尔空调的冷风")
    def hot_wind(self):
        print("海尔空调的热风")
    def swing_wind(self):
        print("海尔空调的摇头风")

class Gree(AC):
    def cool_wind(self):
        print("格力空调的冷风")
    def hot_wind(self):
        print("格力空调的热风")
    def swing_wind(self):
        print("格力空调的摇头风")


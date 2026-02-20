



"""
类方法: 可以通过类名调用, 也可以通过实例对象调用
           定义时必须用@classmethod , 但是第一个参数必须是cls, cls代表当前类对象
静态方法: 可以通过类名调用, 也可以通过实例对象调用
           定义时必须用@staticmethod , 但是没有默认参数,
           也就是说静态方法不需要传递任何默认参数, 也不能访问类属性和实例属性
"""

class Student:
    country = '中国'  # 类属性
    @classmethod
    def show(cls):
        print(f"我是类方法，cls: {cls}")
        print(f"我是{cls.country}的学生")  # 访问类属性

    @staticmethod
    def show2():
        print("我是静态方法")


if __name__ == '__main__':
    Student.show()  # 通过类名调用类方法
    Student.show2()  # 通过类名调用静态方法
    s = Student()
    s.show()  # 通过实例对象调用类方法
    s.show2()  # 通过实例对象调用静态方法
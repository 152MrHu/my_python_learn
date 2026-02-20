"""

"""
import json

from sympy.polys.subresultants_qq_zz import sturm_q

# 你是通义灵码吗
from student import Student
class StudentCMS (object):
    def __init__(self):
        self.stu_list = []

    def show_view(self):
        print("*"*34)
        print("欢迎使用学生管理系统")
        print("\t1. 添加学生信息")
        print("\t2. 删除学生信息")
        print("\t3. 修改学生信息")
        print("\t4. 查询单个学生信息")
        print("\t5. 查询所有学生信息")
        print("\t6. 保存学生信息")
        print("\t0. 退出系统")
        print("*"*34)
    # 添加学生信息
    def add_student(self):
        name = input("请输入学生姓名：")
        gender = input("请输入学生性别：")
        age = input("请输入学生年龄：")
        phone = input("请输入学生联系电话：")
        desc = input("请输入学生描述信息：")
        student = Student(name, gender, age, phone, desc)
        self.stu_list.append(student)
        print(f"添加学生{name}信息成功！")
    # 删除学生信息
    def delete_student(self):
        del_name  = input("请输入要删除的学生姓名：")
        for i in self.stu_list:
            if i.name == del_name :
                self.stu_list.remove(i)
                print(f"删除学生{del_name}信息成功！")
                break
        else:
            print("没有此学生！")
    # 修改学生信息
    def modify_student(self):
        upd_name = input("请输入要删除的学生姓名：")
        for i in self.stu_list:
            if i.name == upd_name:
                i.age = input("请输入修改后年龄：")
                i.gender = input("请输入修改后性别：")
                i.phone = input("请输入修改后手机号：")
                i.desc = input("请输入修改后描述：")

                print(f"修改学生{upd_name}信息成功！")
                break
        else:
            print("没有此学生！")
    # 查询单个学生信息
    def query_student(self):
        name = input("请输入要查询的学生姓名：")
        for i in self.stu_list:
            if i.name == name:
                print(f"查询学生{name}信息成功！")
                print(i)
                print("查询成功")
                break
        else:
            print("没有此学生！")
    # 查询所有学生信息
    def query_all_students(self):
         if  len(self.stu_list) <= 0:
             print("没有学生信息")
         else:
            for student in self.stu_list:
                 print(student)
         print()
    # 保存学生信息
    def save_students(self):
        with open("./studatadata.txt", "a") as f :
            # 把列表中的学生对象转换成字典
            stu_dic = [student.__dict__ for student in self.stu_list]
            # 把字
            f.write(str(stu_dic))
            print("保存成功")
    def load_students(self):
        # 加载学生信息

        with open("./studatadata.txt", "r") as f:
            stu_data = f.read()
            stu_lista = eval(stu_data)
            if len(stu_lista) == 0:
                stu_lista = []
            self.stu_list = [Student(**stu) for stu in stu_lista]
            print("加载成功")

    def run(self):
        self.load_students()
        while True:
            self.show_view()
            choice = input("请输入你的选择：")
            if choice == "1":
                self.add_student()
            elif choice == "2":
                print("删除学生信息")
                self.delete_student()
            elif choice == "3":
                print("修改学生信息")
                self.modify_student()
            elif choice == "4":
                print("查询学生信息")
                self.query_student()
            elif choice == "5":
                print("查询所有学生信息")
                self.query_all_students()
            elif choice == "6":
                print("保存所有学生信息")
                self.save_students()
            elif choice == "0":
                # 二次确认
                confirm = input("你确定要退出系统吗？Y/N")
                if confirm.lower() == "y":
                    self.save_students()
                    print("欢迎下次再来")
                    break
            else:
                print("输入错误，请重新输入")
if __name__ == '__main__':
    cms = StudentCMS()
    cms.show_view()
    cms.run()
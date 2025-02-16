"""
演示类的构造方法
"""
# 演示使用构造方法对成员变量进行赋值
# 构造方法的名称：__init__
class Student:
    name=None
    age=None
    tel=None

    def __init__(self,name,age,tel):
        self.name=name
        self.age=age
        self.tel=tel
        print("Student类创建了一个类对象")

stu=Student("djas",31,"1992839")
print(stu.name)
print(stu.age)
print(stu.tel)

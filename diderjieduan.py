# 1，设计一个类（类比生活中：设计一张登记表）
class Student:
    name=None
    gender=None
    nationality=None
    native_place=None
    age=None

# 2，创建一个对象（类比生后中：打印一张登记表）
stu_1 = Student()
# 3，对象属性进行赋值（类比生活中：填写表格）
stu_1.name="某某某"
stu_1.gender="男"
stu_1.nationality="中国"
stu_1.native_place="安徽省"
stu_1.age=18
# 4. 获取对象中记录的信息
print(f"姓名：{stu_1.name}\n性别：{stu_1.gender}\n国籍：{stu_1.nationality}\n籍贯：{stu_1.native_place}\n年龄：{ stu_1.age}")
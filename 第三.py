"""
演示设计模式之工厂模式
"""
class Person:
    pass
class Worker(Person):
    pass

class Student(Person):
    pass

class Teacher(Person):
    pass

class PersonFactory:
    def create(self,p_type):
        if p_type == 'w':
            return Worker()
        elif p_type == 's':
            return Student()
        else:
            return Teacher()

pf=PersonFactory()
work=pf.get_person('w')
stu=pf.get_person('s')
techer=pf.get_person('t')



"""
演示变量的类型注释
"""
from random import random

# 基础数据类型注释
var_1:int=18
var_2:str="dfjalkd"
var_3:bool=True

# 类对象类型的注释
class Student:
    pass
stu:Student=Student()

#基础容器类型注释
my_list:list=[1,2,3]
my_tuple:tuple=(1,2,3)
my_dict:dict={1:"a",2:"b"}
#容器类型详细注解
my_list:list[int]=[1,2,3]
my_touple:tuple[int,str,bool]=(1,"sdkjf",True)
my_dict:dict[str,int]={1:"a",2:"b"}
#在注释中进行类型注释
var_1=random.randint(1,10) # type:int
#var_2=json.loads('{"name":"djf"}') # type: dict[str,str]
def func():
    return 10
var_3=func() # type:int
# 类型注解只是个备注不会影响代码运行





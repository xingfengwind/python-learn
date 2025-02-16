"""
演示对函数（方法）进行注解
"""
# 对形参进行类型注解
def add(x:int,y:int):
    return x+y
add(1,2)
# 对返回值进行类型注释
def func(data:list)->list:
    return data
print(func(add(1,2)))

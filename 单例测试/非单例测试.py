"""
演示非单例测试
"""
class StrTools:
    pass

s1=StrTools()
s2=StrTools()
print(id(s1))
print(id(s2))
# 定义元组
t1=(1,"Hello",True)
t2=()
t3=tuple()
print(f"t1的类型是:{type(t1)},内容是:{t1}")
print(f"t2的类型是:{type(t2)},内容是:{t2}")
print(f"t3的类型是:{type(t3)},内容是:{t3}")
# 定义单个元素的元素
t4=("hello", )
print(f"t4的类型是:{type(t4)},内容是:{t4}")
# 元组的嵌套
t5=((1,2,3),(4,5,6))
print(f"t4的类型是:{type(t5)},内容是:{t5}")
# 下标索引去取出内容
num=t5[1][2]
print(f"从嵌套元组中取出的数据是：{num}")
# 元组的操作：index查找方法
t6=(1,2,3,4,5,6)
index=t6.index(1)
print(f"在元组6中查找1，的下标：{index}")
# 元组的操作：count统计方法
t7=(1,2,1,4,1,1)
num=t7.count(1)
print(f"在元组t7中统计1的数量有：{num}个")
# 元组的操作：len函数统计元组元素的数量
t8=(1,2,3,4,5,6)
num=len(t8)
print(f"t8元组中的元素有：{num}个")
# 元组的遍历：while
index=0
while index<len(t8):
    print(f"元组的元素有：{t8[index]}")
    index+=1
# 元组的遍历：for
for element in t8:
    print(f"2元组的元素有:{element}")
# 修改元组内容
# 元组的内容不可修改，但嵌套的列表可以修改

t9=(1,2,[3,4])
print(f"t9的内容是:{t9}")
t9[2][0]=5
t9[2][1]=6
print(f"t9的内容是:{t9}")

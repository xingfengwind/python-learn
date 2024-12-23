mylist=["cyuyan","java","python"]
# 1.1 查找某元素
index=mylist.index("cyuyan")
print(f"cyuyan在列表中的下标索引值是：{index}")
# 1.2如果被查找的元素不存在，会报错
# index=mylist.index("hello")
#  print(f"hello在列表中的下标索引值是：{index}“)
# 2. 修改特定下标索引的值
mylist[0]="c++"
print(f"列表被修改值后，结果是：{mylist}")
# 3.在指定下标位置插入新元素
mylist.insert(1,"go")
print(f"列表插入元素后，结果是：{mylist}")
# 4。在列表的尾部追加```单个```新元素
mylist.append("c#")
print(f"追加元素后，结果是：{mylist}")
# 5.在列表尾部追加```一批```新元素
mylist2=[1,2,3]
mylist.extend(mylist2)
print(f"列表再追加一批新元素的列表后，结果是：{mylist}")
# 6.删除指定下标索引的元素(两种方式)
mylist=["a","b","c"]
# 6.1 方式一：del 列表[下标]
del mylist[2]
print(f"列表删除元素后结果是：{mylist}")
# 6.2方式2：列表。pop(下标)
mylist=["a","b","c"]
element=mylist.pop(2)
print(f"通过pop方法取出元素后列表内容：{mylist}，取出元素：{element}")
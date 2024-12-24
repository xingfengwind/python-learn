#7. 删除某元素在列表中的第一个选项
mylist=["a","b","c","d","e"]
mylist.remove("a")
print(f"通过remove方法移除元素后，列表的结果：{mylist}")
# 清出列表
mylist.clear()
print(f"列表被清空了，结果是：{mylist}")
# 9.统计列表内的某元素的数量
mylist=["a","a","a","d","e"]
count=mylist.count("a")
print(f"列表中a的数量:{count}")
# 10.统计列表中的全部的元素数量
mylist=["a","b","c","d","e"]
count=len(mylist)
print(f"列表的元素总数量总共有：{count}个")
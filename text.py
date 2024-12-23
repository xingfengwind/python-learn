 # 定义一个链表List
my_list=["fr","wl","wx"]
print(my_list)
print(type(my_list))

my_list=["ndh",666,True]
print(my_list)
print(type(my_list))

# 定义一个嵌套列表
my_list=[[1,2,3],[4,5,6]]
print(my_list)
print(type(my_list))
# 通过下标索引取出对应位置的数据
my_list=["Tom","Lily","Rose"]
# 列表[下标索引]，从前向后从0开始，每次+1，从后向前从-1开始，每次-1
print(my_list[0])
print(my_list[1])
print(my_list[2])

# 列表[下标索引]，通过下标索引取数据，一定不要超出范围
#print(my_list[3])
# 通过下标索引取出数据(倒序取出)
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])

# 取出嵌套列表的元素
my_list=[[1,2,3],[4,5,6]]
print(my_list[1][1])


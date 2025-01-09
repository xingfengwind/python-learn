my_str="hhvghghejhgjgjh"
# 通过下标索引取值
value=my_str[2]
value2=my_str[-6]
print(f"从字符串{my_str}取下标为2的元素，值是：{value},去下标为-16的元素，值是：{value2}")
# index方法：
value =my_str.index("e")
print(f"在字符串{my_str}中查找额，其起始下标是:{value}")
# replace方法
new_my_str=my_str.replace("e","2")
print(f"将字符串{my_str}进行split切分后得到:{new_my_str}")

# split方法
my_str="ddg"
my_str_list=my_str.split(" ")
print(f"将字符串{my_str}进行split切分后得到:{my_str_list},类型是:{type(my_str_list)}")

# strip方法
my_str=" ddd "
new_my_str=my_str.strip()# 不传入参数，去除首尾空格
print(f"字符串{my_str}被strip后，结果：:{new_my_str}")

my_str="12ddd21"
new_my_st=my_str.strip("12")
print(f"字符串{my_str}被strip('12')后，结果：:{new_my_str}")

#  统计字符串中某个字符的出现次数，count
my_str="sjdjkednfkedj"
count=my_str.count("j")
print(count)
# 统计字符串的长度，len()
num=len(my_str)
print(num)
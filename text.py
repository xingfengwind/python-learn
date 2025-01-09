#strip方法
my_str = " ddd "
new_my_str = my_str.strip()  # 不传入参数，去除首尾空格
print(f"字符串{my_str}被strip后，结果：:{new_my_str}")
my_str = "12ddd21"
new_my_st = my_str.strip("12")
print(f"字符串{my_str}被strip('12')后，结果：:{new_my_str}")
#  统计字符串中某个字符的出现次数，count
my_str = "sjdjkednfkedj"
count = my_str.count("j")
print(count)
# 统计字符串的长度，len()
num = len(my_str)
print(num)
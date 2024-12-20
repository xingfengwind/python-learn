def say_hi():
    print("你好啊")

result = say_hi()
print(f"无返回值函数，返回内容是：{result}")
print(f"无法返回值函数，返回内容类型是：{type(result)}")

# 主动返回None的函数
def say_hi2():
    print("你好啊")
    return None

result = say_hi2()
print(f"无返回值函数，返回内容是：{result}")
print(f"无法返回值函数，返回内容类型是：{type(result)}")

# None用于if判断
def chack_age(age):
    if age >= 18:
        return "SUCCESS"
    else:
        return None

result = chack_age(16)
if not result:
    print("未成年，不可以进入 ")

# None用于声明无初始内容的变量
name=None
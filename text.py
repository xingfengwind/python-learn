# 在函数内修改全局变量
# num=200
# def test_a():
#     print(f"test_a:{num}")
# def test_b():
#     num=500# 局部变量
#     print(f"test_b:{num}")
#
# test_a()
# test_b()
# print(num)

# global关键字，在函数内声明为全局变量
num=200
def test_a():
    print(f"test_a:{num}")
def test_b():
    global num
    num=500# 局部变量
    print(f"test_b:{num}")

test_a()
test_b()
print(num)
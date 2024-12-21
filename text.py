 # 定义函数func_b
def func_b():
    print("---2---")
# 定义函数func_a,并在内部调用func_b
def func_a():
    print("---1---")
    func_b()

    print("---3---")

#调用函数func_a
func_a()


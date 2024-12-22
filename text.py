# 演示局部变量
#def test_a():
#    num = 100
#   print(num)

#test_a()
#出了函数体，局部变量就无法使用了
#print(num)# 无法输出

#演示全局变量
num=200
def test_a():
    print(f"test_a:{num}")
def test_b():
    print(f"test_b:{num}")
test_a()
test_b()
print(num)


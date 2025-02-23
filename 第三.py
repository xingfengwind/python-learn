"""
演示python的闭包性
"""

# 简单闭包
# def outer(logo):
#
#     def inner(msg):
#         print(f"<{logo}><{msg}><{logo}>")
#     return inner
#
#
# fn1 =outer("afjlaks")
# fn1("jfdkl")
#
# fn2=outer("oei")
# fn2=("jdfkda")

# 使用nonlocal关键字修改外部函数的值
def outer(num1):

    def inner(num2):
        nonlocal num1
        num1+=num2
        print(num1)

    return inner

fn=outer(10)
fn(20)
fn(30)
fn(40)
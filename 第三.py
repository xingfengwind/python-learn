"""
演示装饰器的写法
"""
# 装饰器的一般写法
def outer(func):
    def inner():
        print("睡")
        func()
        print("起")
    return inner
def sleep():
    import random
    import time
    print("睡眠中·····")
    time.sleep(random.randint(1, 5))


fn=outer(sleep)
fn()
# 装饰器的快捷写法
@outer
def sleep2():
    import random
    import time
    print("睡眠中····")
    time.sleep(random.randint(1, 5))

sleep()
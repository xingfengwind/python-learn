"""
演示类与对象的关系:及面向对象的编程套路
"""

# 设计一个闹钟类
class Clock:
    id=None
    price=None

    def ring(self):
        import winsound
        winsound.Beep(2000,3000)

# 构造2个闹钟对象并让其工作
clock1=Clock()

clock1.id="003032"
clock1.price=19.99
print(f"闹钟id:{clock1.id},价格price:{clock1.price}")
clock1.ring()

clock2=Clock()
clock2.id="003034"
clock2.price=20.00
print(f"闹钟id:{clock2.id},价格price:{clock2.price}")
clock2.ring()

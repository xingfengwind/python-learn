"""
演示面向对象：继承的基础语法
"""
# 演示单继承
class Phone:
    IMEI=None
    pooducer="dkfal"
    def call_by_4g(self):
       print("4g通话")

class Phone2022(Phone):
    face_id="10293"

    def call_by_5g(self):
        print("2022新功能：5g通话")

phone=Phone2022()
print(phone.pooducer)
phone.call_by_4g()
phone.call_by_5g()

# 演示多继承
class NFCReader:
    nfc_type="第五代"
    producer="dkf"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")
class RemoteControl:
    rc_type="红外遥控"

    def control(self):
        print("红外遥控开启了")
class MyPhone(Phone, NFCReader, RemoteControl):
    pass

phone=MyPhone()
phone.call_by_4g()
phone.read_card()
phone.write_card()
phone.control()
# 演示多继承下，父类成员名一致情况
print(phone.pooducer)# 显示优先继承的

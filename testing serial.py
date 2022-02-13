import serial.tools.list_ports
import serial

import time
comlist = serial.tools.list_ports.comports()
com_num = ''
for i in comlist:
    com_num = str(i)[3:4]

def initserial(com):
    console = serial.Serial(
        port=f'COM{str(com)}',
        baudrate=9600,
        parity="N",
        stopbits=1,
        bytesize=8,
        timeout=8
    )
    return console

main = initserial(com_num)

main.write(b'\n')
main.write(b'\n')
main.write(b'\n')
main.write(b'\n')
test = main.readlines(100)
main.write(chr(3).encode('utf-8'))
print('will push config')
class Ciscoconfig:
    def __init__(self,monitor_num,device_name):
        self.mon_num = monitor_num
        self.device_name = device_name

    def checkmode(self,main):
        pass
    

    def initconfigdev(self,main,passw):
        command = [
            b'enable \n',
            b'configure terminal \n',
            b'Hostname ' +self.device_name.encode('utf-8')+str(self.mon_num).encode('utf-8')+b'\n',
            b'enable secret '+passw.encode('utf-8') + b'\n',
            b'service password-encryption \n',
            b'no logging console \n',
            b'no ip domain-lookup \n',
            b'line console 0  \n',
            b'password ' +passw.encode('utf-8') +b'\n',
            b'login \n',
            b'exec-timeout 0 0 \n',
            b'line vty 0 14 \n',
            b'password ' + passw.encode('utf-8') + b'\n',
            b'login \n'
            b'exec-timeout 0 0 \n'
        ]

        for i in command:
            main.write(i)

        print('Initialized!')
test1 = Ciscoconfig('11','leafswitch')
test1.initconfigdev(main,'pass')
print(main.readlines(100))
main.close()

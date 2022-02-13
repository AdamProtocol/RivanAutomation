import serial.tools.list_ports
import serial

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
print(test)

main.close()

import serial.tools.list_ports
import serial

comlist = serial.tools.list_ports.comports()

def get_COM(command):
    get_com = subprocess.Popen(command,universal_newlines=True,shell=True,
                               stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    get_com = get_com.stdout.read()
    get_com = get_com.split()
    com_num = ''
    for i in get_com:
        if 'COM' in i:
            com_num = i[3:4]
    return com_num

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
start1 = initserial((str(i.device)[-1] for i in comlist))
print('GUMANA')

class Ciscoconfig:
    def __init__(self,monitor_num,device_name):
        self.monitor_num = monitor_num

    def checkmode(self,main)


    def initconfigdev(self,main,passw):
        command = [
            b'enable /n',
            b'configure terminal /n',
            b'Hostname ' +device_name.encode('utf-8')+str(self.mon_num).encode('utf-8')+b'/n',
            b'enable secret '+passw.encode('utf-8') + b'/n',
            b'service password-encryption /n',
            b'no logging console /n',
            b'no ip domain-lookup /n',
            b'line console 0  /n',
            b'password ' +passw.encode('utf-8') +b'/n',
            b'login /n',
            b'exec-timeout 0 0 /n',
            b'line vty 0 14 /n',
            b'password ' + passw.encode('utf-8') + b'/n',
            b'login /n'
            b'exec-timeout 0 0 /n'
        ]

        for i in command:
            main.write(i)

        print('Initialized!')
        
class Switch(Ciscoconfig):

    def __init__(self,monitor_num):
        super().__init__(monitor_num)

    def PORTS(self,main):


        command = [
            b'int gi0/1 /n',
            b'no shutdown /n',
            b'no switchport /n',
            (f'ip add 10.{self.mon_num}.{self.mon_num}.4 255.255.255.0').encode('utf-8')+b'/n',
            b'int vlan 1 /n',
            b'no shutdown /n',
            (f'ip add 10.{self.mon_num}.1.4 255.255.255.0').encode('utf-8') + b'/n',
            b'description MGMTVLAN',
            b'int vlan 10 /n',
            b'no shutdown /n',
            (f'ip add 10.{self.mon_num}.10.4 255.255.255.0').encode('utf-8') + b'/n',
            b'description WIRELESSVLAN',
            b'int vlan 100 /n',
            b'no shutdown /n',
            (f'ip add 10.{self.mon_num}.100.4 255.255.255.0').encode('utf-8') + b'/n',
            b'description VOICEVLAN'
        ]

        for i in command:
            main.write(i)

    def DHCP(self,main):
        command = [
            b'config terminal /n',
            (f'ip dhcp excluded-address 10.{self.mon_num}.1.1 10.{self.mon_num}.1.100').encode('utf-8') + b'/n',
            (f'ip dhcp excluded-address 10.{self.mon_num}.10.1 10.{self.mon_num}.10.100').encode('utf-8') + b'/n',
            (f'ip dhcp excluded-address 10.{self.mon_num}.100.1 10.{self.mon_num}.100.100').encode('utf-8') + b'/n',
            b'ip dhcp pool MGMTVLAN /n',
            (f'network 10.{self.mon_num}.1.0 255.255.255.0').encode('utf-8')+b'/n',
            b'default-router 10.'+self.mon_num.encode('utf-8')+b'1.4 /n',
            b'domain-name mgmt.com /n',
            b'dns-server 10.'+self.mon_num.encode('utf-8')+b'.1.10 /n',
            b'ip dhcp pool WIRELESSDATA /n',
            (f'network 10.{self.mon_num}.10.0 255.255.255.0').encode('utf-8') + b'/n',
            b'default-router 10.' + self.mon_num.encode('utf-8') + b'1.4 /n',
            b'domain-name wireless.com /n',
            b'dns-server 10.' + self.mon_num.encode('utf-8') + b'.1.10 /n',
            b'ip dhcp pool VOICEVLAN /n',
            (f'network 10.{self.mon_num}.100.0 255.255.255.0').encode('utf-8') + b'/n',
            b'default-router 10.' + self.mon_num.encode('utf-8') + b'1.4 /n',
            b'domain-name voice.com /n',
            b'dns-server 10.' + self.mon_num.encode('utf-8') + b'.1.10 /n',
            b'option 150 ip 10.'+self.mon_num.encode('utf-8')+b'.100.8 /n',
        ]
        
        for i in command:
            main.write(i)
        
    def VLAN(self,main):
        command = [
            b'vlan 10 /n',
            b'name WirelessDATA /n',
            b'vlan 100 /n',
            b'name VoiceVLAN /n',
            b'interface fastethernet 0/2 /n',
            b'switchport mode access /n',
            b'switchport access vlan 10 /n',
            b'interface fastethernet 0/3 /n',
            b'switchport mode access /n',
            b'switchport access vlan 100 /n',
            b'interface fastethernet 0/7 /n',
            b'switchport mode access /n',
            b'switchport access vlan 100 /n',
            b'interface fastethernet 0/5 /n',
            b'switchport mode access /n',
            b'switchport access vlan 100 /n',
            b'ip routing /n',
        ]

        for i in command:
            main.write(i)

class CUCM(Ciscoconfig):

    def __init__(self,monitor_num):
        super().__init__(monitor_num)
        self.cucm_ip = f'10.{str(monitor_num)}.100.8'

    def analog_phone(self,main):
        command = [
            b'configure terminal /n',
            b'dial-peer voice 1 pots /n',
            b'destination-pattern ' +(self.monitor_num).encode('utf-8')+b'00 /n',
            b'port 0/0/0 /n',
            b'dial-peer voice 2 pots /n',
            b'destination-pattern ' +(self.monitor_num).encode('utf-8')+b'01 /n',
            b'port 0/0/1 /n',
            b'dial-peer voice 3 pots /n',
            b'destination-pattern ' +(self.monitor_num).encode('utf-8')+b'02 /n',
            b'port 0/0/2 /n',
            b'dial-peer voice 4 pots /n',
            b'destination-pattern ' +(self.monitor_num).encode('utf-8')+b'03 /n',
            b'port 0/0/3 /n',
            b'end /n'
        ]

        for i in command:
            main.write(i)

    def testcall(self,main,number):
        main.write(b'csim start ' +(number).encode('utf-8')+ b' /n')


    def ipphones(self,main,mac1,mac2):
        command = [
            b'configure terminal /n',
            b'no telephony-service /n',
            b'telephony-service /n',
            b'no auto assign /n',
            b'no auto-reg-ephone /n',
            b'max-ephone 5 /n',
            b'max-dn 20 /n',
            b'ip source-address ' +(self.cucm_ip)+ b' port 2000 /n',
            b'create cnf-files /n'
            b'ephone-dn 1 /n',
            b'number '+(self.monitor_num).encode('utf-8')+b'11 /n',
            b'ephone-dn 2 /n',
            b'number '+(self.monitor_num).encode('utf-8')+b'22 /n',
            b'ephone-dn 3 /n',
            b'number '+(self.monitor_num).encode('utf-8')+b'33 /n',
            b'ephone-dn 4 /n',
            b'number '+(self.monitor_num).encode('utf-8')+b'44 /n',
            b'ephone-dn 5 /n',
            b'number '+(self.monitor_num).encode('utf-8')+b'55 /n',
            b'ephone-dn 6 /n',
            b'number '+(self.monitor_num).encode('utf-8')+b'66 /n',
            b'ephone-dn 7 /n',
            b'number '+(self.monitor_num).encode('utf-8')+b'77 /n',
            b'ephone-dn 8 /n',
            b'number '+(self.monitor_num).encode('utf-8')+b'88 /n',
            b'ephone 1 /n',
            b'mac-address '+(main).encode('utf-8')+ b' /n',
            b'button 1:2 2:3 3:2 4:4 /n',
            b'restart /n',
            b'ephone 2 /n',
            b'mac-address '+(main).encode('utf-8')+ b' /n',
            b'button 1:5 2:6 3:7 4:8 /n',
            b'restart /n',
            b'ephone 1 /n',
            b'video /n',
            b'voice service voip /n',
            b'h323 /n',
            b'call start slow /n',
            b'ephone 2 /n',
            b'video /n',
            b'voice service voip /n',
            b'h323 /n',
            b'call start slow /n',

        ]

        for i in command:
            main.write(i)

    #add the IVR auto

class Router(Ciscoconfig):
    def __init__(self,monitor_num):
        super().__init__(monitor_num)
        self.inside_ip = f'10.{str(monitor_num)}.{str(monitor_num)}.1'
        self.outside_ip = f'200.0.0.{monitor_num}'

    def portconfig(self,main):
        command = [
            b'config terminal /n',
            b'int gi 0/0/1 /n',
            b'description OUTSIDE /n',
            b'ip address '+(self.outside_ip).encode('utf-8')+b' 255.255.255.0 /n',
            b'no shutdown /n',
            b'exit /n'
            b'int gi 0/0/0 /n',
            b'description INSIDE /n',
            b'ip address '+(self.inside_ip).encode('utf-8')+b' 255.255.255.0 /n',
            b'no shutdown /n',
            b'exit /n',
            b'end /n',
            b'configure terminal /n',
            b'interface loopback 0 /n',
            b'ip address '+(self.monitor_num).encode('utf-8')+b'.0.0.1 255.255.255.255 /n'
        ]

        for i in command:
            main.write(i)

    def nat(self,main):
        command = [
            b'conf t /n'
            b'no access-list 8 permit 10.'+self.monitor_num.encode('utf-8')+b'0.0.255.255 /n',
            b'int gi0/0/1 /n',
            b'ip nat inside /n',
            b'ip gi0/0/0 /n',
            b'ip nat outside /n',
            b'ip nat inside source list 8 /n',
            b'end /n'
        ]

        for i in command:
            main.write(i)
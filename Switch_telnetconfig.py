#config for switch , make sure that the json file and python file are in the same directory

import telnetlib
import json

with open('CCNA_DB.json') as f:
    data = json.load(f)
    
print('Starting Automation using Telnetlib')

tn = telnetlib.Telnet(data['sw_vlan1'])

tn.write(b'pass\n')
tn.write(b'enable\n')
tn.write(b'pass\n')

tn.write(b'configure terminal\n')

#this block of code
tn.write(b'interface vlan 10\n')
tn.write(b'no shutdown\n')
vlan_10 = 'ip address ' + data['sw_vlan10'] + ' ' + data['Slash_24']
tn.write(vlan_10.encode('ascii') + b'\n')
tn.write(b'description WIRELESSVLAN\n')
#copy paste this block and change vlan 10 to vlan 100

tn.write(b'interface vlan 100\n')
tn.write(b'no shutdown\n')
vlan_100 = 'ip address ' + data['sw_vlan100'] + ' ' + data['Slash_24']
tn.write(vlan_100.encode('ascii') + b'\n')
tn.write(b'description VOICEVLAN\n')

tn.write(b'end\n')

tn.write(b'configure terminal\n')
tn.write(b'ip dhcp excluded-address ' + data['exclude_v1'].encode('ascii') + b'\n')
tn.write(b'ip dhcp excluded-address ' + data['exclude_v10'].encode('ascii') + b'\n')
tn.write(b'ip dhcp excluded-address ' + data['exclude_v100'].encode('ascii') + b'\n')

tn.write(b'ip dhcp pool MGMTVLAN\n')
vlan_1_network = 'network ' + data['v1_network'] + ' ' + data['Slash_24']
tn.write(vlan_1_network.encode('ascii') + b'\n')
tn.write(b'default-router ' + data['sw_vlan1'].encode('ascii') + b'\n')
tn.write(b'dns-server ' + data['pc_ip'].encode('ascii') + b'\n')
tn.write(b'domain-name mgmt.com\n')

tn.write(b'ip dhcp pool WIRELESSDATA\n')
vlan_10_network = 'network ' + data['v10_network'] + ' ' + data['Slash_24']
tn.write(vlan_1_network.encode('ascii') + b'\n')
tn.write(b'default-router ' + data['sw_vlan10'].encode('ascii') + b'\n')
tn.write(b'dns-server ' + data['pc_ip'].encode('ascii') + b'\n')
tn.write(b'domain-name data.com\n')

tn.write(b'ip dhcp pool VOICEVLAN\n')
vlan_100_network = 'network ' + data['v100_network'] + ' ' + data['Slash_24']
tn.write(vlan_1_network.encode('ascii') + b'\n')
tn.write(b'default-router ' + data['sw_vlan100'].encode('ascii') + b'\n')
tn.write(b'domain-name voice.com\n')
tn.write(b'dns-server ' + data['pc_ip'].encode('ascii') + b'\n')
tn.write(b'option 150 ip ' + data['cucm_fa0/0'].encode('ascii') + b'\n')

tn.write(b'end\n')

tn.write(b'configure terminal\n')
tn.write(b'vlan 10\n')
tn.write(b'name WirelessDATA\n')
tn.write(b'vlan 100\n')
tn.write(b'name VoiceVLAN\n')

tn.write(b'interface fastethernet 0/2\n')
tn.write(b'switchport mode access\n')
tn.write(b'switchport access vlan 10\n')

tn.write(b'exit\n')
tn.write(b'interface range fa0/3 , fa0/7 , fa0/5\n')
tn.write(b'switchport mode access\n')
tn.write(b'switchport access vlan 100\n')

tn.write(b'exit\n')
tn.write(b'ip routing\n')

tn.write(b'end\n')
tn.write(b'exit\n')

de = tn.read_all().decode('ascii')
print('AUTOMATION ENDED SHOWING YOU THE LOGS\n')
print(de)







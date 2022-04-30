#config for router, make sure that the json file and python file are in the same directory

import telnetlib
import json
import time #we need this module so the code can wait N second before executing new lines

with open('CCNA_DB.json') as f:
    data = json.load(f)
    
print('Starting Automation using Telnetlib')

tn = telnetlib.Telnet(data['cucm_fa0/0'])

tn.write(b'pass\n')
tn.write(b'enable\n')
tn.write(b'pass\n')

tn.write(b'configure terminal\n')

tn.write(b'interface gi0/0/1\n')
ip_addr = 'ip address ' + data['int_gi0/0/1'] + data['Slash_24']
tn.write(ip_addr.encode('ascii') + b'\n')
tn.write(b'no shutdown\n')
tn.write(b'exit\n')



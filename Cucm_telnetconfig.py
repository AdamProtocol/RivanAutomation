#config for cucm, make sure that the json file and python file are in the same directory

import telnetlib
import json
import time #we need this module so the code can wait N second before executing new lines

with open('CCNA_DB.json') as f:
    data = json.load(f)
    
monitor_num = 11
    
print('Starting Automation using Telnetlib')

tn = telnetlib.Telnet(data['cucm_fa0/0'])

tn.write(b'pass\n')
tn.write(b'enable\n')
tn.write(b'pass\n')

tn.write(b'configure terminal\n')
tn.write(b'no telephony-service\n')
tn.write(b'telephony-service\n')
tn.write(b'no auto-assign\n')
tn.write(b'no auto-reg-ehone\n')
tn.write(b'max-ephone 5\n')
tn.write(b'max-dn 20\n')
source_add = 'ip source-address ' + data['cucm_fa0/0'] + 'port 2000\n'
tn.write(source_add.encode('ascii'))
tn.write(b'create cnf-files\n')

tn.write(b'ephone-dn 1\n')
tn.write(b'number '+ (monitor_num+'00').encode('ascii') + b'\n')

tn.write(b'ephone-dn 2\n')
tn.write(b'number '+ (monitor_num+'11').encode('ascii') + b'\n')

tn.write(b'ephone-dn 3\n')
tn.write(b'number '+ (monitor_num+'22').encode('ascii') + b'\n')

tn.write(b'ephone-dn 4\n')
tn.write(b'number '+ (monitor_num+'33').encode('ascii') + b'\n')

tn.write(b'ephone-dn 5\n')
tn.write(b'number '+ (monitor_num+'44').encode('ascii') + b'\n')

tn.write(b'ephone-dn 6\n')
tn.write(b'number '+ (monitor_num+'55').encode('ascii') + b'\n')

tn.write(b'ephone-dn 7\n')
tn.write(b'number '+ (monitor_num+'66').encode('ascii') + b'\n')

tn.write(b'ephone-dn 8\n')
tn.write(b'number '+ (monitor_num+'77').encode('ascii') + b'\n')

tn.write(b'ephone 1\n')
tn.write(b'mac-address ' +data['ephone1_mac'].encode('ascii')+ b'\n')
tn.write(b'8945\n')
tn.write(b'button 1:1 2:3 3:2 4:4\n')
tn.write(b'restart\n')

tn.write(b'ephone 2\n')
tn.write(b'mac-address ' +data['ephone1_mac'].encode('ascii')+ b'\n')
tn.write(b'8945\n')
tn.write(b'button 1:5 2:6 3:7 4:8\n')
tn.write(b'restart\n')

tn.write(b'end\n')

tn.write(b'configure terminal\n')
tn.write(b'ephone 1\n')
tn.write(b'video\n')
tn.write(b'h323\n')
tn.write(b'call start slow\n')

tn.write(b'ephone 2\n')
tn.write(b'video\n')
tn.write(b'h323\n')
tn.write(b'call start slow\n')

tn.write(b'end\n')
tn.write(b'exit\n')

de = tn.read_all().decode('ascii')
print('AUTOMATION ENDED SHOWING YOU THE LOGS\n')
print(de)


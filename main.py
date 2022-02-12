print(
'''
WELCOME TO RIVAN AUTOCONFIG TOOL 

CLI METHOD
syntax = <CONNECTION> + <DEVICE> + OPTIONS

example
rivan> SERIAL SWITCHLEAF -INIT -VLANS

DEVICES YOU CAN CONFIGURE

SWITCHSPINE					SWITCHLEAF 					CUCM 				ROUTER
options:					options:					options:			options:
-init						-init						-init				-init
-day1						-day1						-day1				-day1
-vlan						-vlan						-ipPhones			-nat
-dhcp						-dhcp						-IVR				-ports
-ports

to initialize the GUI:
rivan> init_GUI
'''
)
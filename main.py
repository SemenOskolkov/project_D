#!/usr/bin/env python3


london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2"
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
    }
}


device_name = input('Введите имя устройства: ')
parameters = list(london_co[device_name].keys())
list_parameter = (', '.join(parameters))
parameter_name = input(f'Введите имя параметра {list_parameter}: ')
if parameter_name.lower() in london_co[device_name]:
    result = london_co[device_name][parameter_name.lower()]
else:
    result = ('Такого параметра нет')
print(result)

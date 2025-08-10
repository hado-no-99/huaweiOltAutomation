from netmiko import ConnectHandler

huawei_gpon_olt = {
    'device_type' : 'huawei_olt_telnet',
    'ip' : '192.168.209.209',
    'username' : 'optomenoc',
    'password' : 'letmein@123',
    'port' : 23
}

net_connect = ConnectHandler(**huawei_gpon_olt)
net_connect.enable()
output = net_connect.send_command_expect('display ont autofind all')
target_serial = input("Enter the serial: ")
initial_search = e
from netmiko import ConnectHandler
import pyfiglet, termcolor, sys
import ont_add, config_srv_port

def main():
    intro_text = pyfiglet.figlet_format("VOID","slant")
    colored_intro_text = termcolor.colored(intro_text,"green")
    tagline = termcolor.colored("Your Network, Assimilated", "green")
    print(colored_intro_text)
    print(tagline)
    print("\n\n")
    print("Welcome to VOID. Interact with huawei olt easily")

    while True:
        try:
            olt_ip = input("Enter the huawei olt ip: ")
            net_connect = connect_to_olt(olt_ip)
            print(net_connect)
            break
        except Exception:
            print("IP address invalid! Please try again")
        
        

    while True:
        option = input("1. Add an ONU\n2. Exit\nChoose an option number: ")
        if option not in ['1','2']:
            print("Enter a valid option!")
            continue
        match option:
            case '1':
                config_srv_port.config_service_port(net_connect)
            case '2':
                break



def connect_to_olt(ip):
    huawei_gpon_olt = {
        'device_type' : 'huawei_olt_telnet',
        'ip' : ip,
        'username' : 'optomenoc',
        'password' : 'letmein@123',
        'port' : 23
    }
    net_connect = ConnectHandler(**huawei_gpon_olt)
    net_connect.enable()
    net_connect.config_mode()
    return net_connect


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("\nQuiting the application...")
# huawei_gpon_olt = {
#     'device_type' : 'huawei_olt_telnet',
#     'ip' : '192.168.100.24',
#     'username' : 'optomenoc',
#     'password' : 'letmein@123',
#     'port' : 23
# }

# net_connect = ConnectHandler(**huawei_gpon_olt)
# net_connect.enable()
# output = net_connect.send_command_expect('display ont autofind all')
# target_serial = input("Enter the serial: ")
import re
from ont_add import add_ont

def free_service_port(net_connect):
    display_free_index_command = net_connect.send_command("display service-port next-free-index")
    port_pattern = re.search(r"(\d+)",display_free_index_command)
    print(f"The next free port is {port_pattern[0]}")
    return port_pattern[0]

def config_service_port(net_connect):
    data = add_ont(net_connect)
    if data != None:
        service_port = input("Enter a service port(default next free index): ") or free_service_port(net_connect)
        service_port_command = net_connect.send_config_set([f"service-port {service_port} vlan {data['vlan']} gpon {data['board']}/{data['card']}/{data['port']} ont {data['ont_id']} gemport 1 multi-service user-vlan {data['vlan']} tag-transform translate"])
        print(service_port_command)
        show_mac_address = net_connect.send_command(f"display mac-address port {data['board']}/{data['card']}/{data['port']} ont {data['ont_id']}")
        print(show_mac_address)

if __name__ == "__main__":
    config_service_port()
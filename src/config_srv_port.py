import re
from ont_add import add_ont

def free_service_port():
    display_free_index_command = "display service-port next-free-index"
    dummy_output = "The next free service-port index is :  2435\n"
    port_pattern = re.search(r"(\d+)",dummy_output)
    return port_pattern[0]

def config_service_port():
    data = add_ont()
    if data != None:
        service_port = input("Enter a service port(default 0): ") or free_service_port()
        service_port_command = f"service port {service_port} vlan {data['vlan']} gpon {data['board']}/{data['card']}/{data['port']} ont {data['ont_id']} multi-service user-vlan {data['vlan']} tag-transform translate"
        print(service_port_command)

config_service_port()
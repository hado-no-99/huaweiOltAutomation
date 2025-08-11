import re
import sys


def add_ont(net_connect):
    detected_onu = net_connect.send_command('display ont autofind all')
    print(detected_onu)
    # applying error handling for user inputs
    def fetch_input(context):
        is_serial = (context == "Serial Number")
        while True:
            userInput = input(f"Enter the {context}: ") if is_serial else input(f"Enter the {context}(default 0): ")
            if userInput.isnumeric() and not is_serial:
                return userInput
                
            elif userInput == "" and not is_serial:
                return "0"
                
            elif is_serial:
                if userInput.isalnum() and len(userInput) >= 4:
                    return userInput
                else:
                    print("Please enter a valid Serial Number")

            else:
                print(f"Please enter a valid {context}")

    # Populating serial and then checking it in the autofind onts
    serial = fetch_input("Serial Number").upper()
    targetSearch = re.search(fr"F/S/P\s+:\s+(\d)/(\d)/(\d)\s+Ont\s+SN\s+:\s+(\w+{serial})",detected_onu)
    if targetSearch == None:
        print(f"ONT with SN {serial} not found")
        return
    
    # Populating the rest of inputs
    vlan = fetch_input("vlan")
    lineProfile = fetch_input("Line Profile")
    serviceProfile = fetch_input("Service Profile")
    description = input("Enter a description(default ONT_DESC): ") or "ONT_DESC"

    
    send_ont_commands = net_connect.send_config_set([
        f"interface gpon {targetSearch[1]}/{targetSearch[2]}",
        f"ont add {targetSearch[3]} sn-auth {targetSearch[4]} omci ont-lineprofile-id {lineProfile} ont-srvprofile-id {serviceProfile} desc {description}\n"
        ])
    # we will send the above command using netmiko
    ont_ID_pattern = re.search(r"ONTID\s+:\s*(\d+)",send_ont_commands)
    print([ont_ID_pattern[1]], vlan, targetSearch[1], targetSearch[2], targetSearch[3])
    return {
        'ont_id' : ont_ID_pattern[1],
        'vlan' : vlan,
        'board' : targetSearch[1],
        'card' : targetSearch[2],
        'port' : targetSearch[3],
    }


# def fetch_gemport(net_connect, lineprofile, vlan):
#     line_profile_details = net_connect.send_command(f"display current-configuration | begin ont-lineprofile gpon profile-id {lineprofile}")
#     gemport_pattern = fr"profile-id {lineprofile}.gem mapping (\d) (\d) vlan {vlan}"


if __name__ == "__main__":
    add_ont()
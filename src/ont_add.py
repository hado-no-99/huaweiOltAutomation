import re
import sys
# reading the file 
file = open("src\\test.txt", "r")
sampleText = file.read()

def add_ont():
    # applying error handling for user inputs
    def fetch_input(context):
        is_serial = (context == "Serial Number")
        while True:
            userInput = input(f"Enter the {context}(default 0): ")
            if userInput.isnumeric():
                if is_serial and len(userInput) < 4:
                    print("Please enter a valid Serial Number")
                    continue
                else:
                    return userInput
                
            elif userInput == "":
                if not is_serial:
                    return "0"
                else:
                    print("Please enter a valid Serial Number")
            else:
                print(f"Please enter a valid {context}")

    # Populating inputs 
    serial = fetch_input("Serial Number")
    vlan = fetch_input("vlan")
    lineProfile = fetch_input("Line Profile")
    serviceProfile = fetch_input("Service Profile")
    description = input("Enter a description(default ONT_DESC): ") or "ONT_DESC"

    # Searching for our required Serial number
    targetSearch = re.search(fr"^F/S/P : (\d)/(\d)/(\d)\sOnt SN : (\d+{serial})",sampleText,re.MULTILINE)
    if targetSearch == None:
        print(f"ONT with SN {serial} not found")
        return
    
    
    ont_command_text = f"interface gpon {targetSearch[1]}/{targetSearch[2]}\nont add {targetSearch[3]} sn-auth {targetSearch[4]} omci ont-lineprofile-id {lineProfile} ont-srvprofile-id {serviceProfile} desc {description}\n"
    # we will send the above command using netmiko
    ont_command = """------------------------------------------------------------------------
                Command executed successfully
                ONTID : 12
  ------------------------------------------------------------------------"""

    ont_ID_pattern = re.search(r"ONTID : (\d+)",ont_command)
    return {
        'ont_id' : ont_ID_pattern[1],
        'vlan' : vlan,
        'board' : targetSearch[1],
        'card' : targetSearch[2],
        'port' : targetSearch[3],
    }


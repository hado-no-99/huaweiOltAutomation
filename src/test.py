import re
output_string = """ont-lineprofile gpon profile-id 0 profile-name "line-profile_default_0"
  tcont 0 dba-profile-id 2
  tcont 4 dba-profile-id 100
  gem add 1 eth tcont 4
  gem add 2 eth tcont 4
  gem mapping 1 1 vlan 930
  gem mapping 1 2 vlan 946
  gem mapping 1 3 vlan 832
  commit
  quit
 ont-lineprofile gpon profile-id 1 profile-name "SMARTOLT_FLEXIBLE_GPON"
  fec-upstream enable
  tr069-management enable
  mapping-mode priority
  tcont 0 dba-profile-id 2
  tcont 1 dba-profile-id 10
  tcont 2 dba-profile-id 10
  tcont 3 dba-profile-id 10
  gem add 1 eth tcont 1
  gem add 2 eth tcont 2
  gem add 3 eth tcont 3
  gem mapping 1 1 priority 0
  gem mapping 2 1 priority 2
  gem mapping 3 1 priority 5
  commit
  quit
 ont-lineprofile gpon profile-id 3 profile-name "Generic_1_V832"
  tcont 0 dba-profile-id 2
  tcont 1 dba-profile-id 10
  tcont 2 dba-profile-id 10
  gem add 1 eth tcont 1
  gem add 2 eth tcont 2
  gem mapping 1 1 vlan 832
  commit
  quit
 ont-lineprofile gpon profile-id 4 profile-name "Generic_1_V930"
  tcont 0 dba-profile-id 2
  tcont 1 dba-profile-id 10
  tcont 2 dba-profile-id 10
  gem add 1 eth tcont 1
  gem add 2 eth tcont 2
  gem mapping 1 1 vlan 930
  commit
  quit
 ont-lineprofile gpon profile-id 5 profile-name "Generic_1_V946"
  tcont 0 dba-profile-id 2
  tcont 1 dba-profile-id 10
  tcont 2 dba-profile-id 10
  gem add 1 eth tcont 1
  gem add 2 eth tcont 2
  gem mapping 1 1 vlan 946
  commit
  quit
 ont-lineprofile gpon profile-id 6 profile-name "Generic_1_V1984"
  tcont 0 dba-profile-id 2
  tcont 1 dba-profile-id 10
  tcont 2 dba-profile-id 10
  gem add 1 eth tcont 1
  gem add 2 eth tcont 2
  gem mapping 1 1 vlan 1984
  commit
  quit
 ont-lineprofile gpon profile-id 7 profile-name "Generic_1_V40"
  tcont 0 dba-profile-id 2
  tcont 1 dba-profile-id 10
  tcont 2 dba-profile-id 10
  gem add 1 eth tcont 1
  gem add 2 eth tcont 2
  gem mapping 1 1 vlan 40
  commit
  quit
 ont-lineprofile gpon profile-id 8 profile-name "Generic_1_V931"
  tcont 0 dba-profile-id 2
  tcont 1 dba-profile-id 10
  tcont 2 dba-profile-id 10
  gem add 1 eth tcont 1
  gem add 2 eth tcont 2
  gem mapping 1 1 vlan 931
  commit
  quit
 ont-lineprofile gpon profile-id 22 profile-name "Double2"
  tcont 1 dba-profile-id 22
  gem add 1 eth tcont 1
  gem add 2 eth tcont 1
  gem add 3 eth tcont 1
  gem mapping 2 3 vlan 930
  gem mapping 3 3 vlan 931
  commit
  quit
 ont-lineprofile gpon profile-id 44 profile-name "44mb"
  tcont 1 dba-profile-id 44
  gem add 1 eth tcont 1
  gem add 2 eth tcont 1
  gem add 3 eth tcont 1
  gem add 4 eth tcont 1
  gem add 5 eth tcont 1
  gem add 6 eth tcont 1
  gem add 7 eth tcont 1
  gem add 8 eth tcont 1
  gem mapping 1 1 vlan 35
  gem mapping 1 2 vlan 946
  gem mapping 1 3 vlan 930
  gem mapping 1 4 vlan 832
  commit
  quit
 ont-lineprofile gpon profile-id 101 profile-name "1G"
  tcont 1 dba-profile-id 101
  gem add 1 eth tcont 1
  gem add 2 eth tcont 1
  gem add 3 eth tcont 1
  gem add 4 eth tcont 1
  gem add 5 eth tcont 1
  gem mapping 1 1 vlan 45
  gem mapping 1 2 vlan 109
  gem mapping 1 3 vlan 1038
  gem mapping 1 4 vlan 1586
  gem mapping 1 5 vlan 3148
  gem mapping 1 7 vlan 3675
  gem mapping 2 0 vlan 3832
  gem mapping 2 1 vlan 3874
  gem mapping 2 2 vlan 40
  gem mapping 2 3 vlan 35
  gem mapping 2 4 vlan 1984
  commit
  quit
#
[device-config]
  <device-config>
 board add 0/3 H805GPFD
 board add 0/4 H805GPFD
 board add 0/5 H805GPFD
 board add 0/9 H801X2CS
 board add standby
#
"""

matching_text = ""
gemport_pattern = fr"profile-id {"0"}[\s\S]*?gem mapping (\d) (\d) vlan ({"930"})"
gemport_match = re.search(gemport_pattern,matching_text,re.DOTALL)
print([gemport_match[1],gemport_match[2],gemport_match[3]])
#!/bin/bash

# Replace these with your actual OLT CLI login details
OLT_IP="192.168.209.209"
OLT_USER="root"
OLT_PASS="admin"

# OLT Interface details
PON_PORT="gpon-olt_1/1/1"
LINE_PROFILE_ID="0"
SRV_PROFILE_ID="0"

# Login to OLT and get unconfigured ONUs
onu_sn=$(sshpass -p "$OLT_PASS" ssh -o StrictHostKeyChecking=no $OLT_USER@$OLT_IP "
enable
show gpon onu uncfg | include $PON_PORT
" | grep "$PON_PORT" | awk '{print $2}' | head -n 1)

if [ -z "$onu_sn" ]; then
  echo "❌ No unconfigured ONU found on $PON_PORT."
  exit 1
fi

echo "✅ Found ONU: $onu_sn"

# Configure ONU
sshpass -p "$OLT_PASS" ssh -o StrictHostKeyChecking=no $OLT_USER@$OLT_IP "
enable
config
interface $PON_PORT
onu add $onu_sn sn-auth $onu_sn omci ont-lineprofile-id $LINE_PROFILE_ID ont-srvprofile-id $SRV_PROFILE_ID
"

echo "✅ ONU $onu_sn configured successfully on $PON_PORT"

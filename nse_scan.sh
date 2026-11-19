#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <IP_Address> <NSE_Script_Name>"
    echo "Example: $0 127.0.0.1 smb-os-discovery"
    exit 1
fi

TARGET_IP=$1
SCRIPT_NAME=$2

echo "[*] Running Nmap NSE script '$SCRIPT_NAME' against $TARGET_IP..."

nmap -Pn --script "$SCRIPT_NAME" "$TARGET_IP"

echo "[*] Scan complete."

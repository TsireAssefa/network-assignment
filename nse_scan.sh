#!/bin/bash

# Check if the user provided exactly 2 arguments
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <IP_Address> <NSE_Script_Name>"
    echo "Example: $0 127.0.0.1 smb-os-discovery"
    exit 1
fi

# Assign arguments to variables
TARGET_IP=$1
SCRIPT_NAME=$2

echo "[*] Running Nmap NSE script '$SCRIPT_NAME' against $TARGET_IP..."
echo "--------------------------------------------------------"

# Run Nmap
# -Pn: Treat host as online (skips ping, useful if ICMP is blocked)
# --script: Specifies the NSE script to run
nmap -Pn --script "$SCRIPT_NAME" "$TARGET_IP"

echo "--------------------------------------------------------"
echo "[*] Scan complete."

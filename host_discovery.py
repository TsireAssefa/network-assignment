#!/usr/bin/env python3
import netifaces
import ipaddress

def get_gateway():
    try:
        gws = netifaces.gateways()
        gateway_info = gws['default'][netifaces.AF_INET]
        return gateway_info[0]
    except (KeyError, IndexError):
        return None

def get_ip_class(ip_str):
    try:
        ip = ipaddress.IPv4Address(ip_str)
    except ipaddress.AddressValueError:
        return "Invalid IP"

    first_octet = int(ip_str.split('.')[0])
    
    if 1 <= first_octet <= 126:
        return "Class A"
    elif 128 <= first_octet <= 191:
        return "Class B"
    elif 192 <= first_octet <= 223:
        return "Class C"
    elif 224 <= first_octet <= 239:
        return "Class D (Multicast)"
    elif 240 <= first_octet <= 255:
        return "Class E (Experimental)"
    else:
        return "Unknown / Loopback"

if __name__ == "__main__":
    print("--- Host Discovery Tool ---")
    
    gw = get_gateway()
    if gw:
        print(f"[*] Default Gateway: {gw}")
        print(f"[*] Gateway IP Class: {get_ip_class(gw)}")
    else:
        print("[!] Could not determine default gateway.")

    target_ip = input("\nEnter an IP to check its class (or press Enter to skip): ").strip()
    if target_ip:
        print(f"[*] IP: {target_ip}")
        print(f"[*] Class: {get_ip_class(target_ip)}")

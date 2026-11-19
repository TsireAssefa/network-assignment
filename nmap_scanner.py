#!/usr/bin/env python3
import nmap
import sys

def nmap_scan(target, ports):
    nm = nmap.PortScanner()
    
    print(f"[*] Starting Nmap scan on {target} for ports: {ports}...")
    
    try:
        nm.scan(hosts=target, ports=ports, arguments='-sT -sV -T4')
    except nmap.PortScannerError as e:
        print(f"[!] Nmap error: {e}")
        return

    if target not in nm.all_hosts():
        print(f"[!] Host {target} seems to be down or unreachable.")
        return

    print(f"\n--- Scan Results for {target} ---")
    for host in nm.all_hosts():
        print(f"Host: {host} ({nm[host].hostname()})")
        print(f"State: {nm[host].state()}")
        
        for proto in nm[host].all_protocols():
            print(f"Protocol: {proto}")
            
            lport = nm[host][proto].keys()
            
            for port in sorted(lport):
                state = nm[host][proto][port]['state']
                
                if state == 'open':
                    service = nm[host][proto][port]['name']
                    version = nm[host][proto][port].get('version', '')
                    print(f"Port: {port}\tState: {state}\tService: {service} {version}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 nmap_scanner.py <IP_or_domain> <port_range>")
        print("Example: python3 nmap_scanner.py 10.204.159.111 20-100")
        sys.exit(1)
        
    target_ip = sys.argv[1]
    port_range = sys.argv[2]
    
    nmap_scan(target_ip, port_range)

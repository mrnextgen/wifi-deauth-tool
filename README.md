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

#!/usr/bin/env python3

# Source: https://blog.cloudflare.com/ssdp-100gbps

import socket
import sys

dst = "239.255.255.250"
if len(sys.argv) > 1:
    dst = sys.argv[1]

st = "upnp:rootdevice"
if len(sys.argv) > 2:
    st = sys.argv[2]

msg = [
    f'M-SEARCH * HTTP/1.1',
    f'Host:239.255.255.250:1900',
    f'ST:{st}',
    f'Man:"ssdp:discover"',
    f'MX:1',
    f'']

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
s.settimeout(10)
s.sendto(str.encode('\r\n'.join(msg)), (dst, 1900))

while True:
    try:
        data, addr = s.recvfrom(32*1024)
    except socket.timeout:
        break
    print(f"[+] {addr}\n{bytes.decode(data)}")

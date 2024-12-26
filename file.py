#!/usr/bin/env python

import socket

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ""

print(get_local_ip())
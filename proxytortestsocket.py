#!/usr/bin/python
# you can test tor proxy setting and real/proxi ip address
import socket
import socks  # you need to install pysocks ("pip install pysocks")

# Configuration
SOCKS5_PROXY_HOST = '127.0.0.1'
SOCKS5_PROXY_PORT = 9050

# Remove this if you don't plan to "deactivate" the proxy later
default_socket = socket.socket

# Set up a proxy
socks.set_default_proxy(socks.SOCKS5, SOCKS5_PROXY_HOST, SOCKS5_PROXY_PORT)
socket.socket = socks.socksocket

# - If you use urllib2:
import urllib2
print urllib2.urlopen('http://icanhazip.com/', timeout=24).read()  # outputs proxy IP

# - If you use requests (pip install requests):
import requests
print requests.get('http://icanhazip.com/', timeout=24).text  # outputs proxy IP

# Use this only if you plan to make requests without any proxies later
socket.socket = default_socket

# Make a request normally without a proxy; this will output your own public IP
print urllib2.urlopen('http://icanhazip.com/', timeout=24).read()
#!/bin/python3

import sys
import socket
from datetime import datetime


if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py")
    sys.exit(1)


print("-" * 50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)


print("Hello, LorenzoMorleone is going  to scan for open ports.")
port_descriptions = {
    20: "FTP (This possibly is a File Transfer Protocol)",
    21: "FTP (This possibly is a File Transfer Protocol)",
    22: "SSH (This possibly is a Secure Shell)",
    23: "Telnet",
    25: "SMTP (This possibly is a Simple Mail Transfer Protocol)",
    53: "DNS (This possibly is a Domain Name System)",
    80: "HTTP (This possibly is a Hypertext Transfer Protocol)",
    443: "HTTPS (This possibly is a Hypertext Transfer Protocol Secure)",
    3389: "RDP (This possibly is aRemote Desktop Protocol)",
    8080: "This possibly is a HTTP Proxy",
}
 
try:
    for port in range(1, 10000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
print("Port {} is open".format(port))
            if port in port_descriptions:
                print("Port {} ({}) is open".format(port, port_descriptions[>
            else:
                print("Port {} is open".format(port))

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit(1)

except socket.error:
    print("Could not connect to the server.")
    sys.exit(1)


print("LorenzoMorleone was here. Aloha!")
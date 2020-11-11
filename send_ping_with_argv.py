from scapy.layers.dns import *
from scapy.all import *
from sys import argv

##### Mission 2 #####
for i in range(1, 3):
    my_ping = IP(dst='www.facebook.com')/ICMP(id=i)/'hello'
    send = sr(my_ping)


##### Mission 3 + 4 #####

commands = argv
amount_of_req = commands[-1]
received = []

print(f'Sending {amount_of_req} packets to {argv[1]}')
for i in range(1, int(amount_of_req)):
    my_ping = IP(dst=commands[1])/ICMP(id=i)/'hello'
    send = sr1(my_ping, verbose=False)
    received.append(send)

print(f'Received {len(received)} reply packets')

from scapy.all import *
from scapy.layers.dns import *

while True:
    enter = input('Enter a message: ')
    ports = map(lambda x: ord(x), [i for i in enter])

    for i in list(ports):
        packets = IP(dst='0.0.0.0', src='127.0.0.1')/UDP(dport=i)
        send(packets)

    if enter == '!end':
        break

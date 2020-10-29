from scapy.all import *
from scapy.layers.dns import *


def dns_packet(packet):
    return UDP in packet

while True:
    packets = sniff(count=1, lfilter=dns_packet)

    index = 0
    result = ''

    for i in packets:

        result += str(chr(packets[index][UDP].dport))
        index += 1
    print('The secret message is: ', result)

    if result == '!':
        break


from scapy.layers.l2 import *
from scapy.all import *

def promi_scanner():

    """
    Scan the network for promiscuous mode by sending fake ARP broadcast,
    in order for us to check if the os system checks all the bits and drop the frame or whether it will respond.
    """

    enter_ip = input('Enter IP to scan: ')
    enter_ip = '.'.join(enter_ip.split('.')[:3])
    enter_router = input('Enter router address: ')

    for i in range(256):
        # Fake broadcast address
        arp_packet = Ether(dst='FF:FF:FF:FF:FF:FE') / ARP(pdst=f'{enter_ip}.{i}')
        router = enter_router

        sendp(arp_packet, verbose=False)

        sniff_it = sniff(count=1, lfilter=lambda frame: Ether in frame and ARP in frame and frame[ARP].op == 2, timeout=0.5)

        if sniff_it:
            if sniff_it[0][Ether][ARP].psrc != arp_packet[ARP].psrc and sniff_it[0][Ether][ARP].psrc != router:
                print(f'{sniff_it[0][Ether][ARP].psrc} is in promiscuous mode')

            else:
              pass

print(promi_scanner())


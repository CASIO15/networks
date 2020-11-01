from scapy.all import *
from scapy.layers.dns import *

syn_segment = TCP(dport=80, seq=123, flags='S')
syn_packet = IP(dst='www.google.com')/syn_segment
syn_akc_packet = sr1(syn_packet)

ack_segment = IP(dst='www.google.com')/TCP(dport=80,
                                           ack=int(syn_akc_packet[TCP].ack) + 1,
                                           seq=int(syn_akc_packet[TCP].seq) + 1,
                                           flags='A')

ack_packet = IP(dst='www.google.com')/ack_segment
send(ack_packet)

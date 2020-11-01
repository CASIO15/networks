from scapy.layers.dns import *

enter = input('Enter your IP address: ')
ports = []

for i in range(20, 1025):

    # building a SYN segment
    syn_segment = TCP(dport=i, flags='S', seq=123)

    # Building the packet with the SYN segment
    syn_packet = IP(dst=enter)/syn_segment

    # Sending one packet, and receiving one answer, setting timeout
    syn_ack_packet = sr1(syn_packet, timeout=2)

    # Checking if the TCP flag is SYN - ACK
    # if exception is raising, pass
    try:
        if syn_ack_packet[TCP].flags == 'SA':
            ports.append(syn_ack_packet[TCP].sport)

    except:
        pass

# Printing open ports, else if there are no open ports
if ports:
    for open in ports:
        print(f'Port {open} is open...')
else:
    print('No open ports...')

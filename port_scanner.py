from scapy.layers.dns import *

enter = input('Enter the IP address you want to scan: ')
start = int(input('START: '))
stop = int(input('STOP: '))
ports = []

# setting start and stop ports range for the scanning
for i in range(start, stop + 1):

    # building a SYN segment
    syn_segment = TCP(dport=i, flags='S', seq=123)

    # Building the packet with the SYN segment
    syn_packet = IP(dst=enter)/syn_segment

    # Sending one packet, and receiving one answer, setting timeout
    syn_ack_packet = sr1(syn_packet, timeout=0.1)

    # Checking if the TCP flag is SYN - ACK
    # if exception is raised, pass
    try:
        if syn_ack_packet[TCP].flags == 'SA':
            ports.append(syn_ack_packet[TCP].sport)

    except:
        pass

# Printing open ports, else if there are no open ports
if ports:
    for open in ports:
        print(f'Port << {open} >> is open...')
else:
    print('No open ports...')

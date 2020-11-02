from scapy.layers.dns import *
from time import perf_counter

enter = input('Enter the IP address you want to scan: ')
start = int(input('START: '))
stop = int(input('STOP: '))
ports = []

print(f'scanning {enter} from port {start} to {stop}\n')
start_time = perf_counter()

# setting start and stop ports range for the scanning
for i in range(start, stop + 1):

    # building a SYN segment
    syn_segment = TCP(dport=i, flags='S', seq=123)

    # Building the packet with the SYN segment
    syn_packet = IP(dst=enter)/syn_segment

    # Sending one packet, and receiving one answer, setting timeout
    syn_ack_packet = sr1(syn_packet, timeout=0.1, verbose=0)

    # Checking if the TCP flag is SYN - ACK
    # if exception is raised, pass
    try:
        if syn_ack_packet[TCP].flags == 'SA':
            ports.append(syn_ack_packet[TCP].sport)

    except:
        pass

# Printing open ports, else if there are no open ports
if ports:
    for o in ports:
        print(f'Port << {o} >> is open...')

else:
    print('No open ports...')

print(f'Scan is complete | time: {abs(start_time - perf_counter())}')

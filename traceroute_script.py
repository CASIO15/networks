from scapy.layers.inet import *
from scapy.all import *
from sys import argv
from time import perf_counter

def traceroute(argv):
  ''' Sending ttl with a for loop, the routers will return us a ttl exceeded.
       When we reach destination we break, I used argv to run it from the console. '''
  
    max_hops = int(input('Enter max hops: '))
    start = perf_counter()
    addr = argv[1]

    for i in range(1, max_hops + 1):
        trace = IP(dst=addr, ttl=i)/ICMP()/'abcdefg'
        send_it = sr1(trace, verbose=False)
        start_packet = perf_counter()

        if send_it[ICMP].type == 11:
            print(f'{send_it[IP].src},  {abs(start_packet - perf_counter() * 10): .3f} ms')
        else:
            print(f'Packet arraived to destination {send_it[IP].src}')
            break

    return f'ms {(perf_counter() - start) * 100: .3f}'

print(traceroute(argv))


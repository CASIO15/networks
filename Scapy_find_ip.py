from scapy.layers.dns import *
import re

enter = input('Enter website address: ')

def get_ip(arg):

    dns_packet = IP(dst='8.8.8.8')/UDP(dport=53)/DNS(qdcount=1, rd=1)/DNSQR(qname=arg)
    response_packet = sr1(dns_packet)

    result = str(response_packet[DNSRR].lastlayer).split('=')
    answer = result[-1].split()[0]

    # Another approach using regular expressions
    # answer = re.findall(r"[0-9]+(?:\.[0-9]+){3}", str(result))

    return f'The IP address is << {answer} >>'

print(get_ip(enter))

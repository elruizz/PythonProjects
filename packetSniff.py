from scapy.all import *
from optparse import OptionParser
import sys
import os
import socket
import netifaces
target_table = ["192.168.1.98","192.168.21.215","192.168.21.212", "192.168.1.43"]
gws = netifaces.gateways()

def getAttacker():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    attacker = s.getsockname()[0]
    s.close()
    return attacker

print("Custom packet sniffer")
if os.getuid() != 0:
    print("[-] Run me as root")
    sys.exit(1)

usage = "Usage: %prog [-i interface] [ -t target_ip ] [ -f filter ]"
me = "192.168.1.97"
parser = OptionParser(usage)
parser.add_option('-i', dest="interface", help='Select the wireless or ethernet interface you want to use.')
parser.add_option('-t', dest="target", help='Select the target ip you want to sniff for if any')
parser.add_option('-f', dest="filter", help="Lets you choose what packets your are sniffing (default='ip')")
#read from a file in the future
(options, args)=parser.parse_args()

attacker = getAttacker()
if options.interface is None:
    interface = "wlp3s0"
else:
    interface = options.interface
if options.target is None:
    pass
else:
    if options.target in target_table:
        pass
    else:
        target_table.append(options.target)
if options.filter is None:
    filter = "ip"
else:
    filter = options.filter
def Sniff_Packet(packet):
    if packet.haslayer(IP):
        pckt_src=packet[IP].src
        pckt_dst=packet[IP].dst
        pckt_ttl=packet[IP].ttl
        if (pckt_dst != attacker and pckt_src != attacker) and pckt_src not in ["162.159.133.234"]:
        #if pckt_dst == "192.168.21.215" or pckt_src=="192.168.21.215":
            print ("IP Packet:"+str(pckt_src)+" is going to "+str(pckt_dst)+" and has ttl value "+str(pckt_ttl))
        #if pckt_src in ["192.168.21.215"] or pckt_dst ==  "192.168.21.215":
            packet.show()
try:
    sniff(filter=filter,iface=interface,prn=Sniff_Packet)
except OSError:
    parser.print_help()
    sys.exit(1)

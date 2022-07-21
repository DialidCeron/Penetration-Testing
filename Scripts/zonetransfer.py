#!/usr/bin/python3
#Script to attempt a zone transfer from a domain.
##Author: Lezly Dialid Cerón Rodríguez

import dns.zone
import dns.resolver
import sys

if len(sys.argv) != 2:
        print("Usage: zonetransfer.py <target domain>")
        sys.exit(0)

print("[*] Resolving NS servers...")
print("[*] Attempting zone transfer...")
answer=dns.resolver.resolve(sys.argv[1], 'NS')
for ns in answer:
        ip_ns=dns.resolver.resolve(ns.target, 'A')
        for ip in ip_ns:
                print("[+] Found NS: {} IP: {}".format(ns, ip))
                try:
                        zone=dns.zone.from_xfr(dns.query.xfr(str(ip), sys.argv[1]))
                        for host in zone:
                                print("[+] Found Host: {}".format(host))
                except Exception as e:
                        print("[-] Refused zone transfer from NS: {}".format(ns))
                        continue
#!/usr/bin/python3

import dns.resolver

txtRecords = []
ip = []

def dnsLookup(  hostname, result  ):

    answers = dns.resolver.query(hostname, 'TXT')
    for i in answers.response.answer:
        for j in i.items:

            dns_string = j.to_text()

            try:
                ipv4 = dns_string.index('ip4:')
                dns_list = dns_string.split('ip4:')
            except:
                ipv4 = False

            try:
                ipv6 = dns_string.index('ip6:')
                dns_list = dns_string.split('ip6:')
            except:
                ipv6 = False

            if ipv4 == False and  ipv6 == False:
                dns_list = dns_string.split('include:')

            del dns_list[0]
            for k in dns_list:
                n = k.split(' ')
                result.append(n[0])


dnsLookup('_spf.google.com', txtRecords)

k = 0
for k in range(len(txtRecords)):
    dnsLookup(txtRecords[k], ip)

for item in ip:
    print(item + "      OK")


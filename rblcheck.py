#!/usr/bin/python

import sys
import os
import csv
import socket
import subprocess
import shlex

RBLS = [
    'aspews.ext.sorbs.net',
    'b.barracudacentral.org',
    'bl.deadbeef.com',
    'bl.emailbasura.org',
    'bl.spamcannibal.org',
    'bl.spamcop.net',
    'blackholes.five-ten-sg.com',
    'blacklist.woody.ch',
    'bogons.cymru.com',
    'cbl.abuseat.org',
    'cdl.anti-spam.org.cn',
    'combined.abuse.ch',
    'combined.rbl.msrbl.net',
    'db.wpbl.info',
    'dnsbl-1.uceprotect.net',
    'dnsbl-2.uceprotect.net',
    'dnsbl-3.uceprotect.net',
    'dnsbl.ahbl.org',
    'dnsbl.cyberlogic.net',
    'dnsbl.dronebl.org',
    'dnsbl.inps.de',
    'dnsbl.njabl.org',
    'dnsbl.sorbs.net',
    'drone.abuse.ch',
    'duinv.aupads.org',
    'dul.dnsbl.sorbs.net',
    'dul.ru',
    'dyna.spamrats.com',
    'dynip.rothen.com',
    'http.dnsbl.sorbs.net'
    'images.rbl.msrbl.net',
    'ips.backscatterer.org',
    'ix.dnsbl.manitu.net',
    'korea.services.net',
    'misc.dnsbl.sorbs.net',
    'noptr.spamrats.com',
    'ohps.dnsbl.net.au',
    'omrs.dnsbl.net.au',
    'orvedb.aupads.org',
    'osps.dnsbl.net.au',
    'osrs.dnsbl.net.au',
    'owfs.dnsbl.net.au',
    'owps.dnsbl.net.au'
    'pbl.spamhaus.org',
    'phishing.rbl.msrbl.net',
    'probes.dnsbl.net.au'
    'proxy.bl.gweep.ca',
    'proxy.block.transip.nl',
    'psbl.surriel.com',
    'rbl.interserver.net',
    'rdts.dnsbl.net.au',
    'relays.bl.gweep.ca',
    'relays.bl.kundenserver.de',
    'relays.nether.net',
    'residential.block.transip.nl',
    'ricn.dnsbl.net.au',
    'rmst.dnsbl.net.au',
    'sbl.spamhaus.org',
    'short.rbl.jp',
    'smtp.dnsbl.sorbs.net',
    'socks.dnsbl.sorbs.net',
    'spam.abuse.ch',
    'spam.dnsbl.sorbs.net',
    'spam.rbl.msrbl.net',
    'spam.spamrats.com',
    'spamlist.or.kr',
    'spamrbl.imp.ch',
    't3direct.dnsbl.net.au',
    'tor.ahbl.org',
    'tor.dnsbl.sectoor.de',
    'torserver.tor.dnsbl.sectoor.de',
    'ubl.lashback.com',
    'ubl.unsubscore.com',
    'virbl.bit.nl',
    'virus.rbl.jp',
    'virus.rbl.msrbl.net',
    'web.dnsbl.sorbs.net',
    'wormrbl.imp.ch',
    'xbl.spamhaus.org',
    'zen.spamhaus.org',
    'zombie.dnsbl.sorbs.net',
]

# To use any IP
print("\n")

addr = raw_input('Please enter ip address: ')

print("\n")

# Checking if IP address is entered

if addr != "":
    print 'You have typed ' + addraddr
else: 
    # to use local IP
    hostname = socket.gethostname()
    address = socket.gethostbyname("%s.local" % hostname)
    addr = address

print "Using local IP : " + addr
print("\n")

# reverse IP
raddr = addr[::-1]
print "Your IP address in reverse : " + raddr
print("\n")

print "Now to print the IP address in reverse and rbl with it"
print("\n")
# adding reversed ip to the dns name
jRBLS = []
for x in RBLS:
    jRBLS.append(raddr+'.'+x)
print jRBLS

# now to do the look of the dns entry
print("\n")
print "checking ip in RBL list ..."
print("\n")
for x in jRBLS:
    p1 = subprocess.Popen(["dig " + x + "+short"],  shell=True, stdout=subprocess.PIPE)
    print p1.communicate()[0]

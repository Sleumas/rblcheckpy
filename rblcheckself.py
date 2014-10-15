#!/usr/bin/python

import re                                  
import subprocess
import socket     


x = raw_input('What is your IP address? ')
def ipformatcheck(x):
    pattern = r"\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]?[0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"
    if re.match(pattern, x):
        #return True
        print ('\nLooking up ip on RBL : ' + x +'\n')
        #print ('Reversing the IP')
        ip = str(x).split('.')
        rev = '%s.%s.%s.%s' % (ip[3],ip[2],ip[1],ip[0])
        spamdbs = ['.dnsbl.sorbs.net', '.cbl.abuseat.org', '.bl.spamcop.net', '.zen.spamhaus.org', '.sbl.spamhaus.org', '.xbl.spamhaus.org', '.pbl.spamhaus.org', '.spamsources.fabel.dk', '.stop.stop.org']
        for db in spamdbs:
                       if db == '.stop.stop.org':
                           break            
                       p = subprocess.Popen(["dig", "+short", rev+db], stdout=subprocess.PIPE)
                       output, err = p.communicate()
                       print db
                       print output
    else:
        hostname = socket.gethostname()
        address = socket.gethostbyname("%s.local" % hostname)
        x = address
        print ('\n Using local IP address : ' + x +'\n')
        ip = str(x).split('.')
        rev = '%s.%s.%s.%s' % (ip[3],ip[2],ip[1],ip[0])
        spamdbs = ['.dnsbl.sorbs.net', '.cbl.abuseat.org', '.bl.spamcop.net', '.zen.spamhaus.org', '.sbl.spamhaus.org', '.xbl.spamhaus.org', '.pbl.spamhaus.org', '.spamsources.fabel.dk', '.stop.stop.org']
        for db in spamdbs:
                       if db == '.stop.stop.org':
                           break            
                       p = subprocess.Popen(["dig", "+short", rev+db], stdout=subprocess.PIPE)
                       output, err = p.communicate()
                       print db
                       print output
ipformatcheck(x)

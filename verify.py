#!/usr/bin/python

import string

f = open("AuthentKey.txt", 'r')

username = f.readline()
key = f.readline()

username = username.strip('\n')
key = key.strip('\n')

#import pyotp
#totp = pyotp.TOTP(key)
#print "Access Code:", totp.now()

import hmac, time, hashlib, struct, base64
#get current time as int via a floor division by 30	
curtime = int(time.time())//30
#Convert ASCII string from  byte string key	
keydecode = base64.b32decode(key)
#time conversion into raw bytes
timepack  = struct.pack(">q", curtime)
#generate HMAC object
HMAC = hmac.new(keydecode, timepack, hashlib.sha1).digest()
#trim 20 byte sha1 to 4 bytes
#extract lowest significant byte (4 bytes total)
offset = ord(HMAC[-1]) & 0x0F
truncHMAC = HMAC[offset:offset+4]
#convert bytes to number and mod by one million to get 6 digit number
code = struct.unpack(">L", truncHMAC)[0]
code &= 0x7FFFFFFF;
code %= 1000000;
#print code
print "Access Code: %06d" % code



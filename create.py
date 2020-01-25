#!/usr/bin/python

#QR code generator

import pip
installed_packages = pip.get_installed_distributions()
flat_installed_packages = [package.project_name for package in installed_packages]

#print installed_packages
#print flat_installed_packages

if not 'qrcode' in flat_installed_packages:
	print "ERROR: No python qrcode"
	print "To install type: pip install --upgrade --user qrcode"
	exit()
if not 'Pillow' in flat_installed_packages:
	print "ERROR: No pillow"
	print "To install type: pip  install --user pillow"
	exit()
if not 'pyotp' in flat_installed_packages:
	print "Error: No pyotp"
	print "To install type: pip install --user pyotp"
	exit()

#Get username input
usertxt = raw_input("Enter a user name to generate the code: ")

#generate key

import random
import string

randominputchars = string.ascii_uppercase + '234567'

key = ''.join(random.choice(randominputchars) for i in range(32))

#store key info
f = open("AuthentKey.txt", "w")
f.write(usertxt)
f.write('\n')
f.write(key)
f.close()


#Generate GA URI
#import pyotp
#AuthURI = pyotp.totp.TOTP(key).provisioning_uri(usertxt, issuer_name="DanAuth")
#print AuthURI

AuthURI= "otpauth://totp/DanAuth:%s?secret=%s&issuer=DanAuth"%(usertxt,key)
print AuthURI

#generate QR SVG
import qrcode
import PIL
#from PIL import Image

#create qr instance
#qr = qrcode.QRCode(version =1, error_correction = qrcode.constants.ERROR_CORRECT_H, box_size = 10, border = 4)

###############################must update qrcode for this to work
img = qrcode.make(AuthURI)
img.save("QR.jpg")



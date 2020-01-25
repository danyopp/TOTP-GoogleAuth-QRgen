create.py will generate a random key and create a QR code that can be scanned by the Google Authenticator app.

An additional “AuthentKey.txt” file is created to debug and contains the generated key and the user inputs. This file is read by “verify.py” when generating one time passwords.

Verify.py will generate the same one time passwords as the google authenticator app. 

This implementation does not utilize the pyotp package but hardcodes the algorithm. The pyotp solution is commented out in the code. 

A bash script is included to make using the files easier. Instructions are below. 

Comments are included to explain algorithm

========================================================
Program Guide

Prereqs:


   Input:
	./submission.sh --installer


======= Creating a QR code: =================================
   Input:
	 ./submission.sh --generate-qr


	This will create a text file titled AuthentKey.txt that contains the username and key of the created QR code. 
	The QR code is also created and placed in the same directory.

Scan the QR code with the iOS GA app. It should automatically add to the list of authentications


======= Getting an OTP: ====================================
   Input:
	./submission.sh --get-otp
	
	This will use the AuthentKey.txt file to determine the TOTP 

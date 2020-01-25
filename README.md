create.py will generate a random key and create a QR code that can be scanned by the Google Authenticator app.

An additional “AuthentKey.txt” file is created to debug and contains the generated key and the user inputs. This file is read by “verify.py” when generating one time passwords.

Verify.py will generate the same one time passwords as the google authenticator app. 

This implementation does not utilize the pyotp package but hardcodes the algorithm. The pyotp solution is commented out in the code. 

A bash script is included to make using the files easier. Instructions are below. 

Program Guide
========================================================


	**./submission.sh --installer**

	Will attempt to install any needed dependencies 

Creating a QR code: =================================


   	**./submission.sh --generate-qr**  

	
	Scan the QR code with the iOS GA app. It should automatically add to the list of authentications
	This will create a text file titled AuthentKey.txt that contains the username and key of the created QR code. 
	The QR code is also created and placed in the same directory.


Getting an OTP: ====================================


	**./submission.sh --get-otp **
	
	This will use the AuthentKey.txt file to determine the TOTP 

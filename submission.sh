#!/bin/bash

if [ $1 = "--installer" ]
then
pip install --user pyotp
pip install --user qrcode
pip install --upgrade --user qrcode
pip install --user Pillow
fi

if [ $1 = "--generate-qr" ]
then
python create.py
fi

if [ $1 = "--get-otp" ]
then
python verify.py
fi	

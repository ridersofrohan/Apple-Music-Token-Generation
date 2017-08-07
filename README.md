# Apple-Music-Token-Generation
This is a python script that will generate an apple music developer token. It helps you make the Apple Music JWT tokens needed to use MusicKit on iOS

## Geting Started
Follow the instructions at [Apple Music API Reference](https://developer.apple.com/library/content/documentation/NetworkingInternetWeb/Conceptual/AppleMusicWebServicesReference/SetUpWebServices.html#//apple_ref/doc/uid/TP40017625-CH2-SW1)

Then come back here and follow the remainder of the instructions below.

## Prerequisites
After following the instructions at the URL above, you should now have 3 pieces of data:

- a MusicKit private key in a *.p8 file
- a 10-digit key identifier in your Apple Developer account
- your 10-digit Apple Developer Account Team ID

## Setup
Make sure that you are using **PYTHON 2**

Install the Python JWT package
```
pip install pyjwt
```

Install the cryptography package
```
pip install cryptography
```

Install requests
```
pip install requests
```

## Customization
Place your MusicKit private key (the .p8 file you downloaded earlier) in the same directory as this file.


Open up the create_jwt file and edit the following lines:

Substitute YOUR_FILENAME with the filename of the .p8 file you downloaded, make sure to leave the .p8 extension.

```
filename = "YOUR_FILENAME.p8"
```

Substitute your 10-digit key identifier (kid) as found in your developer account

```
keyId = "1121212121"
```

Substitute your 10-digit Apple Developer Team ID

```
teamId = "2222222222"
```

Run the script

```
> python create_jwt.py
```

The script will output a token, sample curl command you can run to see if you were successful, and a sample response from a command using your jwt.

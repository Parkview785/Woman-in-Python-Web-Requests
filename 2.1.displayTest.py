''' 
This will display some test patterns onto the SW Maker LED Matrix

WiFi SSID:  SWMakerDraw
WiFi Password:  <there is none>
LED Matrix IP Address: 1.3.3.7

Usage:  python 2.1.displayTest.py

install Windows Python3 modules:
    py -3 -m pip install requests
    py -3 -m pip install Pillow
    py -3 -m pip list


'''

import requests
#  Pixel data is listed as:  RGB  - Red Green Blue
teststring = 'ff000000ff000000ff505050'
#             | Red | Grn |Blue |grey|

# display a pre-coded string of RGB values
print("Display Test Pixels:")
try:
    # will fail miserably if the WiFi connection is lost.  Try and make it a nicer with Try/Except
    response = requests.get('http://1.3.3.7/cc?pixels=' + teststring)
except ConnectionAbortedError:
    print("Lost WiFi connection.  Exciting program")
    exit()
except:
    print("Something else went wrong. Exciting program.")
    exit()
print("Webserver says: ", response)


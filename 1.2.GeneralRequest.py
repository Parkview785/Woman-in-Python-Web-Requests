'''
 This Python 3 script will display some basic Request content to the screen
 And we create a function to nicely display Header text

Usage:  py 1.2.GeneralRequest.py
   or:  python 1.2.GeneralRequest.py

 '''

import requests

def listHeaders(headerText):
    ''' This is a simple function'''
    print("Nicely list headers:")
    for key in headerText:
        print(key,": ", headerText[key])


r = requests.get("https://www.example.com/")         # use this URL first
#r = requests.get("https://www.example.com/badurl")  # use this URL next
#r = requests.get("https://www.taobao.com/")         # try this one last

print("webpage: ",r)  # prints out the response, ie: was it succesful or not
print("URL: ", r.url) # prints out the URL we just accessed
print("Headers:")
print(r.headers)      # displays the webpage header
print(listHeaders(r.headers))


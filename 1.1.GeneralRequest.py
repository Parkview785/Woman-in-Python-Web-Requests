'''
 This Python 3 script will display some basic Request content to the screen

Usage:  py 1.1.GeneralRequest.py
        python 1.1.GeneralRequest.py

 '''

import requests

r = requests.get("https://www.example.com/")         # use this URL first
#r = requests.get("https://www.example.com/badurl")  # use this URL next
#r = requests.get("https://www.taobao.com/")         # try this one last

print("webpage: ",r)  # prints out the response, ie: was it succesful or not
print("URL: ", r.url) # prints out the URL we just accessed
print("Headers:")
print(r.headers)      # displays the webpage header
print("Encoding: ", r.encoding) # what kind of encoding is the webpage written in?
print("Webpage Length:", len(r.text))    # length of the webpage in bytes
print("Text:")
text1 = r.text.encode('utf8')  # be safe, convert to content encoding type to utf-8
print(text1)          # displays the webpage text (mostly the same as content)


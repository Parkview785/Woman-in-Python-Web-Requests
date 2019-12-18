''' 
This Python script will connect to the SW Maker LED Matrix and display a supplied 
  JPG or PNG image.  It will first shrink the image down to 16 x 16 pixels. 

WiFi SSID:  SWMakerDraw
WiFi Password:  <there is none>
LED Matrix IP Address: 1.3.3.7

Usage:  python 3.1.display-JPG2Matrix.py

'''

import requests
import PIL


from PIL import Image
#im = Image.open("video1.jpg")
#im = Image.open("GBird.jpg")
#im = Image.open("image1.png")   # a white P on a pink background
im = Image.open("letterP1.1.jpg")   # a white P on a pink background
#im = Image.open("letterP1.2.jpg")   # a white P on a pink background

new_img = im.resize((16,16))

#print new_img.info   # display image PIL data for debug
#print("colors = ", new_img.getcolors(maxcolors=256))  # lists out the number of pixels of each RGB value
photo = ''
photoRed = ''
photoGreen = ''
photoBlue = ''
photoData = list(new_img.getdata())
print("Converting JPG to displayable formated array")
for i in range(256):
    # print(i,photoData[i])
    photoRed = photoRed + '{:03d}'.format(photoData[i][0])
    photoGreen = photoGreen + '{:03d}'.format(photoData[i][1] )
    photoBlue = photoBlue + '{:03d}'.format(photoData[i][2]) 
    photo = photo + '{:02x}'.format(photoData[i][0])+'{:02x}'.format(photoData[i][1])+'{:02x}'.format(photoData[i][2])

# display the 16x16 image onto local computer
index = 0
image = Image.new('RGB', (16, 16))
# place the array of 16x16 pixel data into a BitMaP image array
print("Convert 16x16 image data into a BitMap")
for y in range(16):
    for x in range(16):
        # show what the pixel numbers look like
        #print(x,y,index,photoRed[index]+photoRed[index+1]+photoRed[index+2],photoGreen[index]+photoGreen[index+1]+photoGreen[index+2],photoBlue[index]+photoBlue[index+1]+photoBlue[index+2])
        image.putpixel((x,y),(int(photoRed[index]+photoRed[index+1]+photoRed[index+2]),int(photoGreen[index]+photoGreen[index+1]+photoGreen[index+2]),int(photoBlue[index]+photoBlue[index+1]+photoBlue[index+2])))
        index += 3
image.show()    # display the 16x16 image onto the screen
image.save('photo-16x16.1.bmp','bmp')  # save the 16x16 bmp file to local folder

#print(photo)
print("Length of original :",len(photoData))
print("Length of conversion :",len(photo))
print("upload image to LED Matrix display")
try:
    response = requests.get('http://1.3.3.7/cc?pixels='+photo)
except ConnectionAbortedError:
    print("Lost WiFi connection.  Exciting program")
    exit()
except:
    print("Something else went wrong. Exciting program.")
    exit()
print( response )  # displays the LED Webserver response from uploading the BMP file


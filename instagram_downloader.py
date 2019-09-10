import pyperclip, requests
from bs4 import BeautifulSoup
import time
import sys

#for toolbar
toolbar_width = 100

address = pyperclip.paste()         #get the address from clipboard
res = requests.get(address)         #get the request object from the address
html = res.text                     #get the whole HTML page from res.text 
soup = BeautifulSoup(html, "lxml")  #parse the whole HTML Page as object
photo_url = soup.find("meta", property="og:image")  #the images are saved
                                                    #in the meta tag
url = photo_url["content"]          #get the image URL from the content
photo_name = url[-25:-6]            #get the name of the file
res = requests.get(url)             #hit the actual image.jpg URL

#save the file in the below location
playFile = open("C:\\delicious\\walnut\\waffles\\" + photo_name + ".jpg", "wb")
# setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width)),
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width + 1))  # return to start of line, after '['

#loop through the chunk of file (Image) in this case
#10000 at a time.
for chunk in res.iter_content(10000):
    # do real work here
    playFile.write(chunk)
    # print('Processing')
    time.sleep(0.1)  
    # update the bar
    sys.stdout.write("▊")
    sys.stdout.flush()
sys.stdout.write("]\n")  # this ends the progress bar
playFile.close()
print("Download Complete!")


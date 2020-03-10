

import requests
from  urllib import request
import os 
import cv2 as cv

def is_url_image(image_url):
   image_formats = ("image/png", "image/jpeg", "image/jpg")
   r = requests.head(image_url)
   print(r.headers.keys())
   if r.headers['Content-Length'] != 0:
      return True
   return False

def downloadImages():
    baseFolder = "I:\\CandidPhotoProject\\professionalPotraitImagesDataset\\"
    urllist = open(baseFolder + 'URLList.txt')
    
    lines = urllist.readlines()
    
    for line in lines[31612:]:
      
        print(line.split('/')[4])

        try:
            content = request.urlopen(line)
        
        except:
            continue

        f = open(baseFolder +line.split('/')[4] + '.jpg','wb')
        f.write(content.read())
        f.close()
        # with open(baseFolder +line.split('/')[4] + '.jpg', 'wb') as handle:
        #     print(line)
        #     #if is_url_image(line):
        #     response = requests.get(line, stream=True)
        #     if not response.ok:
        #         print(response)

        #     for block in response.iter_content():
        #         if not block:
        #             break
                
        #         handle.write(block)
        # b = os.path.getsize(baseFolder +line.split('/')[4] + '.jpg')
        # if b  == 0:
        #     os.remove(baseFolder +line.split('/')[4] + '.jpg')


 

    

if __name__ == '__main__':
    
    downloadImages()
    
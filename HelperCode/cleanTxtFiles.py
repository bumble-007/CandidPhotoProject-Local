import os 
import numpy as np 
import shutil

def removeTxtFiles(path):
    if not os.path.exists(path):
        print("Path doesn't Exist")
        return
    
    for folder in os.listdir(path):

        for files in os.listdir(path + folder):
            if ".txt" in files:
                try:
                     os.remove(path + folder+ "\\" + files)
                except OSError as err:
                    print("OS error: {0}".format(err))


if __name__ == "__main__":
    srcPath = "I:\\CandidPhotoProject\\Dataset\\"
    if os.path.exists(srcPath):
        print("Source Path doesn't exists")
        removeTxtFiles(srcPath)
    else:
        print("Source Path doesn't exists")


import os
import shutil


def createfolders(baseImagePath):

    i = 0
    for i in range(30):
        os.makedirs(baseImagePath + str(i))


def movefiles(baseImagePath):


    i = 0

    for file in os.listdir(baseImagePath):
        if '.jpg' in file:
            folder =  str(int ( i /1000))
            shutil.move(baseImagePath + file, baseImagePath +folder +"\\")
            i += 1



if __name__ == '__main__':
    srcDir = os.getcwd() + "\\"
    baseImagePath = srcDir + "Dataset\\data512x512\\data512x512\\"
    
    if os.path.exists(baseImagePath):
        #createfolders(baseImagePath)
        movefiles(baseImagePath)
    else:
        print("Path doesn't exists")
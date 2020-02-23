import os 
import numpy as np 
import csv 
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import shutil
#import pandas as pd 
import json
import cv2 as cv 

def analyseJson(jsonPath,metaDataPath, imgPath, absolute):
    print(jsonPath)
    #data = json.loads(srcPath)
   
    first = True
    nonCandid = []
    #for src in jsonPath:
    yawList = []
    pitchList = []
    rollList = []
    eyeGazeXList = []
    eyeGazeYList = []
    with open(jsonPath) as f:
        jsonDict = json.load(f)
    
    for key, value in jsonDict.items():
        #faces = len(value)
        for i in range(len(value.keys())):
            eyeGazeX = int(57.3 *(float(value[str(i)]['gaze_angle_x'])))
            eyeGazeY = int (57.3 *(float(value[str(i)]['gaze_angle_y'] ) ))
        
            pitch = int(float(value[str(i)]['pose_Rx']) * 57.3)
            yaw = int(float(value[str(i)]['pose_Ry']) * 57.3)
            roll = int (float(value[str(i)]['pose_Rz']) * 57.3)
            

            if abs(eyeGazeX) <= 5 and abs(eyeGazeY) <=  5 and abs(pitch) <= 5 and abs(yaw) <= 5:
                print(key)
                nonCandid.append(key)
            

    #print(nonCandid)
    
    print("Non Candid Filtering done")
    for file in nonCandid:
        imageName = file[:-4]+ ".jpg"
        if  os.path.exists(metaDataPath + file):
            shutil.move(metaDataPath + file, metaDataPath + "NonCandid\\")
        if  os.path.exists(imgPath + imageName):
            shutil.move(imgPath + imageName,imgPath + "NonCandid\\" )


       
         
def plotJsonData(jsonPath):
    def analyseJson(jsonPath,metaDataPath, imgPath, absolute):
        print(jsonPath)
    #data = json.loads(srcPath)
   
    first = True
    nonCandid = []
    for src in jsonPath:
        yawList = []
        pitchList = []
        rollList = []
        eyeGazeXList = []
        eyeGazeYList = []
        with open(src) as f:
            jsonDict = json.load(f)
        
        for key, value in jsonDict.items():
            #faces = len(value)
            for i in range(len(value.keys())):
                eyeGazeX = int(57.3 *(float(value[str(i)]['gaze_angle_x'])))
                eyeGazeY = int (57.3 *(float(value[str(i)]['gaze_angle_y'] ) ))
            
                pitch = int(float(value[str(i)]['pose_Rx']) * 57.3)
                yaw = int(float(value[str(i)]['pose_Ry']) * 57.3)
                roll = int (float(value[str(i)]['pose_Rz']) * 57.3)
             
                eyeGazeXList.append(np.abs(eyeGazeX))
                eyeGazeYList.append(np.abs(eyeGazeY))

                yawList.append(np.abs(yaw))
                pitchList.append(np.abs(pitch))
                rollList.append(np.abs(roll))
              


        
        fig = plt.figure()
        ax = fig.add_subplot(111)

        ax.hist(eyeGazeXList, ls='dashed', alpha = 0.5, lw=3,fc=(0, 0, 1, 0.5))
        ax.hist(eyeGazeYList, ls='dotted', alpha = 0.5, lw=3,fc=(1, 0, 0, 0.5))
        # #ax.hist(eyeGazeZList, bins=np.arange(0, 1, 0.1), alpha = 0.5, lw=3, fc=(0, 0, 1, 0.5))
    
        plt.show()

        # print(eyeGazeXList)
        # size = len(yawList)
        # axislist = np.arange(size)

        
        
        # plt.scatter(axislist, eyeGazeXList, color= 'b', marker = "o")
        # plt.scatter(axislist, eyeGazeYList, color= 'b', marker = "p")
        # plt.scatter(axislist,  yawList, color= 'b', marker = "*")
        # plt.scatter(axislist, pitchList, color= 'b', marker = "v")
        #plt.scatter(axislist, rollList, color= 'b' ,marker = "*")
        

        # plt.hist(eyeGazeXList,color = 'b')
  
       
    # plt.show()
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')

    # x =yawList
    # y =eyeGazeXList
    # z =axislist



    # ax.scatter(x, y, z, c='r', marker='o')

    # ax.set_xlabel('yawList')
    # ax.set_ylabel('eyeGazeXList')
    # ax.set_zlabel('axislist')

    # plt.show()
           
def writeValuesonImage(jsonPath, imgPath, dstPath):
    with open(jsonPath) as f:
        jsonDict = json.load(f)
    for files in os.listdir(imgPath):
        image = cv.imread(imgPath + str(files))
        if image is None:
            print("Image not found")
            continue
        
        value = jsonDict[str(files[:-4]) +".csv"]
        for i in range(len(value.keys())):
            eyeGazeX = abs(int(57.3 *(float(value[str(i)]['gaze_angle_x']))))
            eyeGazeY = abs(int (57.3 *(float(value[str(i)]['gaze_angle_y'] ) )))
            pitch = abs(int(float(value[str(i)]['pose_Rx']) * 57.3))
            yaw = abs(int(float(value[str(i)]['pose_Ry']) * 57.3))
           
            
            text =  [str(eyeGazeX), str(eyeGazeY), str(pitch), str(yaw)]
            org =  [(256, 256), (256, 276), (256, 296), (256, 316)]

            for j in range(len(text)):
                
                image = putText(image, org[j], text[j])
        
        cv.imwrite(dstPath + str(files), image)
        


   
def putText(image, org, text):
    font = cv.FONT_HERSHEY_SIMPLEX  
    # org 
   #org = (50, 50)    
    # fontScale 
    fontScale = 1
    # Blue color in BGR 
    color = (0, 0, 255)   
    # Line thickness of 2 px 
    thickness = 2   
    # Using cv2.putText() method 
    image = cv.putText(image, text, org, font,  
                    fontScale, color, thickness, cv.LINE_AA) 
    return image


if __name__ == "__main__":
    srcDir = os.getcwd() +"\\"
    jsonPath = srcDir +"processedData\\metaCelebA3.json"

    metaDataPath = srcDir + "metaData\\metaCelebA3\\"
    imgPath ="I:\\CandidPhotoProject\\Dataset\\data512x512\\data512x512\\2\\"
    dstPath = "I:\\CandidPhotoProject\\Analysis\\"
    # if os.path.exists(srcPath):
    #     print("Json exists")
    # else:
    #     print("Json doesn't exist")

    analyseJson(jsonPath, metaDataPath, imgPath, True)
    #plotJsonData(jsonPath)
    #writeValuesonImage(jsonPath, imgPath, dstPath)
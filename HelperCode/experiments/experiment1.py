import os
import shutil
import json
import numpy as np
import cv2 as cv 

def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::

            >>> angle_between((1, 0, 0), (0, 1, 0))
            1.5707963267948966
            >>> angle_between((1, 0, 0), (1, 0, 0))
            0.0
            >>> angle_between((1, 0, 0), (-1, 0, 0))
            3.141592653589793
    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

def analyseJsonFile(jsonPath, path):
    with open(jsonPath) as f:
        jsonDict = json.load(f)
    #print(jsonDict.keys())
    for filename in os.listdir(path):
        if ".csv" in filename:
            value = jsonDict[str(filename)]
            image = cv.imread(path + str(filename[:-4]) + ".jpg")
            for i in range(len(value.keys())):
                if (float(value[str(i)]['confidence'])) > 0.7:
                    gaze_0_x = abs (round((float(value[str(i)]['gaze_0_x']) * 57.3), 3))
                    gaze_0_y = abs(round ((float(value[str(i)]['gaze_0_y'])* 57.3), 3))
                    gaze_0_z = abs (round ((float(value[str(i)]['gaze_0_z'])* 57.3), 3))

                    gaze_1_x = abs (round((float(value[str(i)]['gaze_1_x'])* 57.3), 3))
                    gaze_1_y = abs (round( (float(value[str(i)]['gaze_1_y'])* 57.3), 3))
                    gaze_1_z = abs (round((float(value[str(i)]['gaze_1_z'])* 57.3), 3))

                    
                    angle = 57.3 *angle_between((gaze_0_x, gaze_0_y, gaze_0_z), (gaze_1_x, gaze_1_y, gaze_1_z))
                   
                    angle = round(angle, 3)
                    eyeGazeX =  (round((57.3 *(float(value[str(i)]['gaze_angle_x']))), 3))
                    eyeGazeY = (round( (57.3 *(float(value[str(i)]['gaze_angle_y']))), 3 ))
                    pitch =  abs (round((float(value[str(i)]['pose_Rx']) * 57.3), 3))
                    yaw =  abs (round((float(value[str(i)]['pose_Ry']) * 57.3), 3))
                  

                    # if abs(angle) <= 10:
                    #     shutil.move(path + filename, path + "\\NonCandid\\")
                    #     shutil.move(path + filename[:-4] + ".jpg" , path + "\\NonCandid\\")
                    # else:
                    #     shutil.move(path + filename, path + "\\Candid\\")
                    #     shutil.move(path + filename[:-4] + ".jpg", path + "\\Candid\\")

                    #print(str(filename) +" "+ str(angle))
                    diffx0 =  round((pitch - gaze_0_x), 3)
                    diffy0= round(( yaw - gaze_0_y),3)

                    diffx1 =  round((pitch - gaze_1_x), 3)
                    diffy1 = round(( yaw - gaze_1_y),3)

                    # diffx0 =  round((gaze_0_x), 3)
                    # diffy0= round(( gaze_0_y),3)

                    # diffx1 =  round(( gaze_1_x), 3)
                    # diffy1 = round(( gaze_1_y),3)


                    # text =  ["Ex : " + str(eyeGazeX), "Pitch : " +str(pitch),  "Yaw : " + str(yaw) ,"Ey : " + str(eyeGazeY),  " X0: " + str(diffx0), " Y0: " + str(diffy0) ,  " X1: " + str(diffx1), " Y1: " + str(diffy1) ]

                    text =  [ "Pitch : " +str( (pitch)),  " Diff_X0: " + str((diffx0)),  " Diff_X1: " + str((diffx1)), "Yaw : " + str((yaw)) , " Diff_Y0: " + str((diffy0)), " Diff_Y1: " + str((diffy1)), "X0: " + str(gaze_0_x) , "X1: " + str(gaze_1_x), "Y0: " + str(gaze_0_y) , "Y1: " + str(gaze_1_y) ]

                    # text =  [ "Pitch : " +str( (pitch)),  " Diff_X0: " + str((diffx0)),  " Diff_X1: " + str((diffx1)), "Yaw : " + str((yaw)) , " Diff_Y0: " + str((diffy0)), " Diff_Y1: " + str((diffy1)) ]


                    x = 80
                    org =  [(x, x)  , (x, x + 40)  , (x, x + 80) , (x, x + 120) , (x, x+ 160), (x , x + 200), ( x, x + 240), (x, x + 280) , ( x , x + 320), (x , x + 360)] 
                    

                    # text = [" X: " + str(diffx), " Y: " + str(diffy)]
                    # org = [(x , x), (x , x + 60)]

                    for j in range(len(text)):

                         image = putText(image, org[j], text[j])
                    
                    cv.imwrite(path+ "Results\\" +str(filename[:-4]) + ".jpg", image)
        
                else:
                    print(str(filename) +" rejected because of confidence "  + str(float(value[str(i)]['confidence'])))


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

def copyCSVfiles(csvfilePath, dstPath):
   
    for filename in os.listdir(dstPath):
        if ".jpg" in filename:
            csvfilename = filename[:-4] + "_1.csv"
            
            if os.path.exists(csvfilePath+ csvfilename):
                shutil.copy(csvfilePath+ csvfilename, dstPath)
            else:
                print("No csv in csvfilePath")

def removeLabel(metaDataPath):

    for filename in os.listdir(metaDataPath):
        if '.csv' in filename:
            os.rename(metaDataPath + str(filename),metaDataPath + str(filename[:-6]) +".csv")

if __name__ == '__main__':
    
    csvfilePath = "I:\\CandidPhotoProject\\metaData\\Candid-FHR\\"
    metaDataPath = "I:\\CandidPhotoProject\\metaData\\metaCelebA0\\NonCandid\\"


    dstPath = "I:\\CandidPhotoProject\\Analysis\\Exp2\\1\\"
    jsonPath = "I:\\CandidPhotoProject\\processedData\\metaCelebA1.json"


    if os.path.exists(csvfilePath) and os.path.exists(dstPath):
        #copyCSVfiles(csvfilePath, dstPath)
        #removeLabel(metaDataPath)
        analyseJsonFile(jsonPath, dstPath)
    else:
        print("Path doesn't exists")

    
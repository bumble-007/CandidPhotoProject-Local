import os
import cv2 




def extractframes(videoPath, imagesPath):
    cap = cv2.VideoCapture(videoPath)
    
    # Check if camera opened successfully
    if (cap.isOpened()== False): 
        print("Error opening video stream or file")
    
    # Read until video is completed
    i = 0
    while(cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()    
        # Display the resulting frame
        if ret == True:
            if i % 10 == 0:
                frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
               
                cv2.imwrite(imagesPath +'NotCandid-LR' + str(i) + ".jpg",frame)
            i += 1
        else:
            break


if __name__ == '__main__':
    srcDir = os.getcwd() +"\\"
    videoPath = srcDir + "Dataset\\Videos\\NotCandid-LR.mp4"
    imagesPath =srcDir + "Dataset\\Images\\NotCandid-LR\\"

    if os.path.exists(videoPath) and os.path.exists(imagesPath):
        extractframes(videoPath, imagesPath)
    else:
        print("Path doesn't exists")
    
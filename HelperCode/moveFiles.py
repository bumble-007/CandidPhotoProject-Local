import os
import shutil

def moveFiles( fileList, srcPath, dstPath):

    for file in fileList:
        if os.path.exists(srcPath + file):
            shutil.move(srcPath + file, dstPath)
        else:
            print("File doesn't exists")

    
if __name__ == '__main__':
    srcPath = "I:\\CandidPhotoProject\\Dataset\\data512x512\\data512x512\\0\\NonCandid\\"
    dstPath = "I:\\CandidPhotoProject\\Dataset\\data512x512\\data512x512\\0\\NonCandid\\False"
    if not os.path.exists(dstPath):
        os.makedirs(dstPath)
    fileNumber = [130, 200, 213,252,258,297,315,405,425,454,563,644,722,763,792, 58,252]
    fileNameList = []
    prefix = ["","0", "00", "000", "0000"]
    for filename in fileNumber:
        length =  len(str(filename))
        #print(length)
        fileNameList.append(prefix[5 -length] + str(filename)+ ".jpg")

    print(fileNameList)
    if os.path.exists(srcPath) and len(fileNameList) > 0:
        moveFiles(fileNameList,srcPath, dstPath)
    
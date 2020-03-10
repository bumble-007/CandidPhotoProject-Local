import os
import json
import shutil
import csv
import pandas as pd


def parseCSVfiles(path, processedDataPath):
    count = 0
    if os.path.exists(path):
        print(str(count) + " / 27906")
        combineJson = {}
        for filename in os.listdir(path):
            if ".csv" in filename:
                print(path + filename)
                with open(path + filename) as csvfile:
                    csvReader = csv.DictReader(csvfile, skipinitialspace= True)
                    faceDict = {}
                    count = 0
                    for rows in csvReader:
                        faceDict[str(count)] = rows
                        count+=1
                        #print(rows)
                combineJson[str(filename)] = faceDict
        
        with open(processedDataPath, 'w') as jsonfile:
            jsonfile.write(json.dumps(combineJson, indent = 4))
    else:
        print("Path doesn't exist")


def concatcsvfiles(imgPath, metaDataPath):
   
    dfList = []
    for imgName in os.listdir(imgPath):
        if ".jpg" in imgName:
            csvName = imgName[:-4] + ".csv"
            if os.path.exists(metaDataPath + csvName):
                print(csvName)
                df = pd.read_csv(metaDataPath + csvName, skipinitialspace = True)
                df.insert(0, "imgName", imgName )
                dfList.append(df)

    frame = pd.concat(dfList)
    frame.to_csv('train_NonCandid.csv') 


            

if __name__ == "__main__":
    srcDir = os.getcwd() +"\\"
    srcPath = "I:\\CandidPhotoProject\\Analysis\\Exp2\\Candid-FHR\\"
    processedDataPath = srcDir + "processedData\\" + 'candid_0.json'
    print(srcPath)
    # if os.path.exists(srcPath):
    #     parseCSVfiles(srcPath, processedDataPath)
    imgPath = srcDir + "Dataset\\data512x512\\data512x512\\Train\\combined\\NonCandid\\"
    metaDataPath = srcDir + "metaData\\metaCelebA3\\data\\"
    concatcsvfiles(imgPath, metaDataPath)
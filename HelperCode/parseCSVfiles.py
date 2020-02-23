import os
import json
import shutil
import csv


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

              
if __name__ == "__main__":
    srcDir = os.getcwd() +"\\"
    srcPath = "I:\\CandidPhotoProject\\Analysis\\Exp2\\Candid-FHR\\"
    processedDataPath = srcDir + "processedData\\" + 'exp2_C_FHR.json'
    print(srcPath)
    if os.path.exists(srcPath):
        parseCSVfiles(srcPath, processedDataPath)
import os


def changeNames(srcFolderPath, label):

    for files in os.listdir(srcFolderPath):
        if ".csv" in files:
            os.rename(srcFolderPath + files, srcFolderPath + files[:-4] + label)




if __name__ == '__main__':
    
    srcDir = os.getcwd() + "\\"
    folderPath = srcDir + "metaData\\metaCelebA0\\NonCandid\\"
    label = "_0.csv "

    if os.path.exists(folderPath):
        changeNames(folderPath, label)
    else:
        print("Folder doesn't exist")

    
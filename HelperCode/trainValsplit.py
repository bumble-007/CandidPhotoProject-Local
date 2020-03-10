import os
import shutil
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np 



def train_val_split(csvPath):
    cols = ["imgName", "gaze_0_x","gaze_0_y", "gaze_0_z","gaze_1_x","gaze_1_y", "gaze_1_z", "pose_Rx" ,"pose_Ry", "pose_Rz" ]
    df = pd.read_csv(csvPath, skipinitialspace = True, usecols = cols)
    print(df.head())
    y = np.ones(len(df))
    X_train, X_test, y_train, y_test = train_test_split(df, y, test_size = 0.2, random_state = 123)

    print(X_train.shape)
    print(X_test.shape)

  
    X_train['train_or_test'] = 1
    X_test['train_or_test'] = 0

    concat_df = pd.concat([X_train, X_test],axis = 0 )
    imgName = concat_df
    concat_df = concat_df.drop(columns=['imgName'])
    y = concat_df.pop('train_or_test')

    randomForest = RandomForestClassifier(n_estimators=500, random_state= 123)
    randomForest.fit(concat_df, y)

    y_pred = randomForest.predict(concat_df)
    
    score = cross_val_score(randomForest, concat_df, y  , cv = 5, scoring = 'roc_auc')
    print(score)

    #print(concat_df)

    X_train.to_csv('trainset_NonCandid.csv')
    X_test.to_csv('valset_NonCandid.csv')


def moveImages(imgPath, csvPath, dstPath):

    df = pd.read_csv(csvPath, usecols = ['imgName'])

    for index, row in df.iterrows():
        imgName = str(row['imgName'])
        if os.path.exists(imgPath + imgName):
            shutil.copy(imgPath + imgName, dstPath)

        
if __name__ == '__main__':
 
    csvPath = "trainset_NonCandid.csv"
    #train_val_split(csvPath)
    imgPath = "I:\\CandidPhotoProject\\Dataset\\data512x512\\data512x512\\Train\\combined\\NonCandid\\"
    dstPath = "I:\\CandidPhotoProject\\Dataset\\data512x512\\data512x512\\Train\\dataset\\train\\nonCandid\\"
    moveImages(imgPath, csvPath, dstPath)

    
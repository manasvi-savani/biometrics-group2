import get_images
import get_landmarks
import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB

datasets = ['./images/N_Patel']
num_landmarks = [5, 68]

labels_correct = []
labels_incorrect = []

for dataset in datasets:
                
    for num_landmark in num_landmarks:
        
        image_directory = dataset
        X, y, fileNames = get_images.get_images(image_directory)
        if num_landmark == 5:
            X, y, fileNames = get_landmarks.get_landmarks(X, y, fileNames, 'landmarks_N_Patel/5/', num_landmark, True)
        else:
            X, y, fileNames = get_landmarks.get_landmarks(X, y, fileNames, 'landmarks_N_Patel/68/', num_landmark, True)         
        print("Dataset: %s | No. Landmarks: %d " % (dataset, num_landmark))

        nb = GaussianNB()
        num_correct = 0
        num_incorrect = 0
        
        for i in range(0, len(y)):
            query_img = X[i, :]
            query_label = y[i]
            
            template_imgs = np.delete(X, i, 0)
            template_labels = np.delete(y, i)                            
          
            y_hat = np.zeros(len(template_labels))
            y_hat[template_labels == query_label] = 1 
            y_hat[template_labels != query_label] = 0
            
            nb.fit(template_imgs, y_hat) 
            y_pred = nb.predict(query_img.reshape(1,-1)) 
            
            if y_pred == 1:
                num_correct += 1
                labels_correct.append(fileNames[i])
            else:
                num_incorrect += 1
                labels_incorrect.append(fileNames[i])
        
        print("Num correct = %d, Num incorrect = %d, Accuracy = %0.2f" 
              % (num_correct, num_incorrect, num_correct/(num_correct+num_incorrect)))    
        print('--------------------------------')
                
labels_correct = pd.Series(labels_correct).value_counts()
labels_incorrect = pd.Series(labels_incorrect).value_counts()
    
print("Commonly predicted correctly:")
print(labels_correct.head())
print("------------------------------------")
print("Commonly predicted incorrectly:")
print(labels_incorrect.head())
import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import fetch_olivetti_faces
from sklearn.model_selection import train_test_split 

width = 64
dataset = fetch_olivetti_faces(shuffle = True)

train_data,test_data = train_test_split(dataset,train_size = 0.7,random_state=10)

faces = train_data.data

n_samples, n_features = faces.shape
print("Dataset consists of %d faces" % n_samples)

plt.figure()
plt.imshow(faces[0].reshape((width,width)), cmap = 'gray')

#squash it
faces = faces.transpose() #each column is a squashed face

#get the mean face
mean_face = faces.mean(axis = 1)
plt.figure()
plt.imshow(mean_face.reshape((width,width)), cmap = 'gray')

#subtract the mean face -center everybody
for col in range(faces.shape[1]):
    faces[:,col] = faces[:, col] - mean_face
    
plt.figure()
plt.imshow(faces[:, 0].reshape((width,width)), cmap = 'gray')

#compute the covariance matrix, c
C = np.cov(faces.transpose())

#get the eigenfaces from c
evals, evecs = np.linalg.eig(C)

#show some eigenfaces 
eigenfaces = np.dot(faces, evecs)
plt.figure()
plt.subplot(131)
plt.imshow(eigenfaces[:, 0].reshape((width,width)), cmap = 'gray')
plt.subplot(132)
plt.imshow(eigenfaces[:, 1].reshape((width,width)), cmap = 'gray')
plt.subplot(133)
plt.imshow(eigenfaces[:, 2].reshape((width,width)), cmap = 'gray')
'''
#can we reconstruct the face
k = 20
face1 = np.zeros(width**2)
for i in range(k):
    face1 += eigenfaces[:,i].transpose() * faces[:,0] * eigenfaces[:,i]
plt.figure()
plt.imshow(face1.reshape((width,width)), cmap = 'gray')

#what do the features look like?
face_features = np.zeros((faces.shape[1], k))
for i in range(faces.shape[1]):
    face = faces[:,i]
    for j in range(k):
        face_features[i,j] = np.dot(eigenfaces[:,j].transpose(), face)
   '''     


    
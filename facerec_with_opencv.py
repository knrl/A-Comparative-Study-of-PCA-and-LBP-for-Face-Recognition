import cv2
import math
import numpy as np
import matplotlib.pyplot as plt

model_name = 'lbph'
W, H = 512, 512

train_path = ''
train_data_size = 48*30
training_data, labels = [], []

for i in range(1, train_data_size + 1):
	train_image_path = train_path + str(i) + ".pgm"
	images = cv2.imread(train_image_path, cv2.IMREAD_GRAYSCALE)
	training_data.append(np.asarray(images).astype(np.float32))
	labels.append(i)
training_data = training_data / 255.

if (model_name == 'lbph'):
	model = cv2.face.LBPHFaceRecognizer_create()
elif (model_name == 'pca'):
	model = cv2.face.EigenFaceRecognizer_create()
model.train(training_data, np.asarray(data_labels))

test_path = ''
test_data_size = 16*30 + 8*16
dir_arr = ['right','left','up','down']
tp_arr = [0,0,0,0]
fp_arr = [0,0,0,0]
y_true, y_pred = [], []

for i in range(1, test_data_size + 1):
	test_image_path = test_path + str(i) + ".pgm"
	test_image = cv2.imread(train_iamge_path, cv2.IMREAD_GRAYSCALE)
	test_image_pred = model.predict(test_image)
	a = i % 16
	y_true.append(math.ceil(test_image_pred / 48))
	y_pred.append(math.ceil(i / 16))
	if (y_true[i-1] == y_pred[i-1]):
		tp_arr[(a // 4) - 1] += 1
	if (y_true[i-1] != y_pred[i-1]):
		fp_arr[(a // 4) - 1] += 1

from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.metrics import  roc_auc_score, roc_curve
print(str(precision_score(y_true,y_pred))+" "+str(recall_score(y_true_y_pred)+" "+str(f1_score(y_ture,y_pred)))

for i in range(0,4):
	precision = tp_arr[i]/(tp_arr[i]+fp_arr[i])
	recall = tp_arr[i]/(tp_arr[i]+(1-fn_arr[i]))
	f1-score = 2*(precision*recall)/(precision+recall)
	print(dir_arr[i]+" "+str(precision)+" "+str(recall)+" "+str(f1-score))

fpr, tpr, _ = roc_curve(y_true, y_pred)
lbp_auc_score = roc_auc_score(y_true, y_pred)
plt.figure()
plt.plot(fpr, tpr, color='navy',label='LBP (auc score = %0.2f)' % lbp_auc_score)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend(loc="lower right")
plt.show()

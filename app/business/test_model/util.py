import torch
import torch.nn as nn
import os
import cv2
import numpy as np
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from sklearn.metrics import confusion_matrix
from tqdm.notebook import tqdm


def get_data(data_dir):
  labels = ['wrong', 'correct']
  img_size = 150

  x = []
  y = []
  for label in labels:
    path = os.path.join(data_dir, label)
    class_num = labels.index(label)
    for img in os.listdir(path):
      try:
        img_arr = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
        resized_arr = cv2.resize(img_arr, (img_size, img_size))  # Reshaping images to preferred size
        resized_arr = resized_arr / 255
        x.append([resized_arr])
        y.append([int(class_num)])
      except Exception as e:
        print(e)

  return np.array(x), np.array(y)



class TestDataset():
  def __init__(self, test_x, test_y):
    self.test_x = test_x
    self.test_y = test_y

  # 총 데이터의 개수를 리턴
  def __len__(self):
    return len(self.test_x)

  # 인덱스를 입력받아 그에 맵핑되는 입출력 데이터를 파이토치의 Tensor 형태로 리턴
  def __getitem__(self, idx):
    x = torch.FloatTensor(self.test_x[idx])
    y = torch.LongTensor(self.test_y[idx])
    y = y.squeeze()
    return x, y




def get_model_performance(data_loader, vmi_num):
  total_score = {'try': [], 'acc': [], 'recall': [], 'precision': [], 'f1_score': []}

  device = 'cpu'

  model = torch.load(f'./business/predict_image/learning_model/no{vmi_num}_Pytorch_EfficientNet.pth')
  model = model.to(device)
  model.eval()

  y_pred = []
  y_real = []

  # iterate over test data
  try_num = 1
  for inputs, labels in tqdm(data_loader):
    inputs = inputs.to(device)
    labels = labels.to(device)

    outputs = model(inputs)  # Feed Network
    _, pred = torch.max(outputs.data, 1)

    batch_size = len(labels)
    score = torch.sum(pred.to(device) == labels.to(device))

    pred = [i.item() for i in pred]

    labels = list(labels)
    labels = [i.item() for i in labels]

    y_pred.extend(pred)  # Save Prediction
    y_real.extend(labels)  # Save Truth

    # constant for classes
    classes = ('wrong', 'correct')

    # Build confusion matrix
    cf_matrix = confusion_matrix(y_real, y_pred)

    one_acc = round((score / batch_size).item(), 5)

    one_recall = cf_matrix[1][1] / (cf_matrix[1][1] + cf_matrix[1][0])
    one_recall = round(one_recall, 5)

    one_precision = cf_matrix[1][1] / (cf_matrix[0][1] + cf_matrix[1][1])
    one_precision = round(one_precision, 5)

    one_f1_score = 2 * (one_precision * one_recall) / (one_precision + one_recall)
    one_f1_score = round(one_f1_score, 5)

    total_score['try'].append(try_num)
    total_score['acc'].append(one_acc)
    total_score['recall'].append(one_recall)
    total_score['precision'].append(one_precision)
    total_score['f1_score'].append(one_f1_score)

    try_num += 1
  return total_score

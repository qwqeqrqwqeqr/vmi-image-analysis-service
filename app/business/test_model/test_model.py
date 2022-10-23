from datetime import datetime

from torch.utils.data import DataLoader

from business.test_model.util import get_data, TestDataset, get_model_performance


def get_average_performance_from_model():
  performance_list = []
  for i in range(4,5):
    performance_list.append(test_model(i))

  average_performance = calculate_average(performance_list)

  print("종합 성능지표 accuracy : ", average_performance[0], " recall : ", average_performance[1], " precision : ",
        average_performance[2], " f1_score : ",
        average_performance[3])

  return average_performance


def calculate_average(performance_list):
  total_accuracy = 0
  total_recall = 0
  total_precision = 0
  total_f1_score = 0

  for p in performance_list:
      total_accuracy += p[0]
      total_recall += p[1]
      total_precision += p[2]
      total_f1_score += p[3]

  avg_accuracy = total_accuracy / len(performance_list)
  avg_recall = total_recall / len(performance_list)
  avg_precision = total_precision / len(performance_list)
  avg_f1_score = total_f1_score / len(performance_list)

  now = datetime.now()
  f = open('./log.txt', 'a')
  f.write("[%s] 전체 성능지표 accuracy :  %lf   recall : %lf  precision :  %lf  f1_score : %lf\n" %(now,avg_accuracy,avg_recall,avg_precision,avg_f1_score))
  f.close()

  return avg_accuracy, avg_recall, avg_precision, avg_f1_score


def test_model(number):
  test_x, test_y = get_data(f'./data_set/no_{number}/test')
  test_dataset = TestDataset(test_x, test_y)
  test_dataloader = DataLoader(test_dataset, batch_size=16,
                               shuffle=True, drop_last=True)

  result = get_model_performance(test_dataloader, number)

  accuracy = sum(result["acc"]) / len(result["acc"])
  recall = sum(result["recall"]) / len(result["recall"])
  precision = sum(result["precision"]) / len(result["precision"])
  f1_score = sum(result["f1_score"]) / len(result["f1_score"])




  print(number, "번 모델의 성능지표 accuracy : ", accuracy, " recall : ", recall, " precision : ", precision, " f1_score : ",
        f1_score)

  now = datetime.now()
  f = open('./log.txt', 'a')
  f.write("[%s] %d번 모델의 성능지표 accuracy :  %lf   recall : %lf  precision :  %lf  f1_score : %lf\n" %(now,number,accuracy,recall,precision,f1_score))
  f.close()
  return accuracy, recall, precision, f1_score

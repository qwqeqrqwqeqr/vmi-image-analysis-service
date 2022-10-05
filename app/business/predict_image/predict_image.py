from business.predict_image.predict.predict import predict
from model.evaluation import Evaluation

'''
    1번부터 9번 예측 미적용
    22번부터 30번 현재 gan 작업 중 
'''


def predict_image(image, evaluation_list):
    evaluation_list[10] = map_result(10,
                                     predict(image.a_10, f"./ai/predict/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[11] = map_result(11,
                                     predict(image.a_11, f"./ai/predict/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[12] = map_result(12,
                                     predict(image.a_12, f"./ai/predict/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[13] = map_result(13,
                                     predict(image.a_13, f"./ai/predict/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[14] = map_result(14,
                                     predict(image.a_14, f"./ai/predict/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[15] = map_result(15,
                                     predict(image.a_15, f"./ai/predict/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[16] = map_result(16,
                                     predict(image.a_16, f"./ai/predict/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[17] = map_result(17,
                                     predict(image.a_17, f"./ai/predict/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[18] = map_result(18,
                                     predict(image.a_18, f"./ai/predict/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[19] = map_result(19,
                                     predict(image.a_19, f"./ai/predict/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[20] = map_result(20,
                                     predict(image.a_20, f"./ai/predict/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[21] = map_result(21,
                                     predict(image.a_21, f"./ai/predict/learning_model/predict_10_cnn_model.h5"))

    return evaluation_list


def map_result(number, result):
    return Evaluation(number, result[0], result[1])

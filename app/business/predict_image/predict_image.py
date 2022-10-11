from business.analysis_image.analysis_image import map_result
from business.predict_image.predict.predict import predict
from model.evaluation import Evaluation

'''
    1번부터 9번 예측 미적용
    22번부터 30번 현재 gan 작업 중 
'''


# TODO 모델 경로 constants 제작 및 경로 할당
def predict_image(image, evaluation_list):
    evaluation_list[0] = map_result(4,
                                    predict(image.a_4,
                                            f"./business/predict_image/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[1] = map_result(5,
                                    predict(image.a_5,
                                            f"./business/predict_image/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[2] = map_result(6,
                                    predict(image.a_6,
                                            f"./business/predict_image/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[3] = map_result(7,
                                     predict(image.a_7,
                                             f"./business/predict_image/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[4] = map_result(8,
                                     predict(image.a_8,
                                             f"./business/predict_image/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[5] = map_result(9,
                                     predict(image.a_9,
                                             f"./business/predict_image/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[6] = map_result(10,
                                     predict(image.a_10,
                                             f"./business/predict_image/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[7] = map_result(11,
                                     predict(image.a_11,
                                             f"./business/predict_image/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[8] = map_result(12,
                                     predict(image.a_12,
                                             f"./business/predict_image/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[9] = map_result(13,
                                     predict(image.a_13,
                                             f"./business/predict_image/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[10] = map_result(14,
                                     predict(image.a_14,
                                             f"./business/predict_image/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[11] = map_result(15,
                                     predict(image.a_15,
                                             f"./business/predict_image/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[12] = map_result(16,
                                     predict(image.a_16,
                                             f"./business/predict_image/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[13] = map_result(17,
                                     predict(image.a_17,
                                             f"./business/predict_image/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[14] = map_result(18,
                                     predict(image.a_18,
                                             f"./business/predict_image/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[15] = map_result(19,
                                     predict(image.a_19,
                                             f"./business/predict_image/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[16] = map_result(20,
                                     predict(image.a_20,
                                             f"./business/predict_image/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[17] = map_result(21,
                                     predict(image.a_21,
                                             f"./business/predict_image/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[18] = map_result(22,
                                     predict(image.a_22,
                                             f"./business/predict_image/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[19] = map_result(23,
                                     predict(image.a_23,
                                             f"./business/predict_image/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[20] = map_result(24,
                                     predict(image.a_24,
                                             f"./business/predict_image/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[21] = map_result(25,
                                     predict(image.a_25,
                                             f"./business/predict_image/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[22] = map_result(26,
                                     predict(image.a_26,
                                             f"./business/predict_image/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[23] = map_result(27,
                                     predict(image.a_27,
                                             f"./business/predict_image/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[24] = map_result(28,
                                     predict(image.a_28,
                                             f"./business/predict_image/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[25] = map_result(29,
                                     predict(image.a_29,
                                             f"./business/predict_image/learning_model/predict_10_cnn_model.h5"))
    evaluation_list[26] = map_result(30,
                                     predict(image.a_30,
                                             f"./business/predict_image/learning_model/predict_10_cnn_model.h5"))

    return evaluation_list

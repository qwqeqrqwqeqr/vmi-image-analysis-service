from analysis.predict.predict import predict


def map_predict(number, image_path):
    if number == 10:  # 10번 일 때
        return predict(image_path,f"./ai/predict/learning_model/predict_10_cnn_model.h5")
    else:
        return predict(image_path,f"./ai/predict/learning_model/predict_16_cnn_model.h5")

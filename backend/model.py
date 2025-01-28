import pickle
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), '../models')

# Tải model đã huấn luyện
def load_model(model_name):
    model_file = f"{MODEL_PATH}/{model_name}.pkl"
    with open(model_file, 'rb') as file:
        model = pickle.load(file)
    return model

# Dự đoán xu hướng
def predict_trends(model, data):
    return model.predict(data)

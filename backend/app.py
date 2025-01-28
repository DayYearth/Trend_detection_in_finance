from flask import Flask, request, jsonify
import pandas as pd
from model import load_model, predict_trends
from preprocess import preprocess_data

app = Flask(__name__)

# Route để kiểm tra API hoạt động
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "Server is running"}), 200

@app.route('/upload_raw', methods=['POST'])
def upload_raw():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']

    try:
        # Đọc dữ liệu raw từ file
        data = pd.read_csv(file)

        # Trả về dữ liệu đã xử lý cơ bản (nếu cần)
        return jsonify({"message": "Raw data uploaded successfully", "data_preview": data.head(5).to_dict()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route để tải file CSV lên và dự đoán
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    model_name = request.form.get('model', 'random_forest')

    try:
        # Đọc và xử lý dữ liệu
        data = pd.read_csv(file)
        processed_data = preprocess_data(data)

        # Tải model và dự đoán
        model = load_model(model_name)
        predictions = predict_trends(model, processed_data)

        return jsonify({"predictions": predictions.tolist()}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

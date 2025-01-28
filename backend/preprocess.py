def preprocess_data(data):
    """
    Xử lý dữ liệu đầu vào từ file CSV raw.
    """
    # Kiểm tra các cột cần thiết
    required_columns = ['open', 'high', 'low', 'close', 'volume']
    for col in required_columns:
        if col not in data.columns:
            raise ValueError(f"Missing required column: {col}")

    # Xử lý NaN
    data = data.dropna()

    # Thêm các cột tính toán cần thiết
    data['MA_20'] = data['close'].rolling(window=20).mean()
    data['MA_50'] = data['close'].rolling(window=50).mean()
    data['Log_Return'] = data['close'].pct_change()
    data['Volatility'] = data['Log_Return'].rolling(window=20).std()

    # Xóa các hàng chứa giá trị NaN sau khi tính toán
    data.dropna(inplace=True)

    # Trả về dữ liệu đã xử lý
    return data[['open', 'high', 'low', 'close', 'volume', 'MA_20', 'MA_50', 'Volatility']]

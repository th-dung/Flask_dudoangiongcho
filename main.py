# A very simple Flask Hello World app for you to get started with...
from flask import Flask, render_template, request
from keras.models import load_model
from keras.applications.inception_v3 import decode_predictions
from flask import Flask, render_template, jsonify
import webbrowser as wb
import cv2
import numpy as np

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    LoadModel()
    return render_template('index.html')

@app.route('/', methods=['POST'])
def predict():
    # get image
    image = request.files['images_input']
    if image.filename != '':
        # Đọc ảnh thành bytes
        dataBytes = image.read()
        # Chuyển bytes thành numpy
        arrayFlatten = np.frombuffer(dataBytes, dtype=np.uint8)
        img = cv2.imdecode(arrayFlatten, cv2.IMREAD_COLOR)

        # Chuyển hệ màu BGR - RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Chuẩn hóa normalize
        img = cv2.normalize(img, None, alpha=0, beta=1,norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
        # Resize ảnh về 299,299
        # img = cv2.resize(img, (299, 299))
        img = cv2.resize(img, (224, 224))
        # Mở rộng shape thứ 0
        img = np.expand_dims(img, axis=0)
        # Dự đoán
        preds = model.predict(img)

        # Top
        top = 2
        # Giải mã các dự đoán
        decoded_preds = decode_predictions(preds, top=top)[0]

        # In kết quả dự đoán
        result = ''
        for _, prediction_name, prediction_weight in decoded_preds:
            result += f'{prediction_name}: {prediction_weight}<br>'
            # result_name = f'{prediction_name}'
            google_search(prediction_name)
        return render_template('index.html', result=result)
    
    else:
        message = "Hình ảnh chưa được tải lên"
        return render_template('index.html', message=message)

def google_search(preprediction_name):
	search = preprediction_name.lower()
	url = f'https://www.google.com/search?q={search}'
	wb.get().open(url, new=2)

def LoadModel():
    global model
    # model = load_model('inceptionv3.h5')
    model = load_model('googlenet_dogbreed.h5')
    # model = load_model('weights.h5')

if __name__ == '__main__':
    app.run(debug=True)

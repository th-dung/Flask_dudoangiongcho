from flask import Flask, render_template, send_file

app = Flask(__name__)

# Route hiển thị trang web chứa hình ảnh
@app.route('/')
def home():
    return render_template('test.html')

# Route để trả về hình ảnh từ máy chủ
@app.route('/image')
def get_image():
    # Đường dẫn tới hình ảnh trên máy chủ
    image_path = 'Downloads/dog1.jpg'
    # Trả về hình ảnh
    return send_file(image_path, mimetype='image/jpg')

if __name__ == '__main__':
    app.run(debug=True)

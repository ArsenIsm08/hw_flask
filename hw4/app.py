from flask import Flask, render_template, request, redirect, url_for
import os
import requests
from io import BytesIO

app = Flask(__name__)

# Папка для сохранения загруженных изображений
UPLOAD_FOLDER = 'uploaded_images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    url = request.form.get('url')

    if not url:
        return redirect(url_for('index'))

    try:
        response = requests.get(url)
        if response.status_code == 200:
            image = BytesIO(response.content)
            image_name = url.split("/")[-1]
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_name)
            with open(image_path, 'wb') as file:
                file.write(image.getvalue())
            return render_template('result.html', image_path=image_path)
        else:
            return render_template('error.html', message='Failed to fetch image from URL')
    except Exception as e:
        return render_template('error.html', message=str(e))

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)

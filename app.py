from flask import Flask, render_template, request, redirect, url_for, send_file
import os
import uuid
from werkzeug.utils import secure_filename
import cv2
import numpy as np
import pytesseract
import easyocr
import pandas as pd

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXT = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
reader = easyocr.Reader(['en','hi'], gpu=False) # set gpu=True if available
def allowed_file(filename):
return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXT
def preprocess_image(path):
# read in grayscale
img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# denoise
denoised = cv2.fastNlMeansDenoising(gray, None, 10, 7, 21)
# adaptive threshold
th = cv2.adaptiveThreshold(denoised, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
cv2.THRESH_BINARY, 15, 8)
# optional: morphological ops to connect strokes
kernel = np.ones((1,1), np.uint8)
processed = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)
return processed
@app.route('/', methods=['GET', 'POST'])
def index():
if request.method == 'POST':
if 'image' not in request.files:
return redirect(request.url)
file = request.files['image']
if file.filename == '':
return redirect(request.url)
if file and allowed_file(file.filename):
filename = secure_filename(file.filename)
unique = f"{uuid.uuid4().hex}_{filename}"
path = os.path.join(app.config['UPLOAD_FOLDER'], unique)
file.save(path)
# preprocess
processed = preprocess_image(path)
proc_path = path + '_proc.png'
cv2.imwrite(proc_path, processed)
# First try EasyOCR (handwriting + printed)
try:
results = reader.readtext(proc_path)
# results: list of (bbox, text, conf)
texts = [r[1] for r in results]
except Exception as e:
print('EasyOCR failed:', e)
texts = []
# If results too empty, try pytesseract as fallback
if len(texts) < 1:
# use Tesseract with Hindi+English
config = '--psm 6'
try:
tess_text = pytesseract.image_to_string(proc_path,
lang='eng+hin', config=config)
# split lines
texts = [line.strip() for line in tess_text.splitlines() if
line.strip()]
except Exception as e:
print('Tesseract failed:', e)
# Make a simple table: each line becomes a row
df = pd.DataFrame({'line': texts})
csv_path = path + '.csv'
excel_path = path + '.xlsx'
df.to_csv(csv_path, index=False)
df.to_excel(excel_path, index=False)
# send to result template
return render_template('result.html', image_url='/' + proc_path,
lines=texts,
csv_file=csv_path, excel_file=excel_path)
return render_template('index.html')
@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
return send_file(filename)
@app.route('/download')
def download():
# example endpoint - not used in template
return send_file('example.csv', as_attachment=True)
if __name__ == '__main__':
app.run(debug=True)
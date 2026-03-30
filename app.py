from flask import Flask, jsonify, render_template, request
import json
import datetime
import random

app = Flask(__name__)

def load_data():
    try:
        with open('questions.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/questions')
def get_questions():
    data = load_data()
    # Xáo trộn câu hỏi để mỗi lần học là một trải nghiệm mới
    random.shuffle(data) 
    return jsonify(data)

@app.route('/api/save-score', methods=['POST'])
def save_score():
    req = request.json
    score = req.get('score')
    total = req.get('total')
    time_now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    # Ghi log kết quả vào file results.txt để theo dõi tiến độ
    with open('results.txt', 'a', encoding='utf-8') as f:
        f.write(f"[{time_now}] Điểm số: {score}/{total}\n")
    
    return jsonify({"status": "success", "message": "Đã lưu kết quả thành công!"})

@app.route('/api/get-history')
def get_history():
    try:
        with open('results.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            # Trả về 10 kết quả gần nhất
            return jsonify([line.strip() for line in lines[-10:]])
    except FileNotFoundError:
        return jsonify([])

if __name__ == '__main__':
    print("Ứng dụng học tiếng Anh đang chạy tại http://127.0.0.1:5000")
    app.run(debug=True)
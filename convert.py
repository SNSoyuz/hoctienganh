import json

def convert_txt_to_json(input_file, output_file):
    questions = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            parts = line.strip().split('|')
            if len(parts) >= 7:
                # Nếu có cột thứ 8 thì lấy, không thì để trống
                note = parts[7] if len(parts) > 7 else "Chưa có giải thích cho câu này."
                
                q = {
                    "id": i,
                    "level": parts[6],
                    "question": parts[0],
                    "options": [parts[2], parts[3], parts[4], parts[5]],
                    "answer": 0, 
                    "note": note
                }
                questions.append(q)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=4)

convert_txt_to_json('raw_data.txt', 'questions.json')
print("✅ Đã cập nhật questions.json kèm phần giải thích!")
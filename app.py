from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)
def get_ai_response(user_input: str) -> str:
    response = get_answer(user_input)
    answer = response["answer"]
    source = response["source"]

    return f"{answer} \n Source: {source}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = get_ai_response(user_input)
    return jsonify({'response': response})
    # return jsonify({'response': user_input})

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '' or not file.filename.lower().endswith('.txt'):
        return jsonify({'error': 'Invalid file format. Only .txt files are allowed.'}), 400


    file_content = file.read().decode('utf-8')
    file_name = file.filename

    doc = Document(page_content=file_content, metadata={"source": file_name})
    add_document(doc)

    return jsonify({'message': 'File content read successfully.', 'content': file_content, 'filename': file_name})

if __name__ == '__main__':
    app.run(debug=True)
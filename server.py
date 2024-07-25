from flask import Flask, request, jsonify
import os

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 * 1024  # 16 GB max size

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"message": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400
    if file:
        print(file)
        print(file.filename)
        file.save(f"{os.path.basename(file.filename)}")
        return jsonify({"message": "File successfully uploaded"}), 200

if __name__ == "__main__":
    app.run(debug=True)
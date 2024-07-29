from flask import Flask, request, jsonify,send_file
import os
import base64 

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 * 1024  # 16 GB max size

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"message": "No file part"}), 400
    print(request.files)
    file = request.files['file']
    print(file)
    print(file.read(1024))
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400
    if file:
        print(file)
        print(file.filename)
        file.save(f"{os.path.basename(file.filename)}")
        return jsonify({"message": "File successfully uploaded"}), 200
    
@app.route('/sentpdf', methods=['GET'])
def get_file():
    file_path = 'D00001_10000001.tiff'
    
    # Read and encode the file in Base64
    with open(file_path, 'rb') as file:
        encoded_file = base64.b64encode(file.read()).decode('utf-8')
    
    # Additional data
    additional_data = {
        'patient_name': 'John Doe',
        'age': 30,
        'gender': 'Male',
        'file_data': encoded_file
    }
    
    return jsonify(additional_data)

if __name__ == "__main__":
    app.run(debug=True)
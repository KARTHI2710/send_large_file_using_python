from flask import Flask, request, jsonify
import os

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 * 1024  # 16 GB max size

# Define the directory where files will be saved
save_directory = "uploads"
os.makedirs(save_directory, exist_ok=True)  # Create the directory if it doesn't exist

@app.route('/upload_chunk', methods=['POST'])
def upload_chunk():
    if 'file' not in request.files or 'chunk_index' not in request.form or 'total_chunks' not in request.form or 'filename' not in request.form:
        return jsonify({"message": "Missing parameters"}), 400
    
    file = request.files['file']
    chunk_index = int(request.form['chunk_index'])
    total_chunks = int(request.form['total_chunks'])
    filename = request.form['filename']
    
    save_path = os.path.join(save_directory, filename)
    
    try:
        # Append the chunk to the file
        with open(save_path, 'ab') as f:
            f.write(file.read())
        
        # Respond with the next chunk index needed
        if chunk_index + 1 == total_chunks:
            return jsonify({"message": "File successfully uploaded"}), 200
        else:
            return jsonify({"message": "Chunk successfully uploaded", "next_chunk_index": chunk_index + 1}), 200
    except Exception as e:
        print(f"Error saving file: {e}")
        return jsonify({"message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

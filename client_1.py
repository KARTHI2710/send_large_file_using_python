import requests
import os
import time

def upload_large_file(file_path, url, chunk_size=10 * 1024 * 1024):  # 10 MB chunks
    filename = os.path.basename(file_path)
    total_size = os.path.getsize(file_path)
    total_chunks = (total_size + chunk_size - 1) // chunk_size

    with open(file_path, 'rb') as f:
        chunk_index = 0
        while chunk_index < total_chunks:
            f.seek(chunk_index * chunk_size)
            chunk = f.read(chunk_size)
            files = {'file': (filename, chunk)}
            data = {'chunk_index': chunk_index, 'total_chunks': total_chunks, 'filename': filename}
            try:
                response = requests.post(url, files=files, data=data)
                response.raise_for_status()  # Raise an error for bad status codes
                json_response = response.json()
                if 'next_chunk_index' in json_response:
                    chunk_index = json_response['next_chunk_index']
                else:
                    chunk_index += 1
                print(f"Chunk {chunk_index}/{total_chunks} uploaded successfully.")
            except requests.exceptions.RequestException as e:
                print(f"Error: {e}. Retrying chunk {chunk_index}/{total_chunks}...")
                # Implement retry logic here if necessary, like exponential backoff
                time.sleep(10)
                continue

if __name__ == "__main__":
    file_path = r"D:\D00001_10000001.tiff"
    url = "http://127.0.0.1:5001/upload_chunk"  # Change this to the actual server URL
    upload_large_file(file_path, url)
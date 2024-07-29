import requests
import base64

def upload_large_file(file_path, url):
    with open(file_path, 'rb') as file:
        files = {'file': (file_path, file)}
        print(file)
        response = requests.post(url, files=files,stream=True)
    return response

def download_and_save_file(url, local_filename):
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        file_data = data['file_data']
        
        # Decode the Base64 string and save it as a file
        with open(local_filename, 'wb') as file:
            file.write(base64.b64decode(file_data))
        print(f"File downloaded and saved successfully: {local_filename}")
        
        # Print additional patient info
        print("Patient Information:", {
            'patient_name': data['patient_name'],
            'age': data['age'],
            'gender': data['gender'],
        })
    else:
        print(f"Failed to download file: Status code {response.status_code}")

if __name__ == "__main__":
    file_path = r"D:\D00001_10000001.tiff"
    url = "http://127.0.0.1:5000/upload"
    response = upload_large_file(file_path, url)
    print(response.status_code)
    print(response.json())

    # url = 'http://127.0.0.1:5000/sentpdf'
    # local_filename = 'downloaded_file.tiff'
    # download_and_save_file(url, local_filename)

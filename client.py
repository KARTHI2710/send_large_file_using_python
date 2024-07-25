import requests

def upload_large_file(file_path, url):
    with open(file_path, 'rb') as file:
        files = {'file': (file_path, file)}
        print(file)
        response = requests.post(url, files=files,stream=True)
    return response

if __name__ == "__main__":
    file_path = r"D:\D00001_10000001.tiff"
    url = "http://127.0.0.1:5001/upload"
    response = upload_large_file(file_path, url)
    print(response.status_code)
    print(response.json())
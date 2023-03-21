import os
import tempfile
import requests
import whisper
import azure.functions as func
from urllib.parse import quote



# def download_file(url):
#     print(f"Downloading file from URL: {url}")  # Add this line
#     local_filename = os.path.join(tempfile.gettempdir(), "temp_audio.mp3")
#     with requests.get(url, stream=True) as r:
#         print(f"Response status code: {r.status_code}")  # Add this line
#         r.raise_for_status()
#         with open(local_filename, 'wb') as f:
#             for chunk in r.iter_content(chunk_size=8192):
#                 f.write(chunk)
#     return local_filename

# def readurl():
#     full_url = req.url
#     print(f"Full URL: {full_url}")

    # # Get query string parameters
    # query_parameters = req.params

    # # Iterate through query string parameters and print them
    # for key, value in query_parameters.items():
    #     print(f"Parameter: {key}, Value: {value}")

    # return func.HttpResponse(f"Full URL: {full_url}")

def main(req: func.HttpRequest) -> func.HttpResponse:
    
    full_url = req.url
    print(f"Full URL: {full_url}")
    print(len("https://whisper-function.azurewebsites.net/api/httptrigger1?test_func="))
    # print(len("http://localhost:7071/api/HttpTrigger1?test_func="))
# text = "http://localhost:7071/api/HttpTrigger1?file=https://learndd8d5891dfc9459d22.blob.core.windows.net/sample-workitems/audio.mp3?sp=r&st=2023-03-18T08:35:52Z&se= 2023-03-18T16:35:52Z&sv=2021-12-02&sr=b&sig=%2FJZopggfcTvYW6ip4qRCHH4cB%2FeKy3mUwBrn9NLQ5gw%3D"

    url_start = "https://whisper-function.azurewebsites.net/api/httptrigger1?test_func="
    # url_start = "http://localhost:7071/api/HttpTrigger1?test_func="
    # url_end = "?sp=r&st=2023-03-18T08:35:52Z&se= 2023-03-18T16:35:52Z&sv=2021-12-02&sr=b&sig=%2FJZopggfcTvYW6ip4qRCHH4cB%2FeKy3mUwBrn9NLQ5gw%3D"

    full_url = full_url.replace(url_start, '')
    print(full_url)

    file_url = req.params.get('file')
    test_func = req.params.get('test_func')
    if not file_url:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            file_url = req_body.get('file')
            test_func = req_body.get('test_func')

    if file_url:
        # encoded_url = quote(file_url, safe=":/?=&")
        # local_path = download_file(full_url)
        model = whisper.load_model("base")
        result = model.transcribe(full_url)
        my_result = result["text"]
        return func.HttpResponse(f"{my_result}")
    elif test_func:
        return func.HttpResponse(f"{full_url}")
    else:
        return func.HttpResponse(
            "Please provide a file URL in the query string or inasdfadsf the request body.",
            status_code=400
        )

import os
import tempfile
import requests
import whisper
import azure.functions as func
from urllib.parse import quote


def main(req: func.HttpRequest) -> func.HttpResponse:
    file_url = req.params.get('file')
    test_func = req.params.get('test_func')
    full_url = req.url

    if not file_url:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            file_url = req_body.get('file')
            test_func = req_body.get('test_func')

    if test_func:
        return func.HttpResponse(f"{full_url.replace(test_func, '')}")

    if file_url:
        model = whisper.load_model("base")
        result = model.transcribe(file_url)
        my_result = result["text"]
        return func.HttpResponse(f"{my_result}")

    return func.HttpResponse(
        "Please provide a file URL in the query string or in the request body.",
        status_code=400
    )

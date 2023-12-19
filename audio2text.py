import requests

API_URL = "https://api-inference.huggingface.co/models/bond005/wav2vec2-mbart50-ru"
headers = {"Authorization": "Bearer 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"}

def audio_to_text(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()


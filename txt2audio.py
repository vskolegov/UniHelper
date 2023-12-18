import torch
import os
from IPython.display import Audio, display
import requests


device = torch.device('cpu')
torch.set_num_threads(4)
local_file = 'model.pt'


def wavprocess(message):
    model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
    model.to(device)

    example_text = message
    speaker='baya'
    sample_rate = 48000

    audio = model.save_wav(text=example_text,
                            sample_rate = sample_rate,
                            speaker=speaker)

    return(audio)


sample_rate = 48000
audio = wavprocess('В недрах тундры выдры в г+етрах т+ырят в вёдра ядра кедров. Это я пишу для примера eee кстати, да. примера eee кстати, да. примера eee кстати, да. примера eee кстати, да.')
display(Audio(audio, rate=sample_rate))




API_URL = "https://api-inference.huggingface.co/models/bond005/wav2vec2-mbart50-ru"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

output = query("test.wav")
print(output)

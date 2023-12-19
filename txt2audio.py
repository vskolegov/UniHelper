import torch
import os
from IPython.display import Audio, display
import requests


device = torch.device('cpu')
torch.set_num_threads(4)
local_file = 'model.pt'


def text_to_audio(message):
    model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
    model.to(device)

    example_text = message
    speaker='baya'
    sample_rate = 48000

    audio = model.save_wav(text=example_text,
                            sample_rate = sample_rate,
                            speaker=speaker)

    return(audio)

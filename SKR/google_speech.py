import os
import soundfile as sf
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/sumit/Documents/sumit/gcp/nucleons-190616.json"

from google.cloud import speech_v1p1beta1 as speech


def get_language(file):
    client = speech.SpeechClient()

    speech_file = file
    first_lang = 'en-US'
    second_lang = ["hi-IN"]
    data, sr = sf.read(speech_file)
    with open(speech_file, 'rb') as audio_file:
        content = audio_file.read()
    # print(content)
    audio = speech.types.RecognitionAudio(content=content)

    config = speech.types.RecognitionConfig(
        encoding=speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=sr,
        # audio_channel_count=1,
        language_code=first_lang,
        alternative_language_codes=second_lang)

    # print('Waiting for operation to complete...')
    response = client.recognize(config, audio)
    print("response",response.results)
    return response.results[0].language_code

def get_text(file):
    client = speech.SpeechClient()

    speech_file = file
    first_lang = "hi-IN"
    second_lang = ["en-US"]
    data, sr = sf.read(speech_file)
    with open(speech_file, 'rb') as audio_file:
        content = audio_file.read()
    # print(content)
    audio = speech.types.RecognitionAudio(content=content)

    config = speech.types.RecognitionConfig(
        encoding=speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=sr,
        # audio_channel_count=1,
        language_code=first_lang,
        alternative_language_codes=second_lang)

    # print('Waiting for operation to complete...')
    response = client.recognize(config, audio)
    print("response",response.results)
    return response.results[0].alternatives
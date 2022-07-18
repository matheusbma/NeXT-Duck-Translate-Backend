from datetime import datetime
import os
import wave
import soundfile
from google.cloud import translate_v2 as translate
from google.cloud import speech

translate_client = translate.Client()

class TranslationError(Exception):
    def __init__(self, message="", status_code=400):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'

def convert_to_16bit(file):
   
    def timeStamp():
        now = datetime.now()

        timestamp = datetime.timestamp(now)
        return timestamp

    data, samplerate = soundfile.read(file)
    path = os.path.join(os.getenv("UPLOAD_FOLDER"), "new" + str(timeStamp()) + ".wav")
    soundfile.write(path, data, samplerate, subtype='PCM_16')

    return path

def read_wav_file(filename):
    with wave.open(filename, 'rb') as w:
        rate = w.getframerate()
        frames = w.getnframes()
        buffer = w.readframes(frames)

    return buffer, rate

def CheckSupportedLanguage(origin_language): #check if the target language is supported 
    try:
        response = translate_client.get_languages() #List language codes of supported languages.

        for language in response: #check all the languages
            if origin_language == language["language"]:
                return True

        return False 
        
    except Exception as e:
        raise e

def SpeechToTextPt(audio_file):
    try:
        client = speech.SpeechClient()
            
        audio_file = convert_to_16bit(audio_file)
        
        content, rate = read_wav_file(audio_file)
        os.remove(audio_file)
        stream = [content]

        requests = (
            speech.StreamingRecognizeRequest(audio_content=chunk) for chunk in stream
        )

        config = speech.RecognitionConfig( 
            encoding="LINEAR16",
            audio_channel_count=2,
            language_code="pt-BR",
            sample_rate_hertz=rate,
            model="command_and_search")

        streaming_config = speech.StreamingRecognitionConfig(config=config)

        responses = client.streaming_recognize(
            config=streaming_config,
            requests=requests,
        )

        for response in responses:
            for result in response.results:
                alternatives = result.alternatives
                for alternative in alternatives:
                    return alternative.transcript 
    except Exception as e:
        raise e           

def SpeechToTextEn(audio_file):
    try:
        client = speech.SpeechClient()
            
        audio_file = convert_to_16bit(audio_file)
        
        content, rate = read_wav_file(audio_file)
        os.remove(audio_file)
        stream = [content]

        requests = (
            speech.StreamingRecognizeRequest(audio_content=chunk) for chunk in stream
        )

        config = speech.RecognitionConfig( 
            encoding="LINEAR16",
            audio_channel_count=2,
            language_code="en-US",
            sample_rate_hertz=rate,
            model="command_and_search")

        streaming_config = speech.StreamingRecognitionConfig(config=config)

        responses = client.streaming_recognize(
            config=streaming_config,
            requests=requests,
        )

        for response in responses:
            for result in response.results:
                alternatives = result.alternatives
                for alternative in alternatives:
                    return alternative.transcript
    except Exception as e:
        raise e

def SpeechToTextOriginTarget(origin, audio_file):
    try:
        if not CheckSupportedLanguage(origin_language=origin):
            raise TranslationError(f"{origin} is not supported")

        client = speech.SpeechClient()
            
        audio_file = convert_to_16bit(audio_file)

        content, rate = read_wav_file(audio_file)
        os.remove(audio_file)
        stream = [content]

        requests = (
            speech.StreamingRecognizeRequest(audio_content=chunk) for chunk in stream
        )

        config = speech.RecognitionConfig( 
            encoding="LINEAR16",
            audio_channel_count=2,
            language_code=origin,
            sample_rate_hertz=rate,
            model="command_and_search")

        streaming_config = speech.StreamingRecognitionConfig(config=config)

        responses = client.streaming_recognize(
            config=streaming_config,
            requests=requests,
        )

        for response in responses:
            for result in response.results:
                alternatives = result.alternatives
                for alternative in alternatives:
                    return alternative.transcript
    except Exception as e:
        raise e
import os
from core.speechToText_core import *
from core.translation_core import *
from flask import request
from datetime import datetime

class TranslationControllerError(Exception):
    def __init__(self, message="", status_code=400):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'

def initializeSpeechToText(app):

    def timeStamp():
        now = datetime.now()

        timestamp = datetime.timestamp(now)
        return timestamp

    def upload_file():
        f = request.files['file']
        folder_name = os.getenv("UPLOAD_FOLDER")

        # Check whether the specified path exists or not
        isExist = os.path.exists(folder_name)

        if not isExist:
            # Create a new directory because it does not exist 
            os.makedirs(folder_name)
        
        path = os.path.join(folder_name, f.filename + str(timeStamp()) + ".wav")
        if f.filename != '':
            f.save(path)

        return path

    @app.route("/speech-to-text/en", methods=['POST', 'GET'])
    def speechtotext_pt_to_en():
        try:
            if request.method == 'GET':
                return "Speech in pt-BR"
           
            if request.method == 'POST':
                audio_path = upload_file()
                text = SpeechToTextEn(audio_path)   
                translation = TranslationPtToEn(text)
                os.remove(audio_path)

                return {"text": text, "translation": translation}, 200
                
        except Exception as e:
            return {"Error": e.message}, e.status_code

    @app.route("/speech-to-text/pt", methods=['POST', 'GET'])
    def speechtotext_en_to_pt():
        try:
            if request.method == 'GET':
                return "Speech in en-US"
           
            if request.method == 'POST':
                audio_path = upload_file()
                text = SpeechToTextPt(audio_path)   
                translation = TranslationEnToPt(text)
                os.remove(audio_path)

                return {"text": text, "translation": translation}, 200

        except Exception as e:
            return {"Error": e.message}, e.status_code

    @app.route("/speech-to-text/<origin>/<target>", methods=['POST', 'GET'])
    def speechtotext_translation_origin_to_target(origin, target):
        try:
            if request.method == 'GET':
                return "Speech in Origin to Target"
           
            if request.method == 'POST':

                audio_path = upload_file()
                text = SpeechToTextOriginTarget(origin, audio_path)
                translation = TranslationOriginToTarget(target, text)
                os.remove(audio_path)

                return {"text": text, "translation": translation}, 200

        except Exception as e:
            return {"Error": e.message}, e.status_code
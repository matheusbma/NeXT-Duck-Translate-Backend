from core.translation_core import *
from flask import request


class TranslationControllerError(Exception):
    def __init__(self, message="", status_code=400):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


def initializeTranslation(app):

    @app.route("/translations/pt-to-en", methods=['POST', 'GET'])
    def translation_pt_to_en():
        try:
            if request.method == 'GET':
                return "en-to-pt"

            if request.method == 'POST':
                body = request.get_json()
                text = body["text"]
                if not text:
                    raise TranslationControllerError("Text is empty", 400)
                translation = TranslationPtToEn(text)

                return {"translation": translation}, 200
        except Exception as e:
            return {"Error": e.message}, e.status_code

    @app.route("/translations/en-to-pt", methods=['POST', 'GET'])
    def translation_en_to_pt():
        try:
            if request.method == 'GET':
                return "en-to-pt"

            if request.method == 'POST':
                body = request.get_json()
                text = body["text"]
                if not text:
                    raise TranslationControllerError("Text is empty", 400)
                translation = TranslationEnToPt(text)

                return {"translation": translation}, 200

        except Exception as e:
            return {"Error": e.message}, e.status_code

    @app.route("/translations/target/<target_language>", methods=['POST', 'GET'])
    def translation_origin_to_target(target_language):
        try:
            if request.method == 'GET':
                return "target language"

            if request.method == 'POST':

                body = request.get_json()
                text = body["text"]
                if not text:
                    raise TranslationControllerError("Text is empty", 400)
                translation = TranslationOriginToTarget(target_language, text)

                return {"translation": translation}, 200

        except Exception as e:
            return {"Error": e.message}, e.status_code

    @app.route("/translations/source-language", methods=['POST', 'GET'])
    def Translation_Source_Language():
        try:
            if request.method == 'GET':
                return "source language"

            if request.method == 'POST':

                body = request.get_json()
                text = body["text"]
                if not text:
                    raise TranslationControllerError("Text is empty", 400)
                sourceLanguage = TranslationSourceLanguage(text)

                return {"source": sourceLanguage}, 200

        except Exception as e:
            return {"Error": e.message}, e.status_code

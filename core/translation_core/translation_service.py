import six
from google.cloud import translate_v2 as translate

translate_client = translate.Client()


class TranslationError(Exception):
    def __init__(self, message="", status_code=400):
        self.status_code = status_code
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'


def DecodeText(text):
    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    return text


# check if the target language is supported
def CheckSupportedLanguage(target_language):
    try:
        # List language codes of supported languages.
        response = translate_client.get_languages()

        for language in response:  # check all the languages
            if target_language == language["language"]:
                return True

        return False

    except Exception as e:
        raise e


def TranslationPtToEn(text):
    try:
        decoding_text = DecodeText(text)

        result = translate_client.translate(
            decoding_text, "en", format_="text")
        translation = result["translatedText"]

        return translation
    except Exception as e:
        raise TranslationError(f"Translation error: {e}")


def TranslationEnToPt(text):
    try:
        decoding_text = DecodeText(text)

        result = translate_client.translate(
            decoding_text, "pt", format_="text")
        translation = result["translatedText"]

        return translation
    except Exception as e:
        raise TranslationError(f"Translation error: {e}")


def TranslationOriginToTarget(target, text):
    try:
        if not CheckSupportedLanguage(target_language=target):
            raise TranslationError(f"{target} is not supported")
        decoding_text = DecodeText(text)

        result = translate_client.translate(
            decoding_text, target_language=target, format_="text")
        translation = result["translatedText"]
        return translation
    except Exception as e:
        raise TranslationError(f"Translation error: {e}")


def TranslationSourceLanguage(text):
    try:
        decoding_text = DecodeText(text)

        result = translate_client.translate(decoding_text)
        source_language = result["detectedSourceLanguage"]

        return source_language
    except Exception as e:
        raise TranslationError(f"Translation error: {e}")

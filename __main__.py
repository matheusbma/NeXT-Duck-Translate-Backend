import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()
from translation import initializeTranslation
from speechToText import initializeSpeechToText

app = Flask(__name__)

CORS(
        app,
        resources={r"/*": {"origins": "*"}},
        headers=['Content-Type', 'X-Requested-With', 'Authorization']
    )

initializeTranslation(app)
initializeSpeechToText(app)

@app.route("/", methods=["GET"])
def index():
    return "index"

port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)
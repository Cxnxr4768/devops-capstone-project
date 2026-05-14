from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS

app = Flask(__name__)

talisman = Talisman(app)
CORS(app)

@app.route("/")
def index():
    return {
        "name": "Account REST API Service",
        "version": "1.0"
    }

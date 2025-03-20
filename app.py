from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Tähän rakentuu lasten vaatevaraston hallintaa helpottava sivusto!"


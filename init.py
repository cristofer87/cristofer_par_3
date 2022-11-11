from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "servidor en ejecución"




    #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

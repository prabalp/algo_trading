from flask import Flask
from flask import request

app = Flask(__name__)  # understand this line


@app.route("/", methods=["POST"])
def home():
    data = request.data
    return data


@app.route("/auth_fyers", methods=["POST"])
def update_value():
    return ""


if __name__ == "__main__":  # understand this line (UTL)
    app.run()

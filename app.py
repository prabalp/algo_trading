from flask import Flask
from flask import request

app = Flask(__name__)  # understand this line


@app.route("/", methods=["POST","GET"])
def home():
    # data = request.data
    # return data
    return "good"

@app.route("/auth_fyers", methods=["POST", "GET"])
def update_value():
    return ""


if __name__ == "__main__":  # understand this line (UTL)
    app.run()

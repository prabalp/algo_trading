from flask import Flask

app = Flask(__name__)    #understand this line

@app.route('/')
def home():
    return 'Welcome to the API'

if __name__ == "__main__":  #understand this line (UTL)
    app.run()           
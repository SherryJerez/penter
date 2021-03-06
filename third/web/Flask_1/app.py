from flask import Flask
# https://flask.palletsprojects.com/en/1.1.x/quickstart/#quickstart
# flask run
app = Flask(__name__)

# import config
# app.config.from_object(config)

@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run() # app.run(debug=True)
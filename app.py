from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def hello():
    return "<h1>Hello from Python 3.12 on Azure App Service!</h1>"
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
 

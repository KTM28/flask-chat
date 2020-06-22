import os
from flask import Flask

app = Flask(__name__)
#app.config["TEMPLATES_AUTO_RELOAD"]=True 

@app.route('/')
def index():
    return f'<h1>ello Flask</h1>'

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=os.environ.get("PORT"),
    debug=True)
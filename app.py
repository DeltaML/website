from flask import Flask
from gevent.pywsgi import WSGIServer
from flask import render_template

app = Flask(__name__, static_url_path='', 
            static_folder='./assets',
            template_folder='./templates')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    
    server = WSGIServer(('0.0.0.0', 8080), app, log=app.logger)
    server.serve_forever()

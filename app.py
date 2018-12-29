import os
from flask import Flask
from gevent.pywsgi import WSGIServer
from flask import render_template
DEFAULT_PORT = 5000
app = Flask(__name__, static_url_path='', 
            static_folder='./assets',
            template_folder='./templates')

@app.route('/')
def index():
    return render_template('index.html')


def get_port():
    env_port = os.environ['PORT']
    return int(env_port) if env_port else DEFAULT_PORT

if __name__ == "__main__":
    
    port = get_port()
    server = WSGIServer(('0.0.0.0', port), app, log=app.logger)
    server.serve_forever()

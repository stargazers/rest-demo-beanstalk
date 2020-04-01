from flask import Flask
from flask import jsonify
import requests

app = Flask(__name__)

# This is for Elastic Beanstalk
application = app

@app.route('/')
def index():    
    return 'Hello, world'

@app.route('/weather')
def weather():
    response = requests.get('http://wttr.in/Vantaa?format=j1')
    return response.json()
    
@app.route('/health')
def health():
    return '200 - OK'

if __name__ == '__main__':
    app.run(debug=True)
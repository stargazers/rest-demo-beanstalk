from flask import Flask

app = Flask(__name__)

# This is for Elastic Beanstalk
application = app

@app.route('/')
def index():
    return 'Hello, world'

@app.route('/weather')
def weather():
    return 'Cold.'
    
@app.route('/health')
def health():
    return '200 - OK'

if __name__ == '__main__':
    app.run(debug=True)
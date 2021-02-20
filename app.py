from flask import Flask

# create Flask instance
app = Flask(__name__)

# create first route
# create starting point or 'root'
@app.route('/')
def index():
    return 'Index page'

# try to create another route
@app.route('/hello')
def hello_world():
    
    return 'Hello World'


import json
from flask import Flask,request
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from controller.authentication import signUp_bp  
from controller.authentication import login_bp





app = Flask(__name__)
app.config['SECRET_KEY'] = '98c5bc0a178ff2d6c0c1471c6f3dc5e4'

app.register_blueprint(signUp_bp)
app.register_blueprint(login_bp)





# Configure the JWT token location
app.config['JWT_TOKEN_LOCATION'] = ['headers']
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 1
 

app.config['WTF_CSRF_ENABLED'] = False
app.config['SECRET_KEY'] = '98c5bc0a178ff2d6c0c1471c6f3dc5e4'# Set your secret key
app.config['JWT_ALGORITHM'] = 'HS256'  # Choose an appropriate algorithm
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False  # Set your token expiration as needed

# Initialize the Flask-JWT-Extended extension
jwt = JWTManager(app)

# Enable CORS for all routes
CORS(app)
CORS(app, origins=['http://localhost:3000', 'https://my-digital-ocean-app.com'])



@app.route('/')
def hello_world():
    return 'Hello, World!!'



if '__main__'==__name__:
    app.run() 

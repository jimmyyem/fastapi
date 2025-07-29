import json

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os


load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configure MySQL database from environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define a sample User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'


# Create database tables
@app.before_request
def create_tables():
    db.create_all()


@app.route('/')
def hello_world():
    return json.dumps({'message': 'Hello World!'})


# Sample route to add a user
@app.route('/add_user/<username>/<email>')
def add_user(username, email):
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': f'User {username} added successfully'})

# Sample route to get all users
@app.route('/users')
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username, 'email': user.email} for user in users])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
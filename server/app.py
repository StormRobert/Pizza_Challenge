from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from models import db
import os

abs_path=os.getcwd()
db_path=f'sqlite:///{abs_path}/db/app.db'

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return 'Restaurants'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
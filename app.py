import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask
from config import Config
from models import db
from routes import habit_blueprint

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()  

app.register_blueprint(habit_blueprint)

if __name__ == '__main__':
    app.run(debug=True)

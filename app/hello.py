import os

from flask import Flask                           
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

def init_db(app):
    db.init_app(app)

@app.route('/')                                   
def hello_world():                                
    return "Hello World!" + os.environ["MYSQL_DATABASE"]                       

if __name__ == '__main__':                        
    app.run(host="0.0.0.0", port=3000, debug=True)

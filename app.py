from datetime import datetime
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
# from .main.views import main
# def create_app():
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///posts.db'
db = SQLAlchemy(app)

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)

    def __repr__(self):
        return 'Comment' + str(self.id)
# from .main import models


#     app.register_blueprint(main)

#     return app

# # breakpoint()

if __name__=="__main__":
    app.run(debug=True)
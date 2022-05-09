from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
# from .main.views import main
# def create_app():
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///posts.db'
db = SQLAlchemy(app)

#     app.register_blueprint(main)

#     return app

# # breakpoint()

if __name__=="__main__":
    app.run(debug=True)
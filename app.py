from flask import Flask, Blueprint
# from .main.views import main
# def create_app():
app = Flask(__name__)


#     app.register_blueprint(main)

#     return app

# # breakpoint()

if __name__=="__main__":
    app.run(debug=True)
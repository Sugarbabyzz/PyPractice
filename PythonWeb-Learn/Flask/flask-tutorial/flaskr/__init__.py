import os
from flask import Flask


# def create_app(test_config=None):
#     # create and configure the main
#     main = Flask(__name__, instance_relative_config=True)
#     main.config.from_mapping(
#         SECRET_KEY='dev',
#         DATABASE=os.path.join(main.instance_path, 'flaskr.sqlite')
#     )
#
#     if test_config is None:
#         main.config.from_pyfile('config.py', silent=True)
#     else:
#         main.config.from_pyfile(test_config)
#
#     try:
#         os.makedirs(main.instance_path)
#     except OSError:
#         pass
#
#     @main.route('hello')
#     def hello():
#         return 'Hello world!'
#
#     return main


app = Flask(__name__)

@app.route('/', methods=['Get', 'POST'])
def home():
    return '<h1>Home</h1>'


if __name__ == '__main__':
    app.run()
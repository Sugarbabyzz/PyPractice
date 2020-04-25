from flask import Flask
from .article import article
from .user import user

app = Flask(__name__)
app.debug = True

app.register_blueprint(article)
app.register_blueprint(user)


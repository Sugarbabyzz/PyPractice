from flask import Blueprint
from flask import request

article = Blueprint('article', __name__)

@article.route('/article')
def login():
    return 'article'

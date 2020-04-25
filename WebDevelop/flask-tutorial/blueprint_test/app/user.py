from flask import Blueprint
from flask import request

user = Blueprint(
    'user',
    __name__)

@user.route('/login')
def login():
    return 'Login'
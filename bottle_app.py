# A very simple Bottle Hello World app for you to get started with...
import os
from bottle import default_app, route, run, redirect

@route('/')
def get_index():
    redirect ("/public")
   

@route('/secret')  
def get_public():
    return 'This message should not be shown to anyone!'

@route('/public')  
def get_private():
    return 'This message should be shown to everyone!'
@route('/login')  
def get_login():
    return 'It looks like you re logged in!'

@route('/logout')  
def get_logout():
    return 'It looks like you re logged out!'


if  'PYTHONANYWHERE_DOMAIN' in os.environ: 
    application = default_app()
else :
    run(host='localhost', port=8080)

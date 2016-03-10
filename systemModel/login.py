# coding:utf-8

import web
import hashlib


def login(db):
    '''
    login check function
    :param db:Database from the main page
    :return: loginstatue:login statues
    '''
    loginstatue = 0
    user, passwdmd5 = web.input().username, hashlib.md5(web.input().password) # get the username and password from the POST
    passwd = passwdmd5.hexdigest()
    ident = db.query("select * from user where username = $us",vars={'us': user})
    try:
        checkpass =  ident[0]['password']
        if passwd == checkpass:
            web.config._session.login=1 # set the login session
            loginstatue = 1
        else:
            web.config._session.login=0
            print passwd,"Wrong1!"
    except:
        print passwd,"Wrong2!"
        web.config._session.login=0
    return loginstatue
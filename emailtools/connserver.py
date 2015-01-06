#-*- encoding: utf-8 -*-
'readconfig.py'

import ConfigParser
import os
import poplib

def getConf():
    config = ConfigParser.ConfigParser()
    config.read( os.path.join( 'config.ini' ) )
    
    dicElements = {}
    dicElements['popser'] = config.get( "information", "POPSERVER" )
    dicElements['user'] = config.get( "information", "USER" )
    dicElements['password'] = config.get( "information", "PASSWORD" )
    dicElements['savepath'] = config.get( "information", "SAVEPATH" )
    dicElements['parsernum'] = config.get( "information", "PARSERNUM" )
    
    return dicElements
    

def conServer():
    conf = getConf()
    popser = conf.get( 'popser' )
    user = conf.get( 'user' )
    password = conf.get( 'password' )

    #POP3取信
    try:
        M = poplib.POP3_SSL( popser )
        M.user( user )
        M.pass_( password )
    except:
        M = 'Connect failed! Check the config file!'
    return M
'command.py written by lizhiqiang execute svn update command'

import subprocess
import ConfigParser


#read config file and return a dictionary
def conf_info():
    #parser config file
    config = ConfigParser.ConfigParser()
    #----Rewrite----
    config.read( '/home/peanut/gdjcode/tacweb/templates/svnupconfig.ini' )

    dicElements = {}
    dicElements['username'] = config.get( "information", "username" )
    dicElements['password'] = config.get( "information", "password" )
    dicElements['path'] = config.get( "information", "path" )
    dicElements['url'] = config.get( "information", "url" )
    return dicElements


#folder already checked out or not
def isco_dir():
    dic = conf_info()
    path = dic.get( 'path' )
    
    judstr = "find %s -name '.svn' -type d" %path
    res = subprocess.Popen( judstr, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
    temp = res.stdout.readlines()
    res.communicate()
    
    if temp:
        return True
    else:
        return False


#return checkout svn command string
def checkout_svn():
    dic = conf_info()
    path = dic.get( 'path' )
    username = dic.get( 'username' )
    password = dic.get( 'password' )
    url = dic.get( 'url' )

    strExec = "svn co %s %s --username %s --password %s --non-interactive --trust-server-cert" %( url, path, username, password )
    return strExec


#return update svn command string
def update_svn():
    dic = conf_info()
    path = dic.get( 'path' )
    username = dic.get( 'username' )
    password = dic.get( 'password' )

    strExec = "svn up %s --username %s --password %s --non-interactive --trust-server-cert" %( path, username, password )
    return strExec


#execute commands
def exec_commands( strs ):
    res = subprocess.Popen( strs, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
    err = res.stderr.readlines()
    result = res.wait()    #res.wait()=0 that command execute successful
    res.communicate()
    return result

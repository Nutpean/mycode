##-*- encoding: utf-8 -*-
'email_analyse.py parser email and save attachments'

#import standard library
import poplib
import cStringIO
import email
import os
import re

#import local modules
from connserver import conServer, getConf
from decode import decoding
from getmsg import getDate, getSubject, getConName
from savemsg import saveMessage

#get savepath and parsernum
conf = getConf()
savepath = conf.get( 'savepath' )
parsernum = int( conf.get( 'parsernum' ) )

#connect pop3 server
Mail = conServer()
if type(Mail) == str:
    print Mail
else:
    #total emails
    emailnum = len(Mail.list()[1])
    receivenum = emailnum - parsernum

    while emailnum > receivenum:    
        m = Mail.retr(emailnum)
        emailnum -= 1

        #parser emails
        buf = cStringIO.StringIO()
        for j in m[1]:        
            print >>buf, j
        buf.seek(0)
        msg = email.message_from_file(buf)

        #get send time
        if msg.get_all( 'date' ) != None:
            sendtime = msg.get_all( 'date' )
            if sendtime:
                timestr = getDate( sendtime )
                print 'time: ' + timestr
        else:
            str = msg.get_all( 'received' )
            str = re.split( r';', str[0] )
            str = 'A' + str[1]
            sendtime = []
            sendtime.append( str )
            timestr = getDate( sendtime )
            print 'time: ' + timestr
        #get subject
        substr = msg.get_all( 'subject' )
        subject = getSubject( substr )
        print 'subject: ' + subject
        #get company name
        compname = getConName( msg )
        print 'company name: ' + compname
        
        #create folders
        dirname = savepath + compname + timestr + subject
        print 'dirname:' + dirname
        if compname and subject:
            try:
                if not os.path.isdir( dirname ):
                    os.mkdir( dirname )
            except:
                err = open( 'ErrorLog.txt', 'a' )
                err.write( dirname+' create folder failed!!!' )
                err.write( '\n' )
                err.close()
        
            saveMessage( msg, compname, dirname, subject )
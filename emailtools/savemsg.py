#-*- encoding: utf-8 -*-
'savemsg.py'

import email
import re
import os
from decode import decoding

def saveMessage( msg, compname, dirname, subject ):
    msg = msg
    compname = compname
    dirname = dirname
    subject = subject
    contentfile = os.path.join(dirname, '%s.txt'%subject)
    if not os.path.isfile( contentfile ):
        f = open( os.path.join(dirname, '%s.txt'%subject), 'a' )
        
        f.write( '\n\n----------------------------\n' )
        f.write( 'From:' )
        efrom = email.utils.parseaddr(msg.get_all("from"))[1]
        t = re.sub( '=.*=', '', efrom )
        f.write( t )
        
        f.write( '\n\n----------------------------\n' )
        f.write( 'To:' )
        eto = email.utils.parseaddr(msg.get_all("to"))[1]
        etolist = re.split( ',', eto )
        for i in etolist:
            t = re.sub( '=.*=', '', i )
            f.write( t )
            
        f.write( '\n\n----------------------------\n' )
        f.write( 'Cc:' )
        ecc = ecc = email.utils.parseaddr(msg.get_all("cc"))[1]
        ecclist = re.split( ',', ecc )
        for i in ecclist:
            t = re.sub( '=.*=', '', i )
            f.write( t )
        f.write( '\n\n----------------------------\n' )
        
        f.close()
        
        for part in msg.walk():
            contenttype =  part.get_content_type()
            maintype =  part.get_content_maintype()
            filename = part.get_filename()
            #get formate attachment name
            if filename != None:
                filename = decoding( filename )
                print 'filename' + filename

            #have attachments or not
            if compname and subject:
                #save attachments
                if filename != None and maintype == 'application':
                    try:
                        f = open(os.path.join(dirname, filename), 'wb')
                        f.write( part.get_payload(decode=True) )
                        f.close()
                    except:
                        err = open( 'ErrorLog.txt', 'a' )
                        err.write( dirname+' Parser failed! Attachment download failed!!!' )
                        err.write( '\n' )
                        err.close()
                #save content
                if contenttype == 'text/plain':
                    f = open( os.path.join(dirname, "%s.txt"%subject), 'a' )
                    f.write( part.get_payload(decode=True) )
                    f.close()
#-*- encoding: utf-8 -*-
'decode.py exchange code type'

import re
import base64

def decoding( sourcestr ):
    if re.findall( '\?', sourcestr ):
        strlist = re.split( '\?', sourcestr )
        msg1 = ''
        msg2 = ''
        
        if len ( strlist ) > 3:
            msg1 = strlist[3]    
            msg1 = base64.decodestring( msg1 )
        if len( strlist ) > 7:
            msg2 = strlist[7]
            msg2 = base64.decodestring( msg2 )
       
        if re.findall( 'utf-8|UTF-8', sourcestr ):
            #utf-8 need decode('utf-8').encode('gbk')
            msg1= msg1.decode('utf-8').encode('gb18030')
            msg2= msg2.decode('utf-8').encode('gb18030')
        message = msg1 + msg2
    else:
        message = sourcestr
    
    if type(message) == unicode:
        message = message.encode('gb18030')
        
    message = message.decode('gb18030').encode('utf-8')
        
    return message
    

'''def getSubject( subject ):
    substr = subject[0]
    str = decoding( substr )
    str = re.sub( r'\n|\*|>|<|:|\?|\"|\\|/|\|', '.', str )
    
    return str'''
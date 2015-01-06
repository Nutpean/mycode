##-*- encoding: utf-8 -*-
'attachment.py parser email and save attachments'

import poplib
import cStringIO
import email
import base64
import re
import os

from dateformat import dateFormat
from readconfig import getConf

#get config information
conf = getConf()
popser = conf.get( 'popser' )
user = conf.get( 'user' )
password = conf.get( 'password' )

#POP3取信
M = poplib.POP3_SSL( popser )
M.user( user )
M.pass_( password )

#打印有多少封信
numMessages = len(M.list()[1])
print 'num of messages', numMessages

for i in range(numMessages):    
    m = M.retr(i+1)
#m = M.retr( numMessages )

    buf = cStringIO.StringIO()
    for j in m[1]:        
        print >>buf, j
    buf.seek(0)

    #解析信件内容
    msg = email.message_from_file(buf)

    #创建文件夹！！！文件夹存在的情况
    t = msg.get_all( 'date' )
    date = dateFormat( t )

    '''sub = msg.get_all( 'subject' )
    sub = sub[0]
    if re.findall( 'gb18030|UTF-8|gb2312|gbk|GB2312|GBK|utf-8', sub ):    #Notic   utf-8  gbk  gb2312
        p = re.split( '\?', sub )
        r = p[3]
        sub = base64.decodestring( p[3] )

    try:
        dirname = date + sub
        os.mkdir( dirname )
    except:
        dirname = date
        os.mkdir( dirname )'''
    dirname = date
    os.mkdir( dirname )

    for part in msg.walk():
        maintype =  part.get_content_maintype()
        filename = part.get_filename()
        if filename != None:
            if re.findall( 'gb18030|GB18030|gb2312|GB2312|GBK|gbk', filename ):            #Notic   utf-8  gbk  gb2312            
                p = re.split( '\?', filename )
                r = p[3]
                filename = base64.decodestring( p[3] )
                print filename
            elif re.findall( 'utf-8|UTF-8', filename ):
                p = re.split( '\?', filename )
                r = p[3]
                filename = base64.decodestring( p[3] )
                filename = filename.decode('utf-8').encode('gbk')
                print filename

        if filename and maintype == 'application':
            # 保存附件
            try:
                #f = open("%s" % filename,'wb')
                f = open(os.path.join(dirname, filename), 'wb')
                f.write( part.get_payload(decode=True) )
                f.close()
            except:
                err = open( 'ErrorLog.txt', 'a' )
                err.write( dirname )
                err.write( '邮件解析错误，附件未能下载' )
                err.write( '\n' )
                err.close()
            
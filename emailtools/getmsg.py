#-*- encoding: utf-8 -*-
'getmsg.py'

import email
import re
from decode import decoding

#Month directory
MONTH = { 'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', 'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12' }

#Email Data format like datastr = ['Thu, 11 Dec 2014 10:34:59 +0800', '']
def getDate( datestr ):
    #get first string and split it 
    dstr = datestr[0]
    dlist = re.split( r'\s', dstr )
    
    #get year month day
    year = dlist[3]
    if MONTH.get( dlist[2] ):
        month = MONTH.get( dlist[2] )
    else:
        month = '99'
    day = dlist[1]
    
    #get time
    time = re.sub( ':', '.', dlist[4] )
    
    datatime = '-' + year + month + day + '-' + time + '-'
    return datatime
    

#get subject    
def getSubject( subject ):
    substr = subject[0]
    str = decoding( substr )
    str = re.sub( r'\s|\n|\*|>|<|:|\?|\"|\\|/|\|', '.', str )
    
    #return str
    pattern = u'报告'
    pen = pattern.encode('utf-8')
    #pen = pen.decode('utf-8').encode('gb18030')

    if re.findall( pen, str ):
        return str
    else:
        return ''
    

#get company name
def getConName( message ):
    file_list = []
    compname = []
    for part in message.walk():
        maintype = part.get_content_maintype()
        filename = part.get_filename()
        #get formate files name
        if filename != None and maintype == 'application':
            filename = decoding( filename )
            file_list.append( filename )
    
    #get company name !!!    
    if file_list:
        compstr = file_list[0]
        compname = re.split( '_|--|\.', compstr )
        return compname[0]
    else:
        return ''

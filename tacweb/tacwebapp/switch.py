'switch.py written by lizhiqiang update GEN_CREDIATE_FILE_SWITCH value'
import sys
import re

def turn_onoff():
    #file path --the globalconf.py
    filename = "/home/peanut/gdjcode/conf.py"    #----Rewrite----
    status = 0  #return status

    #read file
    fr = open( filename, 'r' )  
    lines = fr.readlines()  
    fr.close()  

    #change GEN_CREDIT_FILE_SWITCH value
    for i in range( len(lines) ):  
        if lines[i].find( 'GEN_CREDIT_FILE_SWITCH' ) != -1:  
            if lines[i].find( '1' ) != -1:
	        lines[i] = "GEN_CREDIT_FILE_SWITCH = 0\n"
		status = 0
            else:
	        lines[i] = "GEN_CREDIT_FILE_SWITCH = 1\n"
		status = 1
	#elif lines[i].find( 'GEN_CREDIT_FILE_SWITCH = 0' ) != -1:
	 #   lines[i] = "GEN_CREDIT_FILE_SWITCH = 1\n"
	 #   status = 1

    #rewrite file and close file
    fw = open( filename, 'w' )  
    fw.writelines(lines)  
    fw.close()

    return status

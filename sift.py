#!/usr/bin/env python
#===========================================================
# _______  ___   _______  _______        _______  __   __  |
#|       ||   | |       ||       |      |       ||  | |  | |
#|  _____||   | |    ___||_     _|      |    _  ||  |_|  | |
#| |_____ |   | |   |___   |   |        |   |_| ||       | |
#|_____  ||   | |    ___|  |   |   ___  |    ___||_     _| |
# _____| ||   | |   |      |   |  |   | |   |      |   |   |
#|_______||___| |___|      |___|  |___| |___|      |___|   |
#							   |
#===========================================================


######## Python Imports ##############
from __future__  import print_function 
import time 
import os
import subprocess
FNULL=open(os.devnull, 'w')
######################################


####### Variable Definitions #########
tme=time.strftime("%H:%M")
dte=time.strftime("%m-%d-%y")
breaker=False
files=[]
init=0

###### Bootstrap Protocol ############
print('===========================================================')
print(' _______  ___   _______  _______        _______  __   __  |')
print('|       ||   | |       ||       |      |       ||  | |  | |')
print('|  _____||   | |    ___||_     _|      |    _  ||  |_|  | |')
print('| |_____ |   | |   |___   |   |        |   |_| ||       | |')
print('|_____  ||   | |    ___|  |   |   ___  |    ___||_     _| |')
print(' _____| ||   | |   |      |   |  |   | |   |      |   |   |')
print('|_______||___| |___|      |___|  |___| |___|      |___|   |')
print('                                                          |')
print('===========================================================')

while breaker!=True:
	yn=raw_input("Enter names of logs to be searched or 'done' to finish setup: ")
	if yn!='done':
		files.append(yn)
	if yn=='done':
		breaker=True

count=0
while init!=len(files):
	victim=files[count]
	########## List Creations ############
	bad=[]
	log=[]
	his=[]
	hee=[]
	see=[]
	outie=[]
	######################################

	######### System Commands ############
	subprocess.call(["mkdir", "AuditFiles"], stdout=FNULL, stderr=subprocess.STDOUT) 


	######### Opening files ##############
	badwords=open('badwords.txt', 'r')
	cisco=open(victim, 'r')
	history=open('history.txt', 'r') 
	out=open('/home/nick/Desktop/AuditFiles/' + tme + " " + dte + " audit.txt" ,'a')
	#out=open('/home/nick/Desktop/AuditFiles/test.txt', 'a')
	######################################


	######### File to List ###############
	for x in badwords:
		bad.append(x)
	for x in cisco:
		log.append(x)
	for x in history:
		his.append(x)
	######################################


	#### Removing Spaces and End Line ####
	bad=[x.strip("\n") for x in bad]
	bad=[x.strip(" ") for x in bad]
	log=[x.strip("\n") for x in log]
	log=[x.strip(" ") for x in log]
	his=[x.strip(" ") for x in his]
	his=[x.strip("\n") for x in his]
	######################################
	out.write(" " + '\n')
	out.write('=========================================================\n')
	out.write('                 Security Violations                     \n')
	out.write('=========================================================\n')
	print("=========================================================")
	print("Audit initated on file: " + victim)
	print('=========================================================')
        print('                 Security Violations                     ')
        print('=========================================================')


	#########     Security     ##########
	####### Comparing the lists ##########
	for x in log:
		for y in bad:
			if y in x:
				print('Security violation: | the string "' + x + '" was found in file ' + victim)
				out.write('Security violation: | the string "' + x + '" was found in file ' + victim + '\n')
				see.append('Security violation: | the string "' + x + '" was found in file ' + victim)
	out.write('=========================================================\n')
	out.write('                Historical Information                   \n')
	out.write('=========================================================\n')
	print('=========================================================')
        print('                Historical Information                   ')
        print('=========================================================')


	for x in log:
		for y in his:
			if y in x:
				print('Historical event information:| ' + x) 
				out.write('Historical information: | the string "' + x + '" was found in file ' + victim + '\n')
				hee.append('Historical even information:| ' + x)
	print("\n")
	print("****************************************************************")
	print("\n")

	aee="===================================="
	bee="        Security Information        "
	cee="===================================="

	dee="===================================="
	eee="       Historical Information       "
	fee="===================================="
	
	
	out2=open('/home/nick/Desktop/AuditFiles/' + tme + " " + dte + " audit.txt" ,'r')

	histt=''
	secvil=''
	for x in hee:
		histt=histt+' '+x+'\n'
	for x in see:
		secvil=secvil+' '+x+'\n'
	
	wee=aee+'\n'+bee+'\n'+cee+'\n'+secvil+'\n'+dee+'\n'+eee+'\n'+fee+'\n'+histt
	count+=1
	init+=1
	out.close()
	for x in out2:
		outie.append(x)

outie=[x.strip("\n") for x in outie]
mail=''
for x in outie:
	mail=mail+' '+x+"\n"
mail=mail+'\n'
out2.close()



###### Email Backend ###############
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
fromaddr=""
toaddr=""
msg=MIMEMultipart()
msg['From']=fromaddr
msg['To']=toaddr
msg['Subject']='Router Log Update'
body=mail
msg.attach(MIMEText(body,'plain'))


import smtplib
server=smtplib.SMTP()
server.ehlo()
server.starttls()
server.ehlo()
server.login()
text=msg.as_string()
server.sendmail(fromaddr,toaddr,text)


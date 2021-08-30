import sys
import os	
import  smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import validators		
from bs4 import BeautifulSoup	
import requests	

def mail_sending(server,from_,to_,title):
	# Send the mail
	msg = MIMEMultipart()
	msg['From'] = from_
	msg['To'] = to_
	msg['Subject'] = title
	message = 'new job!!!'
	msg.attach(MIMEText(message , 'plain'))
	part = MIMEBase('application', "octet-stream")
	part.set_payload(open("attachment.py", "rb").read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', 'attachment; filename="attachment.py"')
	msg.attach(part)
	try:
		server.sendmail(from_ ,to_ , msg.as_string())
		print ("Congratulations, the email was successfully sent")	
	except:
		print('failed')

def mail_sending_withparm(server,from_,to_,titleA):
	# Send the mail
	msg = MIMEMultipart()
	msg['From'] = from_
	message = 'new job!!!'
	Argument4=sys.argv[4]
	Argument4=Argument4.replace('\\n', '\n')	
	if validators.url(Argument4) == True :		#its a url
		print("its url")
		r = requests.get(Argument4)
		soup = BeautifulSoup(r.content, 'html.parser')
		t=soup.title.string 
		n=soup.find('name')
		b=soup.find('body')

		if t != 'none':
			msg['Subject']=t
		else:
			msg['Subject']=titleA

		if n!= 'none':
			msg['To'] = to_
		else:
			msg['To'] = n

		if b != 'none':
			message=b.text [6:100]
			
			

		msg.attach(MIMEText(message , 'plain'))
		part = MIMEBase('application', "octet-stream")
		part.set_payload(open("attachment.py", "rb").read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition', 'attachment; filename="attachment.py"')
		msg.attach(part)
		try:
			server.sendmail(from_ ,to_ , msg.as_string())
			print ("Congratulations, the email was successfully sent")
		except:
			print('failed')	
		
	elif "title" in Argument4 or "Title" in Argument4:	#its a string
		print("its string")
		str=Argument4.split(",")
		title = ""
		body =""
		name=""
		for line in str:
			if "name" in line :
				name=line.split(":")[1]
				msg['To'] =name
			if "title" in line or "Title" in line:
				title=line.split(":")[1]
				msg['Subject']=title
			if "content" in line or "body" in line:
				body=line.split(":")[1]
				message=body
		if not title :
			msg['Subject'] = titleA
		if not name:
			msg['To'] = to_
		msg.attach(MIMEText(message , 'plain'))
		part = MIMEBase('application', "octet-stream")
		part.set_payload(open("attachment.py", "rb").read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition', 'attachment; filename="attachment.py"')
		msg.attach(part)
		try:
			server.sendmail(from_ ,to_ , msg.as_string())
			print ("Congratulations, the email was successfully sent")	
		except:
			print('failed')

	elif os.path.exists(Argument4):         #its a path               
		name = ""
		title = ""
		body = ""	
		with open(Argument4) as p:
			a=p.readlines()
		for line in a:
			if "name" in line :
				name=line.split(":")[1].strip()
				msg['To'] =name
			if "title" in line or "Title" in line:
				title=line.split(":")[1].strip()
				msg['Subject']=title
			if "content" in line or "body" in line:
				body=line.split(":")[1]
				message=body
				
		if not title :
			msg['Subject'] = titleA
		if not name:
			msg['To'] = to_
		msg.attach(MIMEText(message , 'plain'))
		part = MIMEBase('application', "octet-stream")
		part.set_payload(open("attachment.py", "rb").read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition', 'attachment; filename="attachment.py"')
		msg.attach(part)
		try:
			server.sendmail(from_ ,to_ , msg.as_string())
			print ("Congratulations, the email was successfully sent")	
		except:
			print('failed')
	
	
	
	else:
		print ("not valid Argument4")



def main():
	if len(sys.argv)<4:
		print("Please enter 3 or 4 argv")
		sys.exit()
	username = sys.argv[1]
	mail_server = sys.argv[2]
	job_title = sys.argv[3]
	email ="orel.cyber@gmail.com"
	password = 'Cyber1212'
	server = smtplib.SMTP("smtp.gmail.com",587)
	server.starttls()
	server.ehlo()
	server.login(email,password)
	if len(sys.argv)==4:
		print("mail is in process")
		mail_sending(server ,email,username+"@"+mail_server+".com",job_title)
		server.quit()
	if len(sys.argv)==5:
		mail_sending_withparm(server,email,username+"@"+mail_server+".com",job_title)
		server.quit()

main()
#https://stackoverflow.com/questions/3362600/how-to-send-email-attachments

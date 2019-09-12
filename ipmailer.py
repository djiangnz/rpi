#! /usr/bin/python
import subprocess
import smtplib
from email.mime.text import MIMEText
import datetime
import time
import platform

def get_ip():
    arg ='ip route list'
    out = subprocess.Popen(arg, shell=True, stdout=subprocess.PIPE)
    data = out.communicate()
    split_data = data[0].split()
    info = split_data[split_data.index('src') + 1]
    return info

def get_df():
    arg = 'df -h'
    out = subprocess.Popen(arg, shell=True, stdout=subprocess.PIPE)
    info = ''
    for line in out.stdout:
        info += line
    return info

def get_syslog():
    arg = 'tail /var/log/syslog'
    out = subprocess.Popen(arg, shell=True, stdout=subprocess.PIPE)
    info = ''
    for line in out.stdout:
        info += line
    return info

def mail():
    try:
        # set account
        to = 'to@gmail.com'
        gmail_user = 'from@gmail.com'
        gmail_password = 'gmail app passwd'
        smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo
        smtpserver.login(gmail_user, gmail_password)
        # mail body
        today = datetime.date.today()
        mail_body = "version: %s\nuname: %s" %(platform.version(), platform.uname())
        mail_body += '\n\n' + get_df()
        mail_body += '\n' + get_syslog()
        # compose email
        msg = MIMEText(mail_body)
        msg['Subject'] = "RPI @ "+ get_ip() +" started up on %s" % today.strftime('%b %d %Y')
        msg['From'] = gmail_user
        msg['To'] = to
        # send email
        smtpserver.sendmail(gmail_user, [to], msg.as_string())
        smtpserver.quit()
        return False
    except:
        # service is not ready on booting
        return True

cont = True
while cont:
    cont = mail()
    time.sleep(1)

#!/usr/bin/env python

import subprocess
import smtplib
from email.mime.text import MIMEText
import datetime
import time
import platform
import sys

def get_public_ip():
    arg ='dig +short myip.opendns.com @resolver1.opendns.com'
    return run_in_shell(arg)

def get_private_ip():
    arg ="hostname -I | cut -d ' ' -f1"
    return run_in_shell(arg)

def get_df():
    arg = 'df -h'
    return run_in_shell(arg)

def get_syslog():
    arg = 'tail /var/log/syslog'
    return run_in_shell(arg)

def run_in_shell(arg):
    try:
        out = subprocess.Popen(arg, shell=True, stdout=subprocess.PIPE)
        return out.communicate()[0].decode("utf-8")
    except Exception as e:
        log_error(e)
        return ""

def log_error(e):
    arg = 'echo "%s" >> ~/.ipmailer.log' % e
    run_in_shell(arg)

def mail():
    try:
        # set account
        receiver = 'to@gmail.com'
        sender = 'from@gmail.com'
        password = 'password' # or App Specific password (if 2 step verification is on)

        if len(sys.argv) > 3:
            if sys.argv[1]:
                receiver = sys.argv[1]
            if sys.argv[2]:
                sender = sys.argv[2]
            if sys.argv[3]:
                password = sys.argv[3]

        smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
        smtpserver.starttls()
        smtpserver.login(sender, password)
        # mail body
        public_ip = get_public_ip()
        private_ip = get_private_ip()
        subject_ip = private_ip
        
        mail_body = "version: %s\nuname: %s" % (platform.version(), platform.uname())
        mail_body += '\n'
        if len(public_ip) > 1:
            subject_ip = public_ip
            mail_body += '\nPublic  IP: %s' % get_public_ip()
        mail_body += '\nPrivate IP: %s' % get_private_ip()
        mail_body += '\nDisk Usage: \n%s' % get_df()
        mail_body += '\n/var/log/syslog: \n%s' % get_syslog()
        # compose email
        msg = MIMEText(mail_body)
        
        msg['Subject'] = "Server @ " + subject_ip + " started up"
        msg['From'] = "Server Info <%s>" % sender
        msg['To'] = sender
        # send email
        smtpserver.sendmail(sender, [receiver], msg.as_string())
        smtpserver.quit()
        return False
    except Exception as e:
        log_error(e)
        return True

cont = True
counter = 0
while cont:
    cont = mail()
    time.sleep(1)
    counter += 1
    if counter > 60:
      cout = False
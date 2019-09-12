# RPi scripts

## ipmailer.py
> sending email of ip address on booting
1. put the script to `/home/pi/.ipmailer.py`
1. add the task to `rc.local`. `sudo sed -i '/exit 0/ c\/usr/bin/python /home/pi/.ipmailer.py &\n\nexit 0' /etc/rc.local`

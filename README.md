# RPi scripts

## ipmailer.py
> sending an email of IP address on booting, works for both python2 and python3 

#### via curl
1. `curl -sL https://raw.githubusercontent.com/d-jiang/rpi/master/ipmailer.py | python - to@gmail.com from@gmail.com app_specific_password`

#### manually
1. download the script to `/home/pi/.ipmailer.py`
1. change the settings and message
1. add the task to `rc.local`. `sudo sed -i '/exit 0/ c\/usr/bin/python /home/pi/.ipmailer.py &\n\nexit 0' /etc/rc.local`

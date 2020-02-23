# RPi scripts
[![HitCount](http://hits.dwyl.com/dianyij/rpi.svg)](http://hits.dwyl.com/dianyij/rpi)
## bootmail.py
- sending an email of IP address on booting, works for both python2 and python3.   
- [dig](https://linux.die.net/man/1/dig) is required if you want to get your public IP address.    

#### Usage
##### via curl
1. make sure `/etc/rc.local` exists
1. `sudo sed -i '/^exit 0/ c\(sleep 30 && $(which curl) -sL https://raw.githubusercontent.com/dianyij/rpi/master/bootmail.py | $(which python || which python3) - to@gmail.com from@gmail.com from_password) &\n\nexit 0' /etc/rc.local`
##### manually
1. download the script to `/home/pi/.bootmail.py`
1. change the settings and message
1. `sudo vi /etc/rc.local`
1. insert `$(which python || which python3) /home/pi/.bootmail.py &` before `exit 0`

Notification alarm to telegram bot from check_mk monitoring with Proxy configuration.
for sending alarm notification to telegram after create bot we must have telegram bot token (telegram_bot_token) and change this token on source code.
for example i have check_mk 1.4.0p31 installed on ubuntu server 16.04 because in my country access to telegram is restricted,
i have to use proxy for connection to telegram.

services installed on my server is:

tor and privoxy with "sudo apt install tor, privoxy"
then config tor on /etc/tor/torrc (if you install tor from source code your config file path is:/usr/local/etc/tor/torrc) uncomment: SOCKSPort 9050 DataDirectory /root/.tor 

then config privoxy service:
/etc/privoxy/config uncomment: forward-socks5t / 127.0.0.1:9050 . then:

systemctl restart tor.service 
systemctl restart privoxy.service 

after connecting to tor network completed you can test your ip address with test file in this repository.
you can test tor proxy connection with:
./proxytortest.py
or
./proxytortestsocket.py

The telegram notification script can be put into PREFIX/share/check_mk/notifications/ (with PREFIX being wherever Check_MK got installed to) 
and will automatically be available as a notification method in the WATO Notification configuration. 
for more information:
"https://metzlog.srcbox.net/2016/01/monitoring-notifications-via-telegram/"
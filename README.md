# check_mk-telegram-notify
notifaction alarm to telegram bot from check_mk monitoring with Proxy config in code.
for sending alarm notification to telegram after create bot we must have telegram bot token (telegram_bot_token) and change this token on source code.
for example i have check_mk 1.4.0p31 installed on ubuntu server 16.04 LTS becuase in my country access to telegram is restricted 
i have to use proxy for connection to telegram services 
install tor and privoxy in my server and configuring :
/etc/tor/torrc
if you install tor from source code your config file path is:
/usr/local/etc/tor/torrc
uncomment  SOCKSPort 9050
DataDirectory /root/.tor
and then you can restart tor service with 
systemctl restart tor.service

then config privoxy
/etc/privoxy/config
and uncomment 
forward-socks5t   /               127.0.0.1:9050 .
systemctl restart privoxy.service
after conecting to tor network completed you can test your ip address from testproxy.py or test2proxy.py


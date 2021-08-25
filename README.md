# redis2http

Redis2http takes request data from redis and performs HTTP request.
Mostly used to implement web-hook calls

## Why not requests.get/requests.post ?
Most likely you want main program to run fast and spend very short time on calling hook. HTTP requests are not good for it - it may fail or be slow in many reasons. But putting data to local redis (LPUSH) is very quick.

## Install

~~~
pip3 install redis2http
~~~

If you want to start on boot (as root or sudo):
~~~
cp /usr/local/redis2http/redis2http.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable redis2http
systemctl start redis2http
~~~

## Usage for CLI
CLI is not main purpose for redis2http, but it's good for testing. Examples:

~~~
redis2http.py --send GET https://google.com/
~~~
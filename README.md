# redis2http

Redis2http takes request data from redis and performs HTTP request.
Mostly used to implement web-hook calls

## Why not requests.get/requests.post ?
Most likely you want main program to run fast and spend very short time on calling hook. HTTP requests are not good for it - it may fail or be slow for many reasons. On other hand, LPUSH operation with local redis is always very quick and very reliable.

redis2http is good if a) You do not need to wait for HTTP request completion b) You do not need to get any reply from request 

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

To start as service in foreground (for debugging), just run `redis2http.py` (not options required).


To send request via redis (for debugging):
~~~
redis2http.py --send GET https://google.com/
~~~

After this (in less then second), you can see result in redis2http service output. If redis2http runs as systemd service, then `sudo journalctl -u redis2http`.

## Usage from Python or from whatever (via redis)

Put JSON-encoded data structure to `http_requests_queue` list (or use `-q` for other key name). Python example:
~~~python
data = {
    'method': 'GET',
    'url': 'https://example.com/hook',
    'payload': None
}
request = json.dumps(data)
redis_connection.lpush('http_requests_queue', request)
~~~

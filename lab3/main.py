import datetime

def app(environ, start_response):
    now = datetime.datetime.now()
    data = "Date: %d.%d.%d\n" % (now.day, now.month, now.year)
    data += "SERVER_NAME: %s\n" % (environ["SERVER_NAME"])
    data += "SERVER_PORT: %s" % (environ["SERVER_PORT"])
    data = data.encode("ascii")

    # print(environ)

    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])
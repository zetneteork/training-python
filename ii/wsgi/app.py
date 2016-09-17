#!/usr/bin/python

def application(environ, start_response):
    response_body = ''.join('%s: %s\n' % (key, value)
            for key, value in sorted(environ.items())).encode("utf-8")
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain'),
            ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)
    return [response_body]

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 3000, application)
    httpd.serve_forever()

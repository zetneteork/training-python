#!/usr/bin/python

class application(object):
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response

    def __iter__(self):
        self.start_response('200 OK', [('Content-Type', 'text/plain; charset=utf-8')])
        return iter([''.join('%s: %s\n' % (key, value)
            for key, value in sorted(self.environ.items())).encode("utf-8")])

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 3000, application)
    httpd.serve_forever()

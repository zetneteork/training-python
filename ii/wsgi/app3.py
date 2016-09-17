#!/usr/bin/python

class application(object):
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response

    def __iter__(self):
        self.start_response('200 OK', [('Content-Type', 'text/plain; charset=utf-8')])
        self.items = iter(sorted(self.environ.items()))
        return self

    def __next__(self):
        return '{0}: {1}\n'.format(*next(self.items)).encode("utf-8")

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 3000, application)
    httpd.serve_forever()

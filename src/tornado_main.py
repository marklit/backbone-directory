# Run this with
# PYTHONPATH=. DJANGO_SETTINGS_MODULE=testsite.settings testsite/tornado_main.py
# Serves by default at
# http://localhost:8080/hello-tornado and
# http://localhost:8080/hello-django
from tornado.options import options, define, parse_command_line
import django.core.handlers.wsgi
import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi


define('port', type=int, default=8000)


class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello from tornado')


def main():
    static_path = os.path.join(os.path.dirname(__file__), "../frontend/")
    settings = {
        "static_path": static_path,
        "icons_path": os.path.join(static_path, '/ico/'),
    }
    print settings
    wsgi_app = \
        tornado.wsgi.WSGIContainer(django.core.handlers.wsgi.WSGIHandler())
    tornado_app = tornado.web.Application([
        ('/hello-tornado', HelloHandler),
        
        
        
        (r'/favicon\.ico', tornado.web.StaticFileHandler, dict(path=settings['icons_path'])),
        
        
        ('.*\.js', tornado.web.FallbackHandler, dict(fallback=wsgi_app)),
        (r"/(css|img|js|lib|tpl)*", tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
        ('.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app)),
    ], **settings)
    server = tornado.httpserver.HTTPServer(tornado_app)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
  main()

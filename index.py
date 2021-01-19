""" from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from api.views.hello_world import hello_world  
from api.utils.format import server_log
from api.config import PORT, ADDR


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
        server_log(ADDR, PORT)
        
    server = make_server('0.0.0.0', 5000, app)
    server.serve_forever()
     """
     
from http.server import BaseHTTPRequestHandler
from cowpy import cow

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        message = cow.Cowacter().milk('Hello from Python from a Serverless Function!')
        self.wfile.write(message.encode())
        return

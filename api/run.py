from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from views.hello_world import hello_world  
from utils.format import server_log
from config import PORT, ADDR


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
        server_log(ADDR, PORT)
        
    server = make_server('0.0.0.0', 5000, app)
    server.serve_forever()
    

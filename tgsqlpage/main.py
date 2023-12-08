from tg import expose, TGController, AppConfig
from wsgiref.simple_server import make_server

class MyController(TGController):
    @expose()
    def index(self):
        return "Hello, TurboGears"

#Application Configuration
config = AppConfig(minimal=True, root_controller = MyController())

#Create Application
app = config.make_wsgi_app()


#Create the Server
server = make_server('', 8080, app)
server.serve_forever()
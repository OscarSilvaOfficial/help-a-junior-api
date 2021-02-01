from api.middlewares.application import ApplicationManager
from api.controllers import views

app = ApplicationManager().getApp()

app.add_url_rule('/', 'index', views.getPosts, methods=['GET', 'POST'])
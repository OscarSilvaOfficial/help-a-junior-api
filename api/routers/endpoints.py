from api.middlewares.application import ApplicationManager
from api.controllers import views

app = ApplicationManager().getApp()

app.add_url_rule('/', 'posts', views.getPosts)
app.add_url_rule('/', 'send_post', views.setPost, methods=['POST'])
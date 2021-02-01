from api.middlewares.application import ApplicationManager
from api.controllers import posts, users

app = ApplicationManager().getApp()

app.add_url_rule('/', 'posts', posts.getPosts)
app.add_url_rule('/', 'send_post', posts.setPost, methods=['POST'])
app.add_url_rule('/users', 'get_users', users.getUsers)
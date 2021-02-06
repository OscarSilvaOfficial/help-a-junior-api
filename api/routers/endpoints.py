from api.middlewares.application import ApplicationManager
from api.controllers import posts, users

app = ApplicationManager().getApp()

app.add_url_rule('/', 'posts', posts.get_posts)
app.add_url_rule('/', 'send_post', posts.create_post, methods=['POST'])
app.add_url_rule('/users', 'get_users', users.get_users)
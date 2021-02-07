from api.middlewares.application import ApplicationManager
from api.controllers import posts, users

app = ApplicationManager().get_app()

app.add_url_rule('/posts', 'get_posts', posts.get_posts)
app.add_url_rule('/posts', 'create_post', posts.create_post, methods=['POST'])
app.add_url_rule('/posts/<post_id>', 'update_post', posts.update_post, methods=['PATCH'])
app.add_url_rule('/posts/<post_id>', 'delete_post', posts.delete_post, methods=['DELETE'])
app.add_url_rule('/users', 'get_users', users.get_users)
from api.middlewares.application import ApplicationManager
from api.controllers.posts import PostsView


app = ApplicationManager().get_app()

app.add_url_rule('/posts', 'get_posts', PostsView.get_posts)
app.add_url_rule('/posts', 'create_post', PostsView.create_post, methods=['POST'])
app.add_url_rule('/posts/<post_id>', 'update_post', PostsView.update_post, methods=['PATCH'])
app.add_url_rule('/posts/<post_id>', 'delete_post', PostsView.delete_post, methods=['DELETE'])
from api.middlewares.application import ApplicationManager
from api.controllers import users

app = ApplicationManager().get_app()

app.add_url_rule('/users', 'get_users', users.get_users)
app.add_url_rule('/users', 'create_users', users.create_users, methods=['POST'])
app.add_url_rule('/users/<user_id>', 'update_users', users.update_users, methods=['PATCH'])
app.add_url_rule('/users/<user_id>', 'delete_users', users.delete_users, methods=['DELETE'])
from api.middlewares.application import ApplicationManager
from api.controllers import login


app = ApplicationManager().get_app()

app.add_url_rule('/login', 'login', login.login, methods=['POST'])
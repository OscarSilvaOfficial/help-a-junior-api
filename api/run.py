from api.middlewares.application import ApplicationManager
from api.routers import posts_urls, users_urls, login_urls

app = ApplicationManager().get_app()

if __name__ == '__main__':
    app.run(debug=True)
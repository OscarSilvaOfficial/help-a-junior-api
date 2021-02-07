from api.middlewares.application import ApplicationManager
import api.routers.endpoints

app = ApplicationManager().get_app()

if __name__ == '__main__':
    app.run(debug=True)
from api.middlewares.application import ApplicationManager
import api.routers.endpoints
from flask_cors import CORS

app = ApplicationManager().getApp()
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)
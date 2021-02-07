from sqlalchemy import Column, String, Integer, ForeignKey
from api.middlewares.application import ApplicationManager
from api.models.user import Users
from flask_sqlalchemy import SQLAlchemy


app = ApplicationManager().get_app()
db = SQLAlchemy(app)

class Posts(db.Model):
  __tablename__ = "posts"
  
  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, ForeignKey(Users.id))
  post = Column(String)
  
  def __repr__(self):
    return f"{self.post}"
  
from sqlalchemy import Column, String, Integer, ForeignKey
from api.middlewares.application import ApplicationManager
from flask_sqlalchemy import SQLAlchemy


app = ApplicationManager().getApp()
db = SQLAlchemy(app)

class Posts(db.Model):
  __tablename__ = "posts"
  
  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, ForeignKey('users.id'))
  post = Column(String)
  
  def __repr__(self):
    return f"{self.post}"
  
from sqlalchemy import Column, String, Integer
from api.middlewares.application import ApplicationManager
from flask_sqlalchemy import SQLAlchemy


app = ApplicationManager().getApp()
db = SQLAlchemy(app)

class Users(db.Model):
  __tablename__ = "users"
  
  id = Column(Integer, primary_key=True)
  user = Column(String)
  passwd = Column(String)
  user_name = Column(String)
  
  def __repr__(self):
    return f"{self.user_name}"
  
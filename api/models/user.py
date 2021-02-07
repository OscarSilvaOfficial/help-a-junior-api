from api.middlewares.application import ApplicationManager
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy


app = ApplicationManager().get_app()
db = SQLAlchemy(app)

class Users(db.Model):
  __tablename__ = "users"
  
  id = Column(Integer, primary_key=True)
  user = Column(String)
  passwd = Column(String)
  user_name = Column(String)
  
  def __repr__(self):
    return f"{self.user_name}"
  
from api.models.user import Users
from flask import jsonify

def get_users():
  
  users = []
  for user in Users.query.all():
    users.append(str(user))
  return jsonify(users)
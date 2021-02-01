from flask import jsonify
from api.models.user import Users


def getUsers():
  response = Users.query.all()
  return jsonify(str(response[0]))
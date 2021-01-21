from api.repository.repository import Repository
from flask import jsonify

def getPosts():
    payload = Repository().getPosts()
    response = {
        're': payload
    }
    return jsonify(response)
from fast_sql_manager import repository
from api.repository.repository import Repository
from flask import jsonify, request
from api.utils import format


repository = Repository()

def getPosts():
    payload = repository.selectPosts()
    return jsonify(payload)


def setPost():
    payload = format.requestToTuple(request.args)
    return jsonify(repository.insertPosts(payload))
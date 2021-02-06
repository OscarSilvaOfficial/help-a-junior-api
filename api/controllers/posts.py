from flask import jsonify, request
from api.utils import format
from api.models.post import Posts
from api.middlewares.application import ApplicationManager

session = ApplicationManager().getDbSession()

def get_posts():        
    return jsonify(format.queryToList(Posts.query.all()))


def create_post():
    payload = format.requestToDict(request.args)
    post = Posts(post=payload['post'], user_id=payload['user_id'])
    session.add(post)
    try:
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()
        raise session.rollback()
    finally:
        session.close()
    
    return 'ok'

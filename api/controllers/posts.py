from flask import jsonify, request
from api.utils import format
from api.models.post import Posts
import logging


def get_posts():
    log = format.create_log(request.full_path)
    logging.info(log)        
    response = format.queryToList(Posts.query.all())
    return jsonify(response)


def create_post():
    """ payload = format.requestToDict(request.args)
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
    
    return 'ok' """
    pass
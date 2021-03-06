from flask import jsonify, request, Response
from api.models.post import Posts
from flask_sqlalchemy import SQLAlchemy
from api.middlewares.application import ApplicationManager
from api.controllers.login import authenticated as auth


app = ApplicationManager().get_app()
db = SQLAlchemy(app)

class PostsView(object):
  
  @auth  
  def get_posts():
    response = tuple(Posts.query.all())
    return jsonify(response)

  @auth
  def create_post():
    payload = dict(request.get_json(force=True))
    post = Posts(post=payload['post'], user_id=payload['user_id'])
    
    try:
      db.session.add(post)
      db.session.commit()
    except Exception as e:
      return Response(jsonify({'error':str(e)}), status=400)
    
    return Response('Post criado', status=201)

  @auth
  def update_post(post_id):
    payload = dict(request.get_json(force=True))
    selected_post = db.session.query(Posts).get(post_id)
    
    selected_post.user_id = payload['user_id']
    selected_post.post = payload['post']
    
    try:
      db.session.commit()
    except Exception as e:
      return Response(str(e), status=400)
    
    return Response('Post alterado', status=204)

  @auth
  def delete_post(post_id):
    try:
      delete = db.session.query(Posts).get(post_id)
      db.session.delete(delete)
      db.session.commit()
    except Exception as e:
      return Response(str(e), status=400)
    
    return Response('Post deletado', status=202)
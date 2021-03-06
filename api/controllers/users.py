from api.middlewares.application import ApplicationManager
from api.controllers.login import authenticated as auth
from api.controllers.email import create_email
from api.utils.functions import encript_passwd
from flask import jsonify, request, Response
from flask_sqlalchemy import SQLAlchemy
from pymysql.err import IntegrityError
from api.models.user import Users
from flask import jsonify
import logging


app = ApplicationManager().get_app()
db = SQLAlchemy(app)

@auth
def get_users():
  
  users = []
  for user in Users.query.all():
    users.append(str(user))
    
  return jsonify(users)

@auth
def create_users():
  payload = dict(request.get_json(force=True))
  user = Users(
    user=payload['user'], 
    passwd=encript_passwd(payload['passwd']), 
    user_name=payload['user_name']
  )
  
  try:
      db.session.add(user)
      db.session.commit()
  except IntegrityError as e:
      return Response(str(e), status=400)
    
  try:
    create_email('oscarkaka222@gmail.com', "Conta criada", 'Olá, sua conta foi criada com sucesso')
  except Exception as e:
    return Response(e, status=400)
  
  return Response('Usuário criado', status=201)

@auth
def update_users(user_id):
    payload = dict(request.get_json(force=True))
    user = db.session.query(Users).get(user_id)
    
    if not user:
      return Response('Usuário não existe', status=400)
    
    if 'passwd' in payload:
      user.passwd = encript_passwd(payload['passwd'])
    
    if 'user_name' in payload:
      user.user_name = payload['user_name']
    
    try:
        db.session.commit()
    except IntegrityError as e:
        return Response(str(e), status=400)
    
    
    try:
      create_email('oscarkaka222@gmail.com', "Conta criada", 'Olá, sua conta foi criada com sucesso')
    except Exception as e:
      return Response(e, status=400)
    
    return Response('Usuário alterado', status=204)
 
@auth 
def delete_users(user_id):
    try:
        delete = db.session.query(Users).get(user_id)
        db.session.delete(delete)
        db.session.commit()
    except Exception as e:
        return Response(str(e), status=400)
    
    return Response('Usuário deletado', status=202)
from flask import request, Response
from api.models.user import Users
from api.utils.functions import decript_passwd 
from api.configs.enviroment import SECRET_KEY
from functools import wraps
import jwt


def login():
  login = request.get_json(force=True)
  user = Users.query.filter_by(user=login['user']).first()
  passwd = login['passwd']
  
  if user:    
    user_decript_passwd = decript_passwd(user.passwd)
    if passwd == user_decript_passwd:
      token = jwt.encode(
        {'user': user.user},
        SECRET_KEY,
        algorithm="HS256"
      )
      return token
    else:
      return Response('Usuário ou senha incorretos', status=400)
  else:
    return Response('Usuário ou senha incorretos', status=400)
  
def authenticated(func):
  
  @wraps(func)
  def wrapper(*args, **kwargs):
    if 'auth-token' in request.headers:
      token = request.headers['auth-token']
      try:
        jwt.decode(token, SECRET_KEY, algorithms="HS256")
      except jwt.DecodeError:
        return Response('Token de autenticação incorreto', status=400)
    else:
      return Response('Não existe token de autenticação', status=400)
    return func(*args, **kwargs)
  return wrapper

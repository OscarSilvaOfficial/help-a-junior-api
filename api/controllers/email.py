import requests, logging
from flask import jsonify


def create_email(destination_email, subject, content):
  payload = {
    "destination": destination_email,
    "subject": subject,
    "content": content
  }
  
  try:
    requests.post('http://localhost:5001/send_mail', data=jsonify(payload))
  except Exception as e:
    logging.error(e)
    return "Não foi possível enviar email"
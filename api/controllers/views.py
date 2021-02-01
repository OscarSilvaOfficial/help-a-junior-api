from api.repository.repository import Repository
from flask import jsonify, request
import requests
from datetime import datetime
from time import sleep 
import json

def getPosts():

    log_url = request.values['log_url']
    finish_url = request.values['finish_url']

    if 'params' in request.values: 
        params = request.values['params']

    payload = {
        'log': 'Execução recebida',
    }

    init = json.dumps(payload)
    requests.post(log_url, data=init, headers=None)

    payload = {
        'log': 'Execução iniciou',
    }

    status = json.dumps(payload)
    requests.post(log_url, data=status, headers=None)

    try:
        dataTest = Repository.getPosts

        payload = {
            'log': 'Posts selecionados',
        }

        execucao = json.dumps(payload)
        requests.post(log_url, data=execucao, headers=None)
    except Exception as e:
        payload = {
            'log': 'Erro ao selecionar items',
            'error': True
        }  

        execucao = json.dumps(payload)
        requests.post(log_url, data=execucao, headers=None)


    if False:
        payload = {
            'log': 'Erro ao finalizar',
            'error': True
        }  
    else:
        payload = {
            'log': 'Execução finalizou',
            'error': False
        }    
    
    final = json.dumps(payload)
    
    """ cria log final """
    requests.post(log_url, data=final, headers=None) 
    """ informa que a execução finalizou """
    requests.post(finish_url, data=final, headers=None) 

    return 'ok'


import os
import re

local_path = os.path.abspath('api/logs')

def requestToDict(args):    
    return dict(args)

def requestToTuple(args):
    return tuple(requestToDict(args).values())

def queryToList(args):
    response = []
    for arg in args:
        response.append(str(arg))
    return response

def create_log(args):
    dirs = os.listdir(local_path)
    
    try:
        last_file_v = max([int(item) for item in re.findall(r'[0-9]?[0-9]', ' '.join(dirs), re.MULTILINE)])
    except:
        last_file_v = 0
    
    with open(f'{local_path}/file_v{last_file_v+1}.log', 'x') as f:
        f.write(args)
        
    return 'Arquivo criado'
            
    
    
from api.configs.enviroment import SECRET_KEY
import os, re, jwt

local_path = os.path.abspath('api/logs')

def create_log(args):
    dirs = os.listdir(local_path)
    
    try:
        last_file_v = max([int(item) for item in re.findall(r'[0-9]?[0-9]', ' '.join(dirs), re.MULTILINE)])
    except:
        last_file_v = 0
    
    with open(f'{local_path}/file_v{last_file_v+1}.log', 'x') as f:
        f.write(args)
        
    return 'Arquivo criado'

def encript_passwd(passwd):
    response = jwt.encode(
        {"passwd": passwd}, 
        SECRET_KEY, 
        algorithm="HS256"
    )
    return response

def decript_passwd(passwd):
    response = jwt.decode(
        passwd, 
        SECRET_KEY, 
        algorithms="HS256"
    )
    return response['passwd']
    
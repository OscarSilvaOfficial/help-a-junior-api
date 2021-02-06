def requestToDict(args):    
    return dict(args)

def requestToTuple(args):
    return tuple(requestToDict(args).values())

def queryToList(args):
    response = []
    for arg in args:
        response.append(str(arg))
    return response
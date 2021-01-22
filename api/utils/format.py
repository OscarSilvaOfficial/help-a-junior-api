def requestToDict(args):
    return dict(args)

def requestToTuple(args):
    return tuple(requestToDict(args).values())
from fast_sql_manager import repository


class Repository(object):
    
    def __init__(self, db=repository.Repository('localhost', 3306, 'root', '123456', 'junior_db')):
        self._base = db
    
    def getPosts(self):
        return self._base.selectAll('posts')

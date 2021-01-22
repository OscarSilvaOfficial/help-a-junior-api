from fast_sql_manager.repository import Repository


class Repository(object):
    
    def __init__(self, db=Repository('localhost', 3307, 'root', 'root', 'junior_db')):
        self._base = db
    
    def selectPosts(self):
        return self._base.selectAll('posts')
    
    def insertPosts(self, values: tuple):
        return self._base.insert(
            'posts', 
            ['user_id', 'post'],
            values
        ) 
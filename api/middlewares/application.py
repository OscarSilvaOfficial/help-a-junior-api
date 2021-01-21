from flask import Flask


class ApplicationManager(object):

    def __init__(self, app=Flask(__name__)):
        self._app = app

    def getApp(self):    
        return self._app
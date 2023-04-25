
from Media import *

class Series(Media):
    def __init__(self,name,director,imdb_score,url,year,casts,session):
        super().__init__(name,director,imdb_score,url,year,casts)
        self.session=session

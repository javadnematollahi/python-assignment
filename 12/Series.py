


class Series(Media):
    def __init__(self,name,director,IMDB_score,url,duration,casts,session,episods):
        super().__init__(name,director,IMDB_score,url,duration,casts)
        self.session=session
        self.episods=episods
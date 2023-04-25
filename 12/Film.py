from Media import Media 

class Film(Media):
    def __init__(self,name,director,imdb_score,url,year,casts,genre,duration):
        super().__init__(name,director,imdb_score,url,year,casts)
        self.genre=genre
        self.duration= duration
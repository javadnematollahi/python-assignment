from Actor import *
import time
class Media:
    def __init__(self,name,director,imdb_score,url,year,casts):
        self.name=name
        self.director=director
        self.imdb_score=imdb_score
        self.url=url
        self.year=year
        self.casts=casts
    
    def show_info(self):
        print(f"name is {self.name}\ndirector is {self.director}\nIMDBscore is {self.imdb_score}")
        print(f"URL is {self.url}\duration is {self.duration}\ncasts is {self.imdb_score}")
    
    def download(self):
        print('Click on below link to download and watch: ')
        for i in range(5):
            print(i+1)
            time.sleep(1)
        print(f'Your link in ready:\n  {self.url}')
        


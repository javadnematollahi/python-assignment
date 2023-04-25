from Media import *
from Series import *
from Film import *
from Documentary import *
from Clip import *
from Actor import *
import pytube
# list hae zir ba object hae ke az dadehae database sakhte mishavand por mishavand
films_ram = []
series_ram=[]
clip_ram=[]
documentary_ram=[]
actor_ram=[]
actor_list=[]

def change_stringactor_to_class(a,b=['Unknown']):
    film_actors=[]
    a=a.split('-')
    for i in range(len(a)):
        if a[i] != 'None':
            if actor_list.count(a[i]) == 0:
                nameolastname=a[i].split(' ')
                a[i]=f'{nameolastname[0]}{nameolastname[1]}'
                a[i]=Actor(nameolastname[0],nameolastname[1],b,'Unknown','Unknown','Unknown')
                actor_ram.append(a[i])
                actor_list.append(f'{nameolastname[0]}{nameolastname[1]}')
            else:
                a[i]=actor_ram[actor_list.index(a[i])]
        film_actors.append(a[i])
    return film_actors


def read_from_database():

    f= open("database.txt",'r')
    line_skip=2
    for line in f:
        # print(line)
        if line == "actor\n":
            line_skip=1
            define_media=1
        elif line == "film\n":
            line_skip=1
            define_media=2
        elif line == "series\n":
            define_media=3
            line_skip=1
        elif line == "documentary\n":
            define_media=4
            line_skip=1
        elif line == "clip\n":
            define_media=5  
            line_skip=1    

        if line_skip == 0:
            if define_media == 1:
                result=line.split(',')
                result[5]=result[5].replace("\n", "")
                result[2]=result[2].split('-')
                nameolastname=result[0]+result[1]
                actor_list.append(nameolastname)
                nameolastname=Actor(result[0],result[1],result[2],result[3],result[4],result[5])
                actor_ram.append(nameolastname)

            if define_media == 2:
                film_actors=[]
                result=line.split(',')
                result[7]=result[7].replace("\n", "")      
                result[0]=Film(result[0],result[1],result[2],result[3],result[4],change_stringactor_to_class(result[5],[result[0]]),result[6],result[7])
                films_ram.append( result[0])
            elif define_media == 3:
                series_actors=[]
                result=line.split(',')
                result[6]=result[6].replace("\n", "")
                    
                result[0]=Series(result[0],result[1],result[2],result[3],result[4],change_stringactor_to_class(result[5]),result[6])
                series_ram.append( result[0])
            elif define_media == 4:
                documentary_actors=[]
                result=line.split(',')
                result[5]=result[5].replace("\n", "")
                    
                result[0]=Documentary(result[0],result[1],result[2],result[3],result[4],change_stringactor_to_class(result[5]))
                documentary_ram.append( result[0])
            elif define_media == 5:
                clip_actors=[]
                result=line.split(',')
                result[5]=result[5].replace("\n", "")                   
                result[0]=Clip(result[0],result[1],result[2],result[3],result[4],change_stringactor_to_class(result[5]))
                clip_ram.append( result[0])    
        elif line_skip == 1:
            line_skip=0
 
    f.close()
 
 
def write_to_database():
    f=open("database.txt","w+")
    f.write( 'actor')  
    f.write('\n')
    for actor in actor_ram:
        film_of_actor=''
        for i in actor.film:
            film_of_actor=film_of_actor+f'{i}-'
        film_of_actor=film_of_actor.removesuffix("-")
        f.write( f'{actor.name},{actor.lastname},{film_of_actor},{actor.age},{actor.married},{actor.action_time}')
        f.write('\n')
    f.write( 'film')  
    f.write('\n')
    for filmm in films_ram:
        actor_of_film=''
        if filmm.casts[0]!='None':
            for i in filmm.casts:
                actor_of_film=actor_of_film+f'{i.name}{i.lastname}-'
            actor_of_film=actor_of_film.removesuffix("-")
        else:
            actor_of_film='None'            
        f.write( f'{filmm.name},{filmm.director},{filmm.imdb_score},{filmm.url},{filmm.year},{actor_of_film},{filmm.genre},{filmm.duration}')    
        f.write('\n')
    f.write( 'series')  
    f.write('\n')
    for seri in series_ram:
        actor_of_seri=''
        if seri.casts[0]!='None':
            for i in seri.casts:
                actor_of_seri=actor_of_seri+f'{i.name}{i.lastname}-'
            actor_of_seri=actor_of_seri.removesuffix("-")
        else:
            actor_of_seri='None'
        f.write( f'{seri.name},{seri.director},{seri.imdb_score},{seri.url},{seri.year},{actor_of_seri},{seri.session}')    
        f.write('\n')
    f.write( 'documentary')  
    f.write('\n')
    for doc in documentary_ram:
        actor_of_doc=''
        if doc.casts[0]!='None':
            for i in doc.casts:
                actor_of_doc=actor_of_doc+f'{i.name}{i.lastname}-'
            actor_of_doc=actor_of_doc.removesuffix("-")
        else:
            actor_of_doc='None'
        f.write( f'{doc.name},{doc.director},{doc.imdb_score},{doc.url},{doc.year},{actor_of_doc}')    
        f.write('\n')
    f.write( 'clip')  
    f.write('\n')
    for clp in clip_ram:
        actor_of_clp=''
        if clp.casts[0]!='None':
            for i in clp.casts:
                actor_of_clp=actor_of_clp+f'{i.name}{i.lastname}-'
            actor_of_clp=actor_of_clp.removesuffix("-")
        else:
            actor_of_clp='None'
        f.write( f'{clp.name},{clp.director},{clp.imdb_score},{clp.url},{clp.year},{actor_of_clp}') 
        f.write('\n')
    f.close()
    
          
def show_menu():
    print("1_ Add Media")
    print("2_ Edit Media")
    print("3_ Delete Media")
    print("4_ Search Media")
    print("5_ showlist")
    print("6_ Download")
    print("7_ Exit")
 
def add():
    code_identify=int(input("which do you want to add?\n add film press 1\n add series press 2\n add documentary press 3\n add clip press 4\n add actor press 5"))
    add_casts=[]
    def add_actor():
        name= input("Enter name: ")
        lastname= input("Enter lastname: ")
        film=[]
        film.append(input("Enter film: "))
        if film=='':
            film.append("Unknown") 
        if film[0] != "Unknown" :
            while True:
                film_number=input('Do you want to add another film?\nY for yes\nN for No')
                if film_number=='Y':
                    film.append(input("Enter film: "))
                else:
                    break
        age=input("Enter age: ")
        if age=='':
            age="Unknown"
        married=input("Enter married status: ")
        if married=='':
            married="Unknown"
        action_time=input("Enter action_time: ")
        if action_time=='':
            action_time="Unknown"  
        new_actor=Actor(name,lastname,film,age,married,action_time)  

        actor_ram.append(new_actor)
        if code_identify!=5:
             add_casts.append(new_actor)

    if code_identify==5:
        add_actor()
    
    if code_identify==1 or code_identify==2 or code_identify==3 or code_identify==4:
        name= input("Enter name: ")
        director= input("Enter director: ")
        imdb_score= input("Enter imdb_score: ")
        url= input("Enter url: ")
        year= input("Enter year of produce: ")
        film_number=input('Do you want to add cast to this media?\nY for yes\nN for No')
        if film_number=='Y':
            add_actor()
            while True:
                film_number=input('Do you want to add another actor?\nY for yes\nN for No')
                if film_number=='Y':
                    add_actor()
                else:
                    break
        casts= add_casts 
        if name=='':
            name="Unknown"
        if director=='':
            director="Unknown"
        if imdb_score=='':
            imdb_score="Unknown"
        if url=='':
            url="Unknown"
        if year=='':
            year="Unknown"
        if casts=='':
            casts="Unknown"

    if code_identify==1: 
        genre= input("Enter genre: ")
        duration=input("Enter duration: ")
        if genre=='':
            genre="Unknown"
        if duration=='':
            duration="Unknown"
        new_file=Film(name,director,imdb_score,url,year,casts,genre,duration)
        films_ram.append(new_file)  
    if code_identify==2: 
        session= input("Enter session: ")
        if session=='':
            session="Unknown"
        new_seri=Series(name,director,imdb_score,url,year,casts,session)
        series_ram.append(new_seri)  
    if code_identify==3: 
        new_docc=Documentary(name,director,imdb_score,url,year,casts)
        documentary_ram.append(new_docc)
    if code_identify==4:
        new_clip=Clip(name,director,imdb_score,url,year,casts)
        clip_ram.append(new_clip)


  




def edit():
    code_identify=int(input("which do you want to Edit?\n Edit film press 1\n Edit series press 2\n Edit documentary press 3\n Edit clip press 4\n Edit actor press 5"))
    if code_identify==5:
        i=0
        for actor in actor_ram:
            i+=1
            print(f'{i}-{actor.name}{actor.lastname}')
        i=int(input("please enter the actor number that you want to edit:"))

        if i <= len(actor_ram) and i>0:
            name= input("enter new name: ")
            lastname= input("enter new lastname: ")
            film= input("enter new films of this actor:\n(if you want to enter more than 1 film, put a '-' between films) ")
            age= input("enter new age: ")               
            married= input("enter new married status: ") 
            action_time= input("enter new action_time: ")   
            save_edit=input(f'New content for {actor_ram[i-1].name}{actor_ram[i-1].lastname} will be the below items:\nname={name}\nlastname={lastname}\nfilm={film}\nage={age}\nmarried={married}\naction_time={action_time}\n Save: press (Y)  Dont save: press other key')
            if save_edit=='Y':
                if name!='': actor_ram[i-1].name=name
                if lastname!='': actor_ram[i-1].lastname=lastname
                if film!='': actor_ram[i-1].film=film
                if age!='': actor_ram[i-1].age=age    
                if married!='': actor_ram[i-1].married=married
                if action_time!='': actor_ram[i-1].action_time=action_time    
                new_object=f'{actor_ram[i-1].name}{actor_ram[i-1].lastname}'    
                new_object=Actor(actor_ram[i-1].name,actor_ram[i-1].lastname,actor_ram[i-1].film,actor_ram[i-1].age,actor_ram[i-1].married,actor_ram[i-1].action_time)               
                actor_ram[i-1]=new_object
        else:
            print("The number you have chosen doesnt belong to any actor")

    if code_identify==1:
        i=0
        for film in films_ram:
            i+=1
            print(f'{i}-{film.name}')
        i=int(input("please enter the film number that you want to edit:"))

        if i <= len(films_ram) and i>0:
            name= input("enter new name: ")
            director= input("enter new director: ")
            imdb_score= input("enter new imdb_score: ") 
            url= input("enter new url: ") 
            year= input("enter new year: ") 
            casts= input("enter new casts of this film:\n(if you want to enter more than 1 cast, put a '-' between casts) ")
            genre= input("enter new genre: ") 
            duration= input("enter new duration: ")               
            save_edit=input(f'New content for {films_ram[i-1].name} will be the below items:\nname={name}\ndirector={director}\nimdb_score={imdb_score}\nurl={url}\nyear={year}\ncasts={casts}\ngenre={genre}\nduration={duration}\n Save: press (Y)  Dont save: press other key\n')
            if save_edit=='Y':
                if name!='': films_ram[i-1].name=name
                if director!='': films_ram[i-1].director=director
                if imdb_score!='': films_ram[i-1].imdb_score=imdb_score
                if url!='': films_ram[i-1].url=url    
                if year!='': films_ram[i-1].year=year 
                if casts!='': 
                    films_ram[i-1].casts=change_stringactor_to_class(casts,[name])
                if genre!='': films_ram[i-1].genre=genre   
                if duration!='': films_ram[i-1].duration=duration  
                new_object=f'{films_ram[i-1].name}'    
                new_object=Film(films_ram[i-1].name,films_ram[i-1].director,films_ram[i-1].imdb_score,films_ram[i-1].url,films_ram[i-1].year,films_ram[i-1].casts,films_ram[i-1].genre,films_ram[i-1].duration)               
                films_ram[i-1]=new_object                                     
        else:
            print("The number you have chosen doesnt belong to any film")
    if code_identify==2:
        i=0
        for seri in series_ram:
            i+=1
            print(f'{i}-{seri.name}')
        i=int(input("please enter the series number that you want to edit:"))

        if i <= len(series_ram) and i>0:
            name= input("enter new name: ")
            director= input("enter new director: ")
            imdb_score= input("enter new imdb_score: ") 
            url= input("enter new url: ") 
            year= input("enter new year: ") 
            casts= input("enter new casts of this series:\n(if you want to enter more than 1 cast, put a '-' between casts) ")
            session= input("enter new session number: ")            
            save_edit=input(f'New content for {series_ram[i-1].name} will be the below items:\nname={name}\ndirector={director}\nimdb_score={imdb_score}\nurl={url}\nyear={year}\ncasts={casts}\session={session}\n Save: press (Y)  Dont save: press other key')
            if save_edit=='Y':
                if name!='': series_ram[i-1].name=name
                if director!='': series_ram[i-1].director=director
                if imdb_score!='': series_ram[i-1].imdb_score=imdb_score
                if url!='': series_ram[i-1].url=url    
                if year!='': series_ram[i-1].year=year  
                if casts!='': series_ram[i-1].casts=change_stringactor_to_class(casts)
                if session!='': series_ram[i-1].session=session  
                new_object=f'{series_ram[i-1].name}'    
                new_object=Series(series_ram[i-1].name,series_ram[i-1].director,series_ram[i-1].imdb_score,series_ram[i-1].url,series_ram[i-1].year,series_ram[i-1].casts,series_ram[i-1].session)               
                series_ram[i-1]=new_object                         
        else:
            print("The number you have chosen doesnt belong to any series")
    if code_identify==3:
        i=0
        for doc in documentary_ram:
            i+=1
            print(f'{i}-{doc.name}')
        i=int(input("please enter the documentary number that you want to edit:"))

        if i <= len(documentary_ram) and i>0:
            name= input("enter new name: ")
            director= input("enter new director: ")
            imdb_score= input("enter new imdb_score: ") 
            url= input("enter new url: ") 
            year= input("enter new year: ") 
            casts= input("enter new casts of this documentary:\n(if you want to enter more than 1 cast, put a '-' between casts) ")      
            save_edit=input(f'New content for {documentary_ram[i-1].name} will be the below items:\nname={name}\ndirector={director}\nimdb_score={imdb_score}\nurl={url}\nyear={year}\ncasts={casts}\n Save: press (Y)  Dont save: press other key')
            if save_edit=='Y':
                if name!='': documentary_ram[i-1].name=name
                if director!='': documentary_ram[i-1].director=director
                if imdb_score!='': documentary_ram[i-1].imdb_score=imdb_score
                if url!='': documentary_ram[i-1].url=url    
                if year!='': documentary_ram[i-1].year=year  
                if casts!='': documentary_ram[i-1].casts=change_stringactor_to_class(casts)    
                new_object=f'{documentary_ram[i-1].name}'    
                new_object=Documentary(documentary_ram[i-1].name,documentary_ram[i-1].director,documentary_ram[i-1].imdb_score,documentary_ram[i-1].url,documentary_ram[i-1].year,documentary_ram[i-1].casts)               
                documentary_ram[i-1]=new_object                    
        else:
            print("The number you have chosen doesnt belong to any documentary")
    if code_identify==4:
        i=0
        for clip in clip_ram:
            i+=1
            print(f'{i}-{clip.name}')
        i=int(input("please enter the clip number that you want to edit:"))

        if i <= len(clip_ram) and i>0:
            name= input("enter new name: ")
            director= input("enter new director: ")
            imdb_score= input("enter new imdb_score: ") 
            url= input("enter new url: ") 
            year= input("enter new year: ") 
            casts= input("enter new casts of this clip:\n(if you want to enter more than 1 cast, put a '-' between casts) ")         
            save_edit=input(f'New content for {clip_ram[i-1].name} will be the below items:\nname={name}\ndirector={director}\nimdb_score={imdb_score}\nurl={url}\nyear={year}\ncasts={casts}\n Save: press (Y)  Dont save: press other key')
            if save_edit=='Y':
                if name!='': clip_ram[i-1].name=name
                if director!='': clip_ram[i-1].director=director
                if imdb_score!='': clip_ram[i-1].imdb_score=imdb_score
                if url!='': clip_ram[i-1].url=url 
                if year!='': clip_ram[i-1].year=year    
                if casts!='': clip_ram[i-1].casts=change_stringactor_to_class(casts)   
                new_object=f'{clip_ram[i-1].name}'    
                new_object=Clip(clip_ram[i-1].name,clip_ram[i-1].director,clip_ram[i-1].imdb_score,clip_ram[i-1].url,clip_ram[i-1].year,clip_ram[i-1].casts)               
                clip_ram[i-1]=new_object                       
        else:
            print("The number you have chosen doesnt belong to any clip")
            
            
    
def remove():
    remove_item=int(input("You can choose one of these categories to delete an item from that category:\n film press 1\n series press 2\n documentary press 3\n clip press 4\n actor press 5 "))
    finished_remove='Y'
    while finished_remove == 'Y':
        if remove_item==1:
            i=0
            for film in films_ram:
                i+=1
                print(f'{i}-{film.name}')
            choose_item=int(input("Enter the film number that you want to delete: "))
            films_ram.pop(choose_item-1)
        elif remove_item==2:
            i=0
            for seri in series_ram:
                i+=1
                print(f'{i}-{seri.name}')
            choose_item=int(input("Enter the series number that you want to delete: "))
            series_ram.pop(choose_item-1)
        elif remove_item==3:
            i=0
            for doc in documentary_ram:
                i+=1
                print(f'{i}-{doc.name}')
            choose_item=int(input("Enter the documentary number that you want to delete: "))
            documentary_ram.pop(choose_item-1)
        elif remove_item==4:
            i=0
            for clip in clip_ram:
                i+=1
                print(f'{i}-{clip.name}')
            choose_item=int(input("Enter the clip number that you want to delete: "))
            clip_ram.pop(choose_item-1)
        elif remove_item==5:
            i=0
            for actor in actor_ram:
                i+=1
                print(f'{i}-{actor.name}{actor.lastname}')
            choose_item=int(input("Enter the actor number that you want to delete: "))
            actor_ram.pop(choose_item-1)


        finished_remove = input("Do you want to continue?\n  Y for continue\n  else for finish\n")
    print("Removing is done.")
    
def search():
    user_input=int(input("for searching enter 1\nfor advanced searching enter 2\n"))
    if user_input==1:
        searchkey=input("You can search for the following items by name of a\nfilm\nseries\ndocumentary\nclip\nactor.\nSo enter a word: ")
        for i in films_ram:
            if i.name==searchkey:
                show_request=input('There is a film.\n Do you want to see its information? (Y)for yes and (N)for No')
                if show_request=='Y':
                    castlist_for_show=[]
                    if i.casts[0]!='None':    
                        for j in range(len(i.casts)):
                            castlist_for_show.append(f'{i.casts[j].name}{i.casts[j].lastname}')
                    else:
                        castlist_for_show.append('None')

                    print("\nType: ",'FILM','\n',
                        "name: ",f"{i.name}",'\n',
                        "director: ",f"{i.director}",'\n',
                        "imdb_score: ",f"{i.imdb_score}",'\n',
                        "url: ",f"{i.url}",'\n',
                        "year: ",f"{i.year}",'\n',
                        "genre: ",f"{i.genre}",'\n',
                        "duration: ",f"{i.duration}",'\n',
                        "casts: ",f"{castlist_for_show}")
                break
        else:
            for i in series_ram:
                if i.name==searchkey:
                    show_request=input('There is a series.\n Do you want to see its information? (Y)for yes and (N)for No')
                    if show_request=='Y':
                        castlist_for_show=[]
                        if i.casts[0]!='None':    
                            for j in range(len(i.casts)):
                                castlist_for_show.append(f'{i.casts[j].name}{i.casts[j].lastname}')
                        else:
                            castlist_for_show.append('None')
                        print("\nType: ",'SERIES','\n',
                        "name: ",f"{i.name}",'\n',
                        "director: ",f"{i.director}",'\n',
                        "imdb_score: ",f"{i.imdb_score}",'\n',
                        "url: ",f"{i.url}",'\n',
                        "year: ",f"{i.year}",'\n',
                        "session: ",f"{i.session}",'\n',
                        "casts: ",f"{castlist_for_show}")
                    break
            else:
                for i in documentary_ram:
                    if i.name==searchkey:
                        show_request=input('There is a documentary.\n Do you want to see its information? (Y)for yes and (N)for No')
                        if show_request=='Y':
                            castlist_for_show=[]
                            if i.casts[0]!='None':    
                                for j in range(len(i.casts)):
                                    castlist_for_show.append(f'{i.casts[j].name}{i.casts[j].lastname}')
                            else:
                                castlist_for_show.append('None')
                            print("\nType: ",'DOCUMENTARY','\n',
                            "name: ",f"{i.name}",'\n',
                            "director: ",f"{i.director}",'\n',
                            "imdb_score: ",f"{i.imdb_score}",'\n',
                            "url: ",f"{i.url}",'\n',
                            "year: ",f"{i.year}",'\n',
                            "casts: ",f"{castlist_for_show}")
                        break
                else:
                    for i in clip_ram:
                        if i.name==searchkey:
                            show_request=input('There is a clip.\n Do you want to see its information? (Y)for yes and (N)for No')
                            if show_request=='Y':
                                castlist_for_show=[]
                                if i.casts[0]!='None':    
                                    for j in range(len(i.casts)):
                                        castlist_for_show.append(f'{i.casts[j].name}{i.casts[j].lastname}')
                                else:
                                    castlist_for_show.append('None')
                                print("\nType: ",'CLIP','\n',
                                "name: ",f"{i.name}",'\n',
                                "director: ",f"{i.director}",'\n',
                                "imdb_score: ",f"{i.imdb_score}",'\n',
                                "url: ",f"{i.url}",'\n',
                                "year: ",f"{i.year}",'\n',
                                "casts: ",f"{castlist_for_show}")
                            break
                    else:
                        for i in actor_ram:
                            if f'{i.name} {i.lastname}'==searchkey:
                                show_request=input('There is an actor.\n Do you want to see its information? (Y)for yes and (N)for No')
                                if show_request=='Y':
                                    print("name"," "*(20-len("name")),
                                        "lastname"," "*(20-len("lastname")),
                                            "age"," "*(20-len("age")),
                                            "married"," "*(20-len("married")),
                                            "action_time"," "*(20-len("action_time")),
                                            "film"," "*(100-len("film")))
                                    print(f"{i.name}"," "*(20-len(i.name)),
                                            f"{i.lastname}"," "*(20-len(i.lastname)),
                                            f"{i.age}"," "*(20-len(i.age)),
                                            f"{i.married}"," "*(20-len(i.married)),
                                            f"{i.action_time}"," "*(20-len(i.action_time)),
                                            f"{i.film}"," "*(100-len(i.film)))
                                break
                        else:
                            print("there is nothing match with your word")
    if user_input==2:
        searchkey1=int(input("Enter first time in minute: "))        
        searchkey2=int(input("Enter second time in minute: ")) 
        searchkey_3=[searchkey1,searchkey2]
        searchkey_3.sort()
        for i in films_ram:
            if int(i.duration)>searchkey_3[0] and int(i.duration)<searchkey_3[1]:
                print(f'time of {i.name} is in your range')

    
def show_list():
    
    for i in films_ram:
        castlist_for_show=[]
        if i.casts[0]!='None':    
            for j in range(len(i.casts)):
                castlist_for_show.append(f'{i.casts[j].name}{i.casts[j].lastname}')
        else:
            castlist_for_show.append('None')

        print("\nType: ",'FILM','\n',
              "name: ",f"{i.name}",'\n',
              "director: ",f"{i.director}",'\n',
              "imdb_score: ",f"{i.imdb_score}",'\n',
               "url: ",f"{i.url}",'\n',
               "year: ",f"{i.year}",'\n',
               "genre: ",f"{i.genre}",'\n',
               "duration: ",f"{i.duration}",'\n',
               "casts: ",f"{castlist_for_show}")
    for i in series_ram:
        castlist_for_show=[]
        if i.casts[0]!='None':    
            for j in range(len(i.casts)):
                castlist_for_show.append(f'{i.casts[j].name}{i.casts[j].lastname}')
        else:
            castlist_for_show.append('None')
        print("\nType: ",'SERIES','\n',
        "name: ",f"{i.name}",'\n',
        "director: ",f"{i.director}",'\n',
        "imdb_score: ",f"{i.imdb_score}",'\n',
        "url: ",f"{i.url}",'\n',
        "year: ",f"{i.year}",'\n',
        "session: ",f"{i.session}",'\n',
        "casts: ",f"{castlist_for_show}")
    for i in documentary_ram:
        castlist_for_show=[]
        if i.casts[0]!='None':    
            for j in range(len(i.casts)):
                castlist_for_show.append(f'{i.casts[j].name}{i.casts[j].lastname}')
        else:
            castlist_for_show.append('None')
        print("\nType: ",'DOCUMENTARY','\n',
        "name: ",f"{i.name}",'\n',
        "director: ",f"{i.director}",'\n',
        "imdb_score: ",f"{i.imdb_score}",'\n',
        "url: ",f"{i.url}",'\n',
        "year: ",f"{i.year}",'\n',
        "casts: ",f"{castlist_for_show}")
    for i in clip_ram:
        castlist_for_show=[]
        if i.casts[0]!='None':    
            for j in range(len(i.casts)):
                castlist_for_show.append(f'{i.casts[j].name}{i.casts[j].lastname}')
        else:
            castlist_for_show.append('None')
        print("\nType: ",'CLIP','\n',
        "name: ",f"{i.name}",'\n',
        "director: ",f"{i.director}",'\n',
        "imdb_score: ",f"{i.imdb_score}",'\n',
        "url: ",f"{i.url}",'\n',
        "year: ",f"{i.year}",'\n',
        "casts: ",f"{castlist_for_show}")
    print()
    print("Type"," "*(10-len("Type")),
            "name"," "*(20-len("name")),
            "lastname"," "*(20-len("lastname")),
            "age"," "*(20-len("age")),
            "married"," "*(20-len("married")),
            "action_time"," "*(20-len("action_time")),
            "film"," "*(20-len("film")))
    for v,i in enumerate(actor_ram):
        if v==0:
            print("Actor"," "*(11-len("Actor")),end="")
        else:
            print(" "*(12),end="")
        print(f"{i.name}"," "*(20-len(i.name)),
                f"{i.lastname}"," "*(20-len(i.lastname)),
                f"{i.age}"," "*(20-len(i.age)),
                f"{i.married}"," "*(20-len(i.married)),
                f"{i.action_time}"," "*(20-len(i.action_time)),
                f"{i.film}"," "*(20-len(i.film)))   



def download():
    search_media=int(input('which media do you want to download(Enter its number):\n1-Film\n2-Series\n3-Documentary\n4-Clip'))
    if search_media==1:
        for v,i in enumerate(films_ram):
            print(f'{v+1}_{i.name}')
        film_number=int(input('Enter the film number you want to download: '))
        print(f'downloading from {films_ram[film_number-1].url}')
        link=films_ram[film_number-1].url
        first_stream=pytube.YouTube(link).streams.first()
        first_stream.download(output_path='./',filename=f'{films_ram[film_number-1].name}')
    elif search_media==2:
        for v,i in enumerate(series_ram):
            print(f'{v+1}_{i.name}')
        series_number=int(input('Enter the series number you want to download: '))
        print(f'downloading from {series_ram[series_number-1].url}')
        link=series_ram[series_number-1].url
        first_stream=pytube.YouTube(link).streams.first()
        first_stream.download(output_path='./',filename=f'{series_ram[series_number-1].name}')
    elif search_media==3:
        for v,i in enumerate(documentary_ram):
            print(f'{v+1}_{i.name}')
        documentary_number=int(input('Enter the documentary number you want to download: '))
        print(f'downloading from {documentary_ram[documentary_number-1].url}')
        link=documentary_ram[documentary_number-1].url
        first_stream=pytube.YouTube(link).streams.first()
        first_stream.download(output_path='./',filename=f'{documentary_ram[documentary_number-1].name}')
    elif search_media==4:
        for v,i in enumerate(clip_ram):
            print(f'{v+1}_{i.name}')
        clip_number=int(input('Enter the clip number you want to download: '))
        print(f'downloading from {clip_ram[clip_number-1].url}')        
        link=clip_ram[clip_number-1].url
        first_stream=pytube.YouTube(link).streams.first()
        first_stream.download(output_path='./',filename=f'{clip_ram[clip_number-1].name}')

            
    
print("Welcome to Media store")
print("Loading...")
read_from_database()
print("Data Loaded.")
while True:

    show_menu()

    choice=int(input("Enter your choice: "))

    if choice==1:
        add()
    elif choice==2:
        edit()
    elif choice==3:
        remove()   
    elif choice==4:
        search()
    elif choice==5:
        show_list()
    elif choice==6:
        download()
    elif choice==7:
        write_to_database()
        exit(0)
    else:
        print("Please enter a number betwwen 1 to 7")
# print(PRODUCTS)

# for product in PRODUCTS:
#     print(product)
import sqlite3
import pytube



def load_database():
    global connection
    global my_cursur
    connection=sqlite3.connect("media_database.db")
    my_cursur=connection.cursor()
    
          
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
    
    if code_identify==5:
        name= input("Enter name: ")
        lastname= input("Enter lastname: ")
        films=''
        films=input("Enter film: ")
        if films=='':
            ...
        if films != '' :
            while True:
                film_number=input('Do you want to add another film?\nY for yes\nN for No')
                if film_number=='Y' or film_number=='y':
                    films+='-'+input("Enter film: ")
                else:
                    break
        age=input("Enter age: ")
        married=input("Enter married status: ")
        action_time=input("Enter action_time: ")


        my_cursur.execute(f"INSERT INTO actors (name, lastname, films, age, maritalstatus, actingyears) VALUES ( '{name}' , '{lastname}' , '{films}' , '{age}' , '{married}' , '{action_time}' )")
        

    
    if code_identify==1 or code_identify==2 or code_identify==3 or code_identify==4:
        name= input("Enter name: ")
        director= input("Enter director: ")
        imdb_score= input("Enter imdb_score: ")
        url= input("Enter url: ")
        year= input("Enter year of produce: ")
        casts=input("Enter actor name and lastname that play in this media:\n ")
        if casts=='':
            ...
        if casts != '' :
            while True:
                cast_number=input('Do you want to add another actor?\nY for yes\nN for No\n')
                if cast_number=='Y' or cast_number=='y':
                    casts+='-'+input("Enter actor name and lastname:\n ")
                else:
                    break



    if code_identify==1: 
        genre= input("Enter genre: ")
        duration=input("Enter duration: ")
        my_cursur.execute(f"INSERT INTO films (name, director, rate, link, year, actors, genre, duration) VALUES ( '{name}' , '{director}' , '{imdb_score}' , '{url}' , '{year}' , '{casts}' , '{genre}' , '{duration}' )")
        

    if code_identify==2: 
        session= input("Enter session: ")

        my_cursur.execute(f"INSERT INTO series (name, director, rate, link, year, actors, session) VALUES ('{name}','{director}','{imdb_score}','{url}','{year}','{casts}','{session}')")
        
    if code_identify==3: 
        my_cursur.execute(f"INSERT INTO documentries (name, director, rate, link, year, actors) VALUES ('{name}','{director}','{imdb_score}','{url}','{year}','{casts}')")
        
    if code_identify==4:
        my_cursur.execute(f"INSERT INTO clips (name, director, rate, link, year, actors) VALUES ('{name}','{director}','{imdb_score}','{url}','{year}','{casts}')")
    connection.commit()



  




def edit():
    code_identify=int(input("which do you want to Edit?\n Edit film press 1\n Edit series press 2\n Edit documentary press 3\n Edit clip press 4\n Edit actor press 5"))
    if code_identify==5:

        actor=my_cursur.execute("SELECT * FROM actors")
        actorss=actor.fetchall()
        i=0
        for j in actorss:
            i+=1
            print(f'{i}-{j[0]}{j[1]}')

        actornum=int(input("please enter the actor number that you want to edit:"))

        if actornum>0 and actornum<=len(actorss):
            id_actor=actorss[actornum-1][6]
            namet= input("enter new name: ")
            lastnamet= input("enter new lastname: ")
            filmt= input("enter new films of this actor:\n(if you want to enter more than 1 film, put a '-' between films) ")
            aget= input("enter new age: ")               
            married= input("enter new married status: ") 
            action_time= input("enter new action_time: ")   
            save_edit=input(f'New content for {actorss[actornum-1][0]}{actorss[actornum-1][1]} will be the nonempty below items:\nname={namet}\nlastname={lastnamet}\nfilm={filmt}\nage={aget}\nmarried={married}\naction_time={action_time}\n Save: press (Y)  Dont save: press other key')
            if save_edit=='Y':
                if namet!='': my_cursur.execute(f"UPDATE actors SET name= '{namet}' WHERE id='{id_actor}'")
                if lastnamet!='': my_cursur.execute(f"UPDATE actors SET lastname='{lastnamet}' WHERE id='{id_actor}'")
                if filmt!='': my_cursur.execute(f"UPDATE actors SET films= '{filmt}' WHERE id='{id_actor}'")
                if aget!='': my_cursur.execute(f"UPDATE actors SET age= '{aget}' WHERE id='{id_actor}'")   
                if married!='': my_cursur.execute(f"UPDATE actors SET maritalstatus= '{married}' WHERE id='{id_actor}'") 
                if action_time!='': my_cursur.execute(f"UPDATE actors SET actingyears= '{action_time}' WHERE id='{id_actor}'")   
                connection.commit()
        else:
            print("The number you have chosen doesnt belong to any actor")

    if code_identify==1:
        film=my_cursur.execute("SELECT * FROM films")
        filmss=film.fetchall()
        i=0
        for j in filmss:
            i+=1
            print(f'{i}-{j[1]}')
        filmnum=int(input("please enter the film number that you want to edit:"))

        if filmnum <= len(filmss) and filmnum>0:
            id_film=filmss[filmnum-1][0]
            name= input("enter new name: ")
            director= input("enter new director: ")
            imdb_score= input("enter new imdb_score: ") 
            url= input("enter new url: ") 
            year= input("enter new year: ") 
            casts= input("enter new casts of this film:\n(if you want to enter more than 1 cast, put a '-' between casts) ")
            genre= input("enter new genre: ") 
            duration= input("enter new duration: ")               
            save_edit=input(f'New content for {filmss[filmnum-1][1]} will be the below items:\nname={name}\ndirector={director}\nimdb_score={imdb_score}\nurl={url}\nyear={year}\ncasts={casts}\ngenre={genre}\nduration={duration}\n Save: press (Y)  Dont save: press other key\n')
            if save_edit=='Y':
                if name!='': my_cursur.execute(f"UPDATE films SET name= '{name}' WHERE id= {id_film}")
                if director!='': my_cursur.execute(f"UPDATE films SET director= '{director}' WHERE id= {id_film}")
                if imdb_score!='': my_cursur.execute(f"UPDATE films SET rate='{imdb_score}' WHERE id= {id_film}")
                if url!='': my_cursur.execute(f"UPDATE films SET link='{url}' WHERE id= {id_film}")
                if year!='': my_cursur.execute(f"UPDATE films SET year='{year}' WHERE id= {id_film}")
                if casts!='':  my_cursur.execute(f"UPDATE films SET actors='{casts}' WHERE id= {id_film}")
                if genre!='': my_cursur.execute(f"UPDATE films SET genre='{genre}' WHERE id= {id_film}")
                if duration!='': my_cursur.execute(f"UPDATE films SET duration='{duration}' WHERE id= {id_film}")
                connection.commit()                
        else:
            print("The number you have chosen doesnt belong to any film")
    if code_identify==2:
        seri=my_cursur.execute("SELECT * FROM series")
        seriess=seri.fetchall()
        i=0
        for j in seriess:
            i+=1
            print(f'{i}-{j[1]}')
        serinum=int(input("please enter the series number that you want to edit:"))

        if serinum <= len(seriess) and serinum>0:
            id_seri=seriess[serinum-1][0]
            name= input("enter new name: ")
            director= input("enter new director: ")
            imdb_score= input("enter new imdb_score: ") 
            url= input("enter new url: ") 
            year= input("enter new year: ") 
            casts= input("enter new casts of this series:\n(if you want to enter more than 1 cast, put a '-' between casts) ")
            session= input("enter new session number: ")            
            save_edit=input(f'New content for {seriess[serinum-1][1]} will be the below items:\nname={name}\ndirector={director}\nimdb_score={imdb_score}\nurl={url}\nyear={year}\ncasts={casts}\session={session}\n Save: press (Y)  Dont save: press other key')
            if save_edit=='Y':
                if name!='': my_cursur.execute(f"UPDATE series SET name='{name}' WHERE id={id_seri}")
                if director!='': my_cursur.execute(f"UPDATE series SET director='{director}' WHERE id={id_seri}")
                if imdb_score!='': my_cursur.execute(f"UPDATE series SET rate='{imdb_score}' WHERE id={id_seri}")
                if url!='': my_cursur.execute(f"UPDATE series SET link='{url}' WHERE id={id_seri}")
                if year!='': my_cursur.execute(f"UPDATE series SET year='{year}' WHERE id={id_seri}")
                if casts!='':  my_cursur.execute(f"UPDATE series SET actors='{casts}' WHERE id={id_seri}")
                if session!='': my_cursur.execute(f"UPDATE series SET session='{session}' WHERE id={id_seri}")
                connection.commit()                       
        else:
            print("The number you have chosen doesnt belong to any series")
    if code_identify==3:
        doci=my_cursur.execute("SELECT * FROM documentries")
        docss=doci.fetchall()
        i=0
        for j in docss:
            i+=1
            print(f'{i}-{j[1]}')
        docnum=int(input("please enter the documentary number that you want to edit:"))

        if docnum <= len(docss) and docnum>0:
            id_doc=docss[docnum-1][0]
            name= input("enter new name: ")
            director= input("enter new director: ")
            imdb_score= input("enter new imdb_score: ") 
            url= input("enter new url: ") 
            year= input("enter new year: ") 
            casts= input("enter new casts of this documentary:\n(if you want to enter more than 1 cast, put a '-' between casts) ")      
            save_edit=input(f'New content for {docss[docnum-1][1]} will be the below items:\nname={name}\ndirector={director}\nimdb_score={imdb_score}\nurl={url}\nyear={year}\ncasts={casts}\n Save: press (Y)  Dont save: press other key')
            if save_edit=='Y':
                if name!='': my_cursur.execute(f"UPDATE documentries SET name='{name}' WHERE id={id_doc}")
                if director!='': my_cursur.execute(f"UPDATE documentries SET director='{director}' WHERE id={id_doc}")
                if imdb_score!='': my_cursur.execute(f"UPDATE documentries SET rate='{imdb_score}' WHERE id={id_doc}")
                if url!='': my_cursur.execute(f"UPDATE documentries SET link='{url}' WHERE id={id_doc}")
                if year!='': my_cursur.execute(f"UPDATE documentries SET year='{year}' WHERE id={id_doc}")
                if casts!='':  my_cursur.execute(f"UPDATE documentries SET actors='{casts}' WHERE id={id_doc}")
                connection.commit()   
        else:
            print("The number you have chosen doesnt belong to any documentary")
    if code_identify==4:
        clip=my_cursur.execute("SELECT * FROM clips")
        clipss=clip.fetchall()
        i=0
        for j in clipss:
            i+=1
            print(f'{i}-{j[1]}')
        clipnum=int(input("please enter the clip number that you want to edit:"))

        if clipnum <= len(clipss) and clipnum>0:
            id_clip=clipss[clipnum-1][0]
            name= input("enter new name: ")
            director= input("enter new director: ")
            imdb_score= input("enter new imdb_score: ") 
            url= input("enter new url: ") 
            year= input("enter new year: ") 
            casts= input("enter new casts of this clip:\n(if you want to enter more than 1 cast, put a '-' between casts) ")         
            save_edit=input(f'New content for {clipss[clipnum-1][1]} will be the below items:\nname={name}\ndirector={director}\nimdb_score={imdb_score}\nurl={url}\nyear={year}\ncasts={casts}\n Save: press (Y)  Dont save: press other key')
            if save_edit=='Y':
                if name!='': my_cursur.execute(f"UPDATE clips SET name='{name}' WHERE id={id_clip}")
                if director!='': my_cursur.execute(f"UPDATE clips SET director='{director}' WHERE id={id_clip}")
                if imdb_score!='': my_cursur.execute(f"UPDATE clips SET rate='{imdb_score}' WHERE id={id_clip}")
                if url!='': my_cursur.execute(f"UPDATE clips SET link='{url}' WHERE id={id_clip}")
                if year!='': my_cursur.execute(f"UPDATE clips SET year='{year}' WHERE id={id_clip}")
                if casts!='':  my_cursur.execute(f"UPDATE clips SET actors='{casts}' WHERE id={id_clip}")
                connection.commit()                       
        else:
            print("The number you have chosen doesnt belong to any clip")
            
            
    
def remove():
    remove_item=int(input("You can choose one of these categories to delete an item from that category:\n film press 1\n series press 2\n documentary press 3\n clip press 4\n actor press 5 "))
    finished_remove='Y'
    while finished_remove == 'Y':
        if remove_item==1:
            film=my_cursur.execute("SELECT * FROM films")
            filmss=film.fetchall()
            i=0
            for j in filmss:
                i+=1
                print(f'{i}-{j[1]}')
            choose_item=int(input("Enter the film number that you want to delete: "))
            my_cursur.execute(f"DELETE FROM films WHERE id='{filmss[choose_item-1][0]}'")
            connection.commit()
        elif remove_item==2:
            seri=my_cursur.execute("SELECT * FROM series")
            seriess=seri.fetchall()
            i=0
            for j in seriess:
                i+=1
                print(f'{i}-{j[1]}')
            choose_item=int(input("Enter the series number that you want to delete: "))
            my_cursur.execute(f"DELETE FROM series WHERE id='{seriess[choose_item-1][0]}'")
            connection.commit()
        elif remove_item==3:
            doc=my_cursur.execute("SELECT * FROM documentries")
            documentriess=doc.fetchall()
            i=0
            for j in documentriess:
                i+=1
                print(f'{i}-{j[1]}')
            choose_item=int(input("Enter the documentries number that you want to delete: "))
            my_cursur.execute(f"DELETE FROM documentries WHERE id='{documentriess[choose_item-1][0]}'")
            connection.commit()
        elif remove_item==4:
            clip=my_cursur.execute("SELECT * FROM clips")
            clipss=clip.fetchall()
            i=0
            for j in clipss:
                i+=1
                print(f'{i}-{j[1]}')
            choose_item=int(input("Enter the clips number that you want to delete: "))
            my_cursur.execute(f"DELETE FROM clips WHERE id='{clipss[choose_item-1][0]}'")
            connection.commit()
        elif remove_item==5:
            act=my_cursur.execute("SELECT * FROM actors")
            actorss=act.fetchall()
            i=0
            for j in actorss:
                i+=1
                print(f'{i}-{j[1]}')
            choose_item=int(input("Enter the actors number that you want to delete: "))
            my_cursur.execute(f"DELETE FROM actors WHERE id='{actorss[choose_item-1][6]}'")
            connection.commit()


        finished_remove = input("Do you want to continue?\n  Y for continue\n  else for finish\n")
    print("Removing is done.")
    
def search():
    user_input=int(input("for searching enter 1\nfor advanced searching enter 2\n"))
    if user_input==1:
        searchkey=input("You can search for the following items by name of a\nfilm\nseries\ndocumentary\nclip\nactor.\nSo enter a word: ")
        result=my_cursur.execute("SELECT * FROM films")
        filmss=result.fetchall()
        for film in filmss:
        # for i in films_ram:
            if film[1]==searchkey:
                show_request=input('There is a film.\n Do you want to see its information? (Y)for yes and (N)for No')
                if show_request=='Y':

                    print("\nType: ",'FILM','\n',
                        "name: ",f"{film[1]}",'\n',
                        "director: ",f"{film[2]}",'\n',
                        "imdb_score: ",f"{film[3]}",'\n',
                        "url: ",f"{film[4]}",'\n',
                        "year: ",f"{film[5]}",'\n',
                        "genre: ",f"{film[7]}",'\n',
                        "duration: ",f"{film[8]}",'\n',
                        "casts: ",f"{film[6]}")
                break
        else:
            result=my_cursur.execute("SELECT * FROM series")
            seriess=result.fetchall()
            for seri in seriess:
                if seri[1]==searchkey:
                    show_request=input('There is a series.\n Do you want to see its information? (Y)for yes and (N)for No')
                    if show_request=='Y':
                        print("\nType: ",'SERIES','\n',
                        "name: ",f"{seri[1]}",'\n',
                        "director: ",f"{seri[2]}",'\n',
                        "imdb_score: ",f"{seri[3]}",'\n',
                        "url: ",f"{seri[4]}",'\n',
                        "year: ",f"{seri[5]}",'\n',
                        "session: ",f"{seri[7]}",'\n',
                        "casts: ",f"{seri[6]}")
                    break
            else:
                result=my_cursur.execute("SELECT * FROM documentries")
                docss=result.fetchall()
                for doc in docss:
                    if doc[1]==searchkey:
                        show_request=input('There is a documentary.\n Do you want to see its information? (Y)for yes and (N)for No')
                        if show_request=='Y':
                            print("\nType: ",'DOCUMENTARY','\n',
                            "name: ",f"{doc[1]}",'\n',
                            "director: ",f"{doc[2]}",'\n',
                            "imdb_score: ",f"{doc[3]}",'\n',
                            "url: ",f"{doc[4]}",'\n',
                            "year: ",f"{doc[5]}",'\n',
                            "casts: ",f"{doc[6]}")
                        break
                else:
                    result=my_cursur.execute("SELECT * FROM clips")
                    clipss=result.fetchall()
                    for clip in clipss:
                        if clip[1]==searchkey:
                            show_request=input('There is a clip.\n Do you want to see its information? (Y)for yes and (N)for No')
                            if show_request=='Y':
                                print("\nType: ",'CLIP','\n',
                                "name: ",f"{clip[1]}",'\n',
                                "director: ",f"{clip[2]}",'\n',
                                "imdb_score: ",f"{clip[3]}",'\n',
                                "url: ",f"{clip[4]}",'\n',
                                "year: ",f"{clip[5]}",'\n',
                                "casts: ",f"{clip[6]}")
                            break
                    else:
                        result=my_cursur.execute("SELECT * FROM actors")
                        actorss=result.fetchall()
                        for actor in actorss:
                            if f'{actor[0]} {actor[1]}'==searchkey:
                                show_request=input('There is an actor.\n Do you want to see its information? (Y)for yes and (N)for No')
                                if show_request=='Y':
                                    print("\nType: ",'ACTOR','\n',
                                    "name: ",f"{actor[0]}",'\n',
                                    "lastname: ",f"{actor[1]}",'\n',
                                    "age: ",f"{actor[3]}",'\n',
                                    "married: ",f"{actor[4]}",'\n',
                                    "action_time: ",f"{actor[5]}",'\n',
                                    "film: ",f"{actor[2]}")
                                break
                        else:
                            print("there is nothing match with your word")
    if user_input==2:
        searchkey1=int(input("Enter first time in minute: "))        
        searchkey2=int(input("Enter second time in minute: ")) 
        searchkey_3=[searchkey1,searchkey2]
        searchkey_3.sort()
        result=my_cursur.execute("SELECT * FROM films")
        filmss=result.fetchall()
        for film in filmss:
            if int(film[8])>searchkey_3[0] and int(film[8])<searchkey_3[1]:
                print(f'time of {film[1]} is in your range')

    
def show_list():
    
    result=my_cursur.execute("SELECT * FROM films")
    filmss=result.fetchall()
    result=my_cursur.execute("SELECT * FROM series")
    seriess=result.fetchall()
    result=my_cursur.execute("SELECT * FROM documentries")
    docss=result.fetchall()
    result=my_cursur.execute("SELECT * FROM clips")
    clipss=result.fetchall()
    result=my_cursur.execute("SELECT * FROM actors")
    actorss=result.fetchall()
    for film in filmss:
        print("\nType: ",'FILM','\n',
            "name: ",f"{film[1]}",'\n',
            "director: ",f"{film[2]}",'\n',
            "imdb_score: ",f"{film[3]}",'\n',
            "url: ",f"{film[4]}",'\n',
            "year: ",f"{film[5]}",'\n',
            "genre: ",f"{film[7]}",'\n',
            "duration: ",f"{film[8]}",'\n',
            "casts: ",f"{film[6]}")
    for seri in seriess:
        print("\nType: ",'SERIES','\n',
        "name: ",f"{seri[1]}",'\n',
        "director: ",f"{seri[2]}",'\n',
        "imdb_score: ",f"{seri[3]}",'\n',
        "url: ",f"{seri[4]}",'\n',
        "year: ",f"{seri[5]}",'\n',
        "session: ",f"{seri[7]}",'\n',
        "casts: ",f"{seri[6]}")
    for doc in docss:
        print("\nType: ",'DOCUMENTARY','\n',
        "name: ",f"{doc[1]}",'\n',
        "director: ",f"{doc[2]}",'\n',
        "imdb_score: ",f"{doc[3]}",'\n',
        "url: ",f"{doc[4]}",'\n',
        "year: ",f"{doc[5]}",'\n',
        "casts: ",f"{doc[6]}")
    for clip in clipss:
        print("\nType: ",'CLIP','\n',
        "name: ",f"{clip[1]}",'\n',
        "director: ",f"{clip[2]}",'\n',
        "imdb_score: ",f"{clip[3]}",'\n',
        "url: ",f"{clip[4]}",'\n',
        "year: ",f"{clip[5]}",'\n',
        "casts: ",f"{clip[6]}")
    for actor in actorss:
        print("\nType: ",'ACTOR','\n',
        "name: ",f"{actor[0]}",'\n',
        "lastname: ",f"{actor[1]}",'\n',
        "age: ",f"{actor[3]}",'\n',
        "married: ",f"{actor[4]}",'\n',
        "action_time: ",f"{actor[5]}",'\n',
        "film: ",f"{actor[2]}") 



def download():
    search_media=int(input('which media do you want to download(Enter its number):\n1-Film\n2-Series\n3-Documentary\n4-Clip'))
    if search_media==1:
        result=my_cursur.execute("SELECT * FROM films")
        filmss=result.fetchall()
        for v,i in enumerate(filmss):
            print(f'{v+1}_{i[1]}')
        film_number=int(input('Enter the film number you want to download: '))
        print(f'downloading from {filmss[film_number-1][4]}')
        link=filmss[film_number-1][4]
        first_stream=pytube.YouTube(link).streams.first()
        first_stream.download(output_path='./',filename=f'{filmss[film_number-1][1]}')
    elif search_media==2:
        result=my_cursur.execute("SELECT * FROM series")
        seriess=result.fetchall()
        for v,i in enumerate(seriess):
            print(f'{v+1}_{i[1]}')
        series_number=int(input('Enter the series number you want to download: '))
        print(f'downloading from {seriess[series_number-1][4]}')
        link=seriess[series_number-1][4]
        first_stream=pytube.YouTube(link).streams.first()
        first_stream.download(output_path='./',filename=f'{seriess[series_number-1][1]}')
    elif search_media==3:
        result=my_cursur.execute("SELECT * FROM documentries")
        docss=result.fetchall()
        for v,i in enumerate(docss):
            print(f'{v+1}_{i[1]}')
        documentary_number=int(input('Enter the documentary number you want to download: '))
        print(f'downloading from {docss[documentary_number-1][4]}')
        link=docss[documentary_number-1][4]
        first_stream=pytube.YouTube(link).streams.first()
        first_stream.download(output_path='./',filename=f'{docss[documentary_number-1][1]}')
    elif search_media==4:
        result=my_cursur.execute("SELECT * FROM clips")
        clipss=result.fetchall()
        for v,i in enumerate(clipss):
            print(f'{v+1}_{i[1]}')
        clip_number=int(input('Enter the clip number you want to download: '))
        print(f'downloading from {clipss[clip_number-1][4]}')        
        link=clipss[clip_number-1][4]
        first_stream=pytube.YouTube(link).streams.first()
        first_stream.download(output_path='./',filename=f'{clipss[clip_number-1][1]}')

            
    
print("Welcome to Media store")
print("Loading...")
load_database()
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
        exit(0)
    else:
        print("Please enter a number betwwen 1 to 7")
# print(PRODUCTS)

# for product in PRODUCTS:
#     print(product)
from colorama import Fore
import gtts
import pyttsx3
import playsound
import os
from io import BytesIO


engine = pyttsx3.init() 
def read_from_file():
    global words_bank
    try:
        f= open("input/translate.txt",'r')
        # words=[]
        # for line in f:
        #     words.append(line)

        # big_string = f.read()
        # words=big_string.split("\n")
        #   |
        #   |
        #  \ /

        temp=f.read().split("\n")
        words_bank=[]
        for i in range(0,len(temp),2):
            my_dict={"en":temp[i], "fa":temp[i+1]}
            words_bank.append(my_dict)

        f.close()
        return words_bank
    except FileNotFoundError:
        print(Fore.RED +"\nWords database isn't in input folder!\n"+Fore.WHITE )
        return False

def show_menu():
    print("1. translate English to persian")
    print("2. translate persian to English")
    print("3. add a new word to database")
    print("4. exit")


def translate_english_to_persian():
    user_txt= input("Enter your English text:\n")

    sentences=user_txt.split(".")
    output=''
    for i,sentence in enumerate(sentences):
        user_words=sentence.split(" ")
        for user_word in user_words:
            for word in words_bank:
                if user_word==word['en']:
                    output= output+word['fa']+" "
                    break
            else:
                output= output+user_word+" "
        if i!=len(sentences)-1:
            output= output+"."

    print(Fore.GREEN +output + Fore.WHITE)

    x=gtts.gTTS(output,lang="ar",slow=False)
    x.save("speech_file.mp3")
    playsound.playsound("speech_file.mp3")
    os.remove("speech_file.mp3")

    # engine.say(output)   
    # engine.runAndWait()  
    # speech_file=gtts.gTTS(output,lang="en",slow=False)
    # speech_file.save("speech_file.mp3")  
    # playsound("speech_file.mp3")
    print()

def translate_persian_to_english():
    user_txt= input("Enter your Finglish text:\n")

    sentences=user_txt.split(".")
    output=''
    for i,sentence in enumerate(sentences):
        user_words=sentence.split(" ")
        for user_word in user_words:
            for word in words_bank:
                if user_word==word['fa']:
                    output= output+word['en']+" "
                    break
            else:
                output= output+user_word+" "
        if i!=len(sentences)-1:
            output= output+"."

    print(Fore.GREEN +output + Fore.WHITE)
    x=gtts.gTTS(output,lang="en",slow=False)
    x.save("speech_file.mp3")
    playsound.playsound("speech_file.mp3")
    os.remove("speech_file.mp3")

    # engine.say(output)  
    # engine.runAndWait()  

    # speech_file=gtts.gTTS(output,lang="en",slow=False)
    # speech_file.save("speech_file.mp3")  
    # playsound("speech_file.mp3")
    print()

def add_new_word():
    user_en= input("Enter your new English word:\n")
    user_fa= input("Enter your new Finglish word:\n")

    for word in words_bank:
        if user_en==word['en']:
            print("Your input English word exist in word bank.")
            break
    else:
        my_dict={"en":user_en, "fa":user_fa}
        words_bank.append(my_dict)
        print(Fore.GREEN +"Your Entered word added to word bank of translator." + Fore.WHITE)


word=read_from_file()


if word!=False:
    print("************welcome to translator************")
    while True:
        show_menu()
        try:
            choice = int(input("Enter your choice:\n"))
            if choice ==1:
                translate_english_to_persian()
            elif choice==2:
                translate_persian_to_english()
            elif choice==3:
                add_new_word()
            elif choice==4:
                break
            if 4<choice or choice<1:
                print(Fore.RED +"\nEnter a number between 1 to 4.\n"+Fore.WHITE)
        except:
            print(Fore.RED +"\nEnter a number between 1 to 4.\n"+Fore.WHITE )







import pyfiglet
import random
import time
from colorama import Fore

def show_game():
    for row in game_board:
        for cell in row:
            if cell=="O":
                print(Fore.BLUE +cell, end=" ")
            elif cell =="X":
                print(Fore.RED +cell, end=" ")
            else:
                print(Fore.WHITE +cell, end=" ")
        print(Fore.WHITE )

def check_game(mode):
    for j in range(3):
        if  game_board[j][0]=="X" and game_board[j][1]=="X" and game_board[j][2]=="X" or\
            game_board[0][j]=="X" and game_board[1][j]=="X" and game_board[2][j]=="X" or\
            game_board[0][0]=="X" and game_board[1][1]=="X" and game_board[2][2]=="X" or\
            game_board[0][2]=="X" and game_board[1][1]=="X" and game_board[2][0]=="X":
            print("Player 1 win!")
            return 1
        if  game_board[j][0]=="O" and game_board[j][1]=="O" and game_board[j][2]=="O" or\
            game_board[0][j]=="O" and game_board[1][j]=="O" and game_board[2][j]=="O" or\
            game_board[0][0]=="O" and game_board[1][1]=="O" and game_board[2][2]=="O" or\
            game_board[0][2]=="O" and game_board[1][1]=="O" and game_board[2][0]=="O":
            if mode==1:
                print("Player 2 win!")
            elif mode ==2:
                print("CPU win!")
            return 1
    if Counter==9:
        print("Draw!")
        return 1
    

title=pyfiglet.figlet_format("Tic Tac Toe",font="slant")
print(title)

game_board= [["_","_","_"],
             ["_","_","_"],
             ["_","_","_"]]

show_game()
Counter=0

while True:
    try:
        print("Please select a number:\n1. Player vs Player\n2. CPU vs Player\n3. Exit")
        mode = int(input())
        if mode==3 or mode==2 or mode==1:
            break
    except:
        print("Input is invalid")

if mode!=3:
    start_time=time.time()
    while True:
        print("Player 1")   
        while True:
            try:
                row = int(input("Enter row number:\n"))
                column = int(input("Enter column number:\n"))
            except:
                print("Input is invalid")

            if 0<= row <=2 and 0<=column<=2:
                if game_board[row][column]=="_":
                    game_board[row][column]="X"
                    Counter+=1
                    break
                else:
                    print(" jer nazan :/ ")
            else:
                print("Input is invalid")

        show_game()
        if check_game(mode)==1:
            break
        if mode==1:
            print("Player 2")
            while True:
                try:
                    row = int(input("Enter row number:\n"))
                    column = int(input("Enter column number:\n"))
                except:
                    print("Input is invalid")

                if 0<= row <=2 and 0<=column<=2:
                    if game_board[row][column]=="_":
                        game_board[row][column]="O"
                        Counter+=1
                        break
                    else:
                        print(" jer nazan :/ ")
                else:
                    print("Input is invalid")

            show_game()
            if check_game(mode)==1:
                break
        if mode==2:
            print("\nCPU:")
            while True:

                row = random.randint(0,2)
                column = random.randint(0,2)

                if game_board[row][column]=="_":
                    game_board[row][column]="O"
                    Counter+=1
                    break
 

            show_game()
            if check_game(mode)==1:
                break

    end_time=time.time()
    print(f"The duration of the game is {round(end_time-start_time)} second.")

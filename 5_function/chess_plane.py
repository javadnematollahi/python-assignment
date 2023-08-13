

def chess_plane():
    try:
        n=int(input("Enter width:\n"))
        m=int(input("Enter height:\n"))
    except:
        print("Input is invalid")
    
    chess=[]
    chess_in=[]

    for i in range(n):
        for j in range(m):
            if j%2==i%2:
                chess_in.append("#")
            else:
                chess_in.append("*")
        chess.append(chess_in)
        chess_in=[]


    for i in range(n):
        for j in range(m):
            print(chess[i][j],end="")
            if j==m-1:
                print()
    

chess_plane()

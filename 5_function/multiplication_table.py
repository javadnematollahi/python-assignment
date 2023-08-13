


def multiplication_table():
    try:
        n=int(input("Enter rows number:\n"))
        m=int(input("Enter columns number:\n"))
    except:
        print("Input is invalid")
    
    rows=[]
    columns=[]

    for i in range(n):
        for j in range(m):
            columns.append((i+1)*(j+1))

        rows.append(columns)
        columns=[]

    for row in rows:
        print(row)
    

multiplication_table()
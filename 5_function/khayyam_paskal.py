


def khayyam_paskal():
    try:
        n=int(input("Enter rows number:\n"))
    except:
        print("Input is invalid")

    rows=[]
    cols=[]

    for i in range(n):
        for j in range(i+1):
            if i-1>0 and j-1>=0 and j!=i:
                cols.append(rows[i-1][j-1]+rows[i-1][j])
            else:
                cols.append(1)
        rows.append(cols)
        cols=[]

    for row in rows:
        print(row)


khayyam_paskal()
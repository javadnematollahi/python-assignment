
PRODUCTS = []

def read_from_database():

    f= open("E:/pylearn/7/database.txt",'r')
    for line in f:
        result=line.split(',')
        result[3]=result[3].replace("\n", "")
        my_dict={"code":result[0],"name":result[1],
                 "price":result[2],"count":result[3]}
        PRODUCTS.append(my_dict)
 
    f.close()
 
 
def write_to_database():
    f=open("E:/pylearn/7/database.txt","w+")
    for product in PRODUCTS:
        f.write( ','.join( product.values() ))   #تابع جوین می تواند مقادیر یک لیست یا تاپل یا دیکشنری را تبدیل به یک رشته کند
        f.write('\n')
    f.close()
    
def QR_code_generator():
    product_code=input("Please enter the product code you want to make a QR code of it:\n ")
    for product in PRODUCTS:
        if product_code==product['code']:
            import qrcode 
            qr = qrcode.QRCode(version = 1,
                            box_size = 10,
                            border = 5)
            qr.add_data(product)
            qr.make(fit = True)
            img = qr.make_image(fill_color = 'red', back_color = 'white')
            img.save(f"E:/pylearn/7/{product['name']}.png")
            break
    else:
        print("Your product code is not exist")
    
          
def show_menu():
    print("1_ Add")
    print("2_ Edit")
    print("3_ Remove")
    print("4_ Search")
    print("5_ showlist")
    print("6_ Buy")
    print("7_ QR_code_generator")
    print("8_ Exit")
 
def add():
    code= input("Enter code: ")
    name= input("Enter name: ")
    price= input("Enter price: ")
    count= input("Enter count: ")
    new_product={'code': code, 'name':name, 'price':price,'count':count}
    PRODUCTS.append(new_product)
    
def edit():
    finished_edit='Y'
    while finished_edit == 'Y':
        product_code=input("Please enter the product code you want to edit:\n ")
        for product in PRODUCTS:
            if product['code']== product_code:
                edited_item= int(input("Please type the item number that you want to edit:\n1) name\n2) price\n3) count\n  "))
                if edited_item==1:
                    product['name']=input('Enter new name for this code: ')
                elif edited_item==2:
                    product['price']=input('Enter new price for this code: ')
                elif edited_item==3:
                    product['count']=input('Enter new count for this code: ')
                print(product)
                break
        else:
            print("The product code you enter is not exist")
        finished_edit = input("Do you want to continue?\n  Y for continue\n  else for finish\n")
    print("Your edit is done.")
            
            
    
def remove():
    finished_edit='Y'
    while finished_edit == 'Y':
        product_code=input("Please enter the product code you want to delet:\n ")
        for product in PRODUCTS:
            if product['code']== product_code:
                a=PRODUCTS.index(product)
                PRODUCTS.pop(a)
                print(f"{product['name']} is removed from products")
                # print(a)
        finished_edit = input("Do you want to continue?\n  Y for continue\n  else for finish\n")
    print("Removing is done.")
    
def search():
    user_input=input("type your keyword: ")
    for product in PRODUCTS:
        if product['code']==user_input or product['name']==user_input:
            print(product["code"],",",product["name"],",",product["price"])
            break
    else:
        print('not found')
    
def show_list():
    print("code"," "*(20-len("code")),"name"," "*(20-len("name")),"price"," "*(20-len("price")),"count")  
    for product in PRODUCTS:
       print(product["code"]," "*(20-len(product['code'])),product["name"]," "*(20-len(product['name']))
             ,product["price"]," "*(20-len(product['price'])),product["count"])
def buy():
    buy_list=[]
    
    finished_buy='Y'
    while finished_buy == 'Y':
        product_code=input("Please enter the product code you want to buy:\n ")
        for product in PRODUCTS:
            if product['code']== product_code:
                if(int(product['count'])>0):
                    quantity_of_buying=int(input(f"please enter the number of {product['name']} you will to buy: "))
                    if quantity_of_buying<=int(product['count']):
                        product['count']=str(int(product['count'])-quantity_of_buying)
                        buy_dict={'name':product['name'],'count':quantity_of_buying,
                                  'price of each':product['price'],
                                  'price':quantity_of_buying*int(product['price'])}
                        buy_list.append(buy_dict)
                        factor_show=input('Do you want to see your bill now?\n   Y for see bill\n   else key for doesnt need now\n')
                        if factor_show=='Y':
                            total_price=0
                            for i in range(len(buy_list)):
                                total_price +=int(buy_list[i]['price'])
                                print(buy_list[i])
                            print(f"total price:{total_price}\n")
                    else:
                        print('The number you have entered is out of range!')
                else:
                    print(f"{product['name']} is finished")
            break
        else:
            print(f"There isnt any product code equal to {product_code}")

        finished_buy = input("Do you want to continue or show final bill and finish?\n  Y for continue\n  else for show final bill and finish\n")
    if len(buy_list)>0:
        total_price=0
        for i in range(len(buy_list)):
            total_price +=int(buy_list[i]['price'])
            print(buy_list[i])
        print(f"total price:{total_price}\n")
        print("Surprised: Dont need to pay :)")
    
print("Welcome to javad store")
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
        buy()
    elif choice==7:
        QR_code_generator()
    elif choice==8:
        write_to_database()
        exit(0)
    else:
        print("Please enter a number betwwen 1 to 7")
# print(PRODUCTS)

# for product in PRODUCTS:
#     print(product)
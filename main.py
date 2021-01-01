from Operations import Actions


while True:
    try:
        f = open('Database.txt','r')
        f.close()
        break
    except:
        f = open('Database.txt','w+')
        f.close()

while True:
    print("""
    Hello user! 
    Welcome in the system. Please choose: 
    Login - type 'Y'
    Sign Up - type 'B'
    Log out - type 'E'
    """)

    choice = input(">> ")
    if choice=='Y' or choice=='y':
        point1 = Actions()
        point1.logIn()

    elif choice=='B' or choice=='b':
        point2 = Actions()
        point2.addNewUser()

    elif choice == 'E' or choice=='e':
        quit()
    else:
        print("Try another button")

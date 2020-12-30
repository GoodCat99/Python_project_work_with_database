from Page_01 import Page


class Actions:
    def addNewUser(self):
        user = ''
        print("You start the creation of new account. Welcome! ")

        file = open('Database.txt', 'r')
        data = file.readlines()
        database = []
        for line in data:
            # line_strip = line.strip()
            database.append(line.strip())
        #print(database)

        username = input('Username: ')
        password = input('Password: ')

        for element in database:
            if username in element:
                print("Please try another user or create a new")
                file.close()
                user = 'active'
                break
            else:
                continue

        if user != 'active':
            database.append([username, password])
            print(database)
            with open('Database.txt', 'w') as f:
                for item in database:
                    f.write(str(item) + '\n')
            file.close()
            print("User has been created")

        else:
            print("Please try another user or create a new")

    def logIn(self):
        user = ''
        print("Could you please enter your username and password ?")
        username = input('Username: ')
        password = input('Password: ')
        file = open('Database.txt', 'r')
        data = file.readlines()

        database = []
        for line in data:
            database.append(line.strip())

        for element in database:
            if username in element:
                if password in element:
                    print("You are in the system")
                    file.close()
                    user = 'active'
                    break
            else:
                continue
        if user =='active':
            new_page = Page()
            new_page.new()

        else:
            print("Please try another user or create a new")
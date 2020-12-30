import sqlite3

class Data:

    #creation a connection to the database
    @staticmethod
    def addNewDatabase(database):
        conn = sqlite3.connect(f'{database}')
        conn.close()

    #creation new database with internal details within database
    @staticmethod
    def tableWithData(database):
        conn = sqlite3.connect(f'{database}')
        c = conn.cursor()

        table = input("Please indicate the name of your table: ")

        button_a = input("Do you want to create a new column within the table ? ('Y'('yes')/'N'('no')")

        if button_a == 'Y' or button_a == 'y':
            name_of_column = input("Name of column: ")
            type_of_column = input("Type of column: ")


            c.execute(f'CREATE TABLE {table} ({name_of_column} {type_of_column})')

        elif button_a == 'N' or button_a == 'n':
            print("Please try again")


        while True:
            button_a = input("Do you want to create a new column within the table ? ('Y'('yes')/'N'('no')")

            if button_a == 'Y' or button_a == 'y':
                name_of_column = input("Name of column: ")
                type_of_column = input("Type of column: ")

                c.execute(f'ALTER TABLE {table} ADD COLUMN {name_of_column} {type_of_column}')
            elif button_a == 'N' or button_a == 'n':
                break

        conn.commit()
        conn.close()

    #adding the column for existed database
    @staticmethod
    def addNewColumn(database):
        conn = sqlite3.connect(f'{database}')
        c = conn.cursor()

        table = input("Please indicate the name of your table: ")

        while True:
            button_a = input(f'Do you want to create a new column within the table {table} ? (Y(yes)/N(no)')

            if button_a == 'Y' or button_a == 'y':
                name_of_column = input("Name of column: ")
                type_of_column = input("Type of column: ")

                c.execute(f'ALTER TABLE {table} ADD COLUMN {name_of_column} {type_of_column}')
            elif button_a == 'N' or button_a == 'n':
                break
        conn.commit()
        conn.close()

    #adding the data for columns of table
    @staticmethod
    def addingOfData(database):
        conn = sqlite3.connect(f'{database}')
        c = conn.cursor()
        list_of_variables = []
        table = input("Please indicate the name of your table: ")

        c.execute(f'PRAGMA table_info({table})')
        newList = c.fetchall()

        while True:
            choice_of_adding = input("Do you want to add new data to the table ? (Y/N)")
            if choice_of_adding == 'Y' or choice_of_adding == 'y':
                for element in newList:
                    for item in element:
                        if item == element[1]:
                            a = element[1]
                            variable = input(f'{a}: ')
                            list_of_variables.append(variable)

                conn = sqlite3.connect(f'{database}')
                c = conn.cursor()

                c.execute(f'INSERT INTO {table} VALUES (?,?,?)', list_of_variables)

                conn.commit()
                list_of_variables = []

            elif choice_of_adding == "N" or choice_of_adding == "n":
                break

        conn.close()

    @staticmethod
    def showAllTables(database):
        conn = sqlite3.connect(f'{database}')
        c = conn.cursor()

        c.execute("SELECT name FROM sqlite_master WHERE type = 'table';")

        tables = c.fetchall()

        for element in tables:
            print(element)
        conn.commit()
        conn.close()

    @staticmethod
    def deleteTable(database):
        conn = sqlite3.connect(f'{database}')
        c = conn.cursor()

        print("Could you please indicate the table which you want to delete ?")
        table = input(">> ")

        c.execute(f'DROP TABLE {table}')

        print("The table was deleted")
        input("Please click Enter")

        conn.commit()
        conn.close()







from Database import Data


class Page:
    def new(self):
        database = input("Could you please indicate a name of data base: ")
        Data.addNewDatabase(database)
        print("Database is connected\n")
        print("Existed tables within database: ")
        Data.showAllTables(database)
        input("\nTo continue please click Enter ")

        while True:
            print("-------------------------\n")
            print("Internal menu: ")
            print("""
            1. New Table with new data
            2. Adding of new column for existed table
            3. Data adding for existed table
            4. Deletion of table
            5. Log out
            """)

            choice_01 = input(">> ")

            if choice_01 == '1':
                Data.tableWithData(database)

            elif choice_01 == '2':
                Data.addNewColumn(database)

            elif choice_01 == '3':
                print("Please add new data")
                Data.addingOfData(database)

            elif choice_01 == '4':
                Data.deleteTable(database)

            elif choice_01 == '5':
                break


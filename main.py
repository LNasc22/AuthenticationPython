# Alunos: Kauane Santana da Rosa e Lucas Nascimento da Silva


import getpass

with open('autentication.txt', "r") as autentication:
    linesAutentication = autentication.readlines()

with open('permissions.txt', "r") as permission:
    linesPermission = permission.readlines()

users = []
permissions = []
files = []

canAccess = False

username = ""

def autenticacao():
    login = input("What is your login?\n")
    password = getpass.getpass("What is your password\n")

    for line in linesAutentication:
        line = line.strip()

        field = line.split(",")

        name = field[0]
        key = field[1]

        users.append((name, key))

    if (login, password) in users:
        global username
        username = login
        print(f"Welcome, {login}!\n")
        global canAccess 
        canAccess = True
    else:
        print("Login or password are incorrect. Try again later!\n")

def mostrarOpcoes():
    global permissions
    global files
    print("Available commands:")
    print("1. List files")
    print("2. Create file")
    print("3. Read file")
    print("4. Delete file")
    print("5. Execute file")
    print("6. Exit\n")

    option = int(input("Select an option\n"))

    if option == 1:

        for line in linesPermission[1:5]:
            line = line.strip()

            field = line.split(",")

            file = field[1]

            files.append((file))
            
        print(f"{files}\n")

    elif option == 3:
        arquivo = input("Type the file name:\n")

        for line in linesPermission[1:]:
            line = line.strip()

            field = line.split(",")

            name = field [0]
            file = field[1]
            read = field[2]

            permissions.append((name, file, read))

        if (username,arquivo,'1') in permissions:
            print("You have permission to read this file!\n")
        else:
            print("No reading permission!\n")

    elif option == 4:
        arquivo = input("Type the file name:\n")

        for line in linesPermission[1:]:
            line = line.strip()

            field = line.split(",")

            name = field [0]
            file = field[1]
            delete = field[3]

            permissions.append((name, file, delete))

        if (username,arquivo,'1') in permissions:
            print("You have permission to delete this file!\n")
        else:
            print("No deleting permission!\n")

    elif option == 5:
        arquivo = input("Type the file name:\n")

        for line in linesPermission[1:]:
            line = line.strip()

            field = line.split(",")

            name = field [0]
            file = field[1]
            execute = field[4]

            permissions.append((name, file, execute))

        if (username,arquivo,'1') in permissions:
            print("You have permission to execute this file!\n")
        else:
            print("No execution permission!\n")

    elif option == 6:
        print("Ok, see ya!")
        global canAccess
        canAccess = False

    permissions = []
    files = []

    while option != 6 and canAccess:
        mostrarOpcoes()

autenticacao()

if canAccess:
    mostrarOpcoes()
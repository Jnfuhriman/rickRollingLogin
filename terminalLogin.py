import webbrowser

def fail():
    site = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    webbrowser.open_new_tab(site)

def addUser(cred):
    while True:
        newUser = input("Enter a unique username: ")
        if newUser in cred:
            print('That username already exists\n')
        else:
            break
    while True:
        newPass = input("Enter a password: ")
        verifyPass = input("Re-enter password to verify: ")
        if newPass == verifyPass:
            break
        else: print('Passwords must match')
    createUser(newUser, newPass)

def createUser(user, password):
    f = open('userPasswords.txt','a')
    userPass = user + ":" + password
    f.write("\n")
    f.write(userPass)
    f.close()
    print("Successfully added user: ", user)
    print("Logging out now")
    main()

def loggedIn(user, cred):
    if user == 'ad':
        print("Welcome admin\n")
        adminChoice = input('Would you like to add a user?')
        if adminChoice == 'yes':
            addUser(cred)
    else: 
        print("Welcome ", user)


def main():
    attempts = 3
    while attempts > 0:
        username = input("Username: ")
        password = input("Password: ")
        f = open('userPasswords.txt', "r")
        credDict = {}
        while True:
            line = f.readline()
            if not line:
                break
            else:
                tempLine = line.split(':')
                credDict[tempLine[0]] = tempLine[1].rstrip()
        if username in credDict and password == credDict[username]:
            loggedIn(username, credDict)
            break
        else:
            attempts = attempts - 1
            if attempts == 0:
                print("No more attempts, exiting program")
                fail()
                break
            else:
                print("invalid credentials, attempts remaining: ", attempts, "\n")
        f.close()
main()
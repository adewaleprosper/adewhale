name = input("What is your name? \n")
allowedUsers = ['Seyi','Mike','Love']
allowedPassword = ['passwordSeyi', 'passwordMike', 'passwordLove']

if(name in allowedUsers):
    password = input("Your password? \n")
    userId = allowedUsers.index(name)

    if(password == allowedPassword[userId]):
        primt('Welcome %s' % name)
        print('These are the available options:')
        print('1. Withdrawal')
        print('2. Cash deposit')
        print('3. Complaint')
        print('4. Register')
        print('5. Login')
        print('6. Generate Account Number')

        selectedOption = int(input('Please select an option:'))

        if(selectedOption == 1):
            print('you selected %s' % selectedOption)
            
        elif(selectedOption == 2):
            print('you selected %s' % selectedOption)
            
        elif(selectedOption == 3):
            print('you selected %s' % selectedOption)

        elif(selectedOption == 4):
            print('you selected %s' % selectedOption)
            details = input("please your email address \n")
            first_name = input("What is your first name? \n")
            last_name = input("what is your last name? \n")
            security = input("password")
            print('Thank you ' + first_name + ' ' + last_name ' for registering')

        elif(selectedoption == 5):
            print('you selected %s' %selectedOption)
            check = input("please put in your email address \n")
            checks = input("password \n")
            print('Welcome')

        elif(selectedOption == 6):
            print("Generating Account Number")
            return random.randrange(111111111,9999999999)    
        else:
            print('Invalid Option selected, please try again')

    else:
        print('Password Incorrect, please try again')
else:

    print('Name not found, please try again')
def register():
    try:
        import sys
        age = int(input("enter your Age:\n"))  # Prompt user for age
        if age < 18:
            print("you are not eligible to register")  # Check if age is less than 18
            sys.exit()  # Exit if not eligible
        else:
            print("you are eligible to register")  # Proceed if age is 18 or above
    except ValueError:
        print("Invalid input. Please enter a valid age.")  # Handle non-integer input
        return

    (input("enter your first name \n"))  # Prompt user for first name
    (input("enter your last name \n"))  # Prompt user for last name
    print("\nSelect your Gender:")
    print("1. Male")
    print("2. Female")
    input("Gender: ")  # Prompt user for gender
    input("enter your mobile number\n ")  # Prompt user for mobile number
    input("\n enter your email\n")  # Prompt user for email
    pas = input("create a password\n")  # Prompt user to create a password
    rpas = input("re-type your password\n")  # Prompt user to re-type the password
    if pas == rpas:
        print("Registration Successful")  # Confirm registration if passwords match
    else:
        print(" Registration Failed \n Check Your Password")  # Error if passwords don't match

def login():
    import sys
    age = int(input("enter your Age: \n"))  # Prompt user for age
    if age < 18:
        print("you are not eligible to login")  # Check if age is less than 18
        sys.exit()  # Exit if not eligible
    else:
        print("you are eligible to login")  # Proceed if age is 18 or above
    username = input("enter your User Name\n")  # Prompt user for username
    pas = 0000  # Default password (not secure, for demo purposes)
    pas1 = int(input("enter your password\n"))  # Prompt user for password
    if (pas1 == pas):
        import random
        while True:
            try:
                opt = int(input("\n select option \n 1.Withdraw \n 2.Deposit \n 3.Pin Change \n "))  # Prompt user for option
                if opt == 1:
                    print("************Withdraw*************")
                    pin = int(input("enter pin\n"))  # Prompt user for pin
                    #PIN
                    Pin = 1234  # Default pin (not secure, for demo purposes)
                    if (pin == Pin):
                        #balance
                        balance = 100000  # Example balance
                        amt = float(input("enter amt\n"))  # Prompt user for withdrawal amount
                        if amt < balance:
                            if amt % 100 == 0 or amt % 50 == 0:  # Check if amount is multiple of 50 or 100
                                bal = balance - amt  # Deduct amount from balance
                                #balance;
                                avlbal = str(bal)  # Convert balance to string
                                print("amount you have withdraw :", amt)
                                print("balance you have available:", avlbal)
                                print("****************Withdraw Successful ******************\n")
                                break
                            else:
                                print("\n*************Amount must be above 100******************\n")
                                print("                        OR                                \n")
                                print("***************Amount must be divisible my 100************")
                        else:
                            print("\ninsufficient balance\n")  # Error if insufficient balance
                    else:
                        print("\ninvalid pin\n")  # Error if pin is incorrect
                elif opt == 2:
                    print("**********************DEPOSIT****************************\n")
                    #pin
                    Pin = 1234  # Default pin (not secure, for demo purposes)
                    pin = int(input("enter pin\n"))  # Prompt user for pin
                    if pin == Pin:
                        amt = float(input("enter amt\n"))  # Prompt user for deposit amount
                        #balance
                        balance = 100000  # Example balance
                        if amt % 100 == 0 or amt % 50 == 0:  # Check if amount is multiple of 50 or 100
                            bal = balance + amt  # Add amount to balance
                            # balance
                            avlbal = str(bal)  # Convert balance to string
                            print("****************Deposit Successful*****************\n")
                            print("Amount you have Deposit :", amt)
                            print("Balance you have available:", avlbal)
                            break
                        else:
                            print("\namt multiply by 100\n")  # Error if amount not multiple of 50 or 100
                    else:
                        print("\ninvalid pin\n")  # Error if pin is incorrect
                elif opt == 3:
                    print("******************Pin Change***************")
                    pin = int(input("enter pin\n"))  # Prompt user for pin
                    #PIN
                    Pin = 1234  # Default pin (not secure, for demo purposes)
                    if (pin == Pin):
                        otp = random.randint(1111, 9999)  # Generate random OTP
                        print("OTP : ", otp)
                        userotp = int(input("enter otp\n"))  # Prompt user for OTP
                        if otp == userotp:
                            newpin = int(input("Enter New Pin\n"))  # Prompt user for new pin
                            Rnewpin = int(input("Re-Enter Pin\n"))  # Prompt user to re-enter new pin
                            if newpin == Rnewpin:
                                print("\nPin Updated\n")  # Confirm pin change if pins match
                                break
                            else:
                                print("\nPin doesn't Match\n")  # Error if pins don't match
                        else:
                            print("\nOTP doesn't Match\n")  # Error if OTP is incorrect
                else:
                    print("\nInvalid Option\n")  # Error if invalid option is selected
            except ValueError:
                print("Invalid input. Please enter a valid option.")  # Handle non-integer input
    else:
        print("Password is incorrect")  # Error if password is incorrect

while True:
    print("WELCOME TO THE STATE BANK OF INDIA")
    print("1:Registration")
    print("2:Login")
    try:
        choice = int(input("Enter your choice: \n"))  # Prompt user for choice
        if choice == 2:
            login()  # Call login function if choice is 2
            break
        if choice == 1:
            register()  # Call register function if choice is 1
            break
        else:
            print("Invalid option. Please select a valid option (1-3).")  # Error if invalid choice is made
    except ValueError:
        print("Invalid input. Please enter a valid option.")  # Handle non-integer input

    input("enter your mobile number\n ")
    input("\n enter your email\n")
    pas = input("create a password\n")
    rpas = input("re-type your password\n")
    if pas == rpas:
        print("Registration  Successful")
    else:
        print(" Registration Failed \n Check Your Password")


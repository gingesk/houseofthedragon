import random
import sys

def main():
    account_details = log_in() #runs log in, which also gets the user's account details. the rest of the options can only be accessed after a PIN is logged in with or registered.
    # key for account details: 
    # account_details[0] - PIN
    # account_details[1] - First Name
    # account_details[2] - Second Name
    # account_details[3] - Account Number
    # account_details[4] - Balance
    # account_details[5] - Overdraft
    print(f"\nWelcome back, {account_details[1]}.")
    print(f"Your current balance is {account_details[4]}.")
    while True: #main menu loop
        selection = input("\nEnter what you would like to do: ")
        selection = selection.upper()
        if selection == "HELP": #displays options through help menu.
            print("Your available options are:")
            print("'DEPOSIT' to your account.")
            print("'WITHDRAW' from your account.")
            print("'APPLY' for an overdraft.")
            print("'EXIT' and log out.")
            print("Please note: Your account will only be updated after you log out.")
        elif selection == "DEPOSIT":
            account_details[4] = deposit_money(int(account_details[4])) #runs deposit, and updates account balance.
        elif selection == "WITHDRAW":
            account_details[4] = withdraw_money(int(account_details[4]),int(account_details[5])) #runs withdraw, and updates account balance.
        elif selection == "APPLY":
            account_details[5] = overdraft_application(int(account_details[5])) #runs overdraft application, and updates it accordingly.
        elif selection == "EXIT":
            break #breaks out of the while loop to exit the program.
        else:
            print("That was not a valid option. Enter 'HELP' for help.")
    log_out(account_details)

def deposit_money(balance):
    deposit = get_int_input("Enter how much you would like to deposit")
    balance=balance+deposit #adds deposited amount to balance.
    print(f"Deposited {deposit} to your balance. New balance: {balance}.")
    return str(balance)

def withdraw_money(balance,overdraft):
    withdrawal = get_int_input("Enter how much you would like to withdraw")
    if balance-withdrawal < overdraft: #prevents the user from withdrawing beyond their overdraft (a negative number).
        print("You cannot withdraw this much, you may need to apply for a larger overdraft.")
    else:
        balance=balance-withdrawal #takes withdrew amount from balance.
        print(f"Withdrew {withdrawal} from your balance. New balance: {balance}.")
    return str(balance)

def overdraft_application(overdraft):
    overdraft = get_int_input(f"Your current overdraft limit is {-overdraft}, what new overdraft limit would you like to apply for?")
    overdraft = -overdraft #converts the positive number the user entered into a negative one, for math purposes.
    print(f"Your overdraft has been updated to a limit of {-overdraft}.")
    return str(overdraft)

def log_in():
    while True: #loops until a valid 4-digit numerical pin is entered.
        try:
            pin = int(input("Please enter your PIN: "))
            if pin > 9999 or pin < 1:
                print("Error: Invalid PIN entry, PINs are 4-digits.")
            else:
                pin = str(pin).zfill(4) #uses zfill to ensure a pin is 4 digit, even if just '1' were entered.
                break #breaks from the loop as the pin is valid.
        except:
            print("Error: Invalid PIN entry, PINs are numerical.")
    try:
        f = open("accounts.txt","r")
    except:
        f = open("accounts.txt","w")
        f.close()
        f = open("accounts.txt","r")
    accounts_list = f.readlines()
    for account in reversed(accounts_list): #performs a linear search to look for the pin, starting from latest entries to get the most recent account details.
        account = account.split("|")
        if pin == account[0]:
            print("Valid PIN, logging in.") #logs in if the pin is found.
            f.close()
            return account
    else:
        f.close()
        print("Did not find an account with this PIN, would you like to register?") #if the pin is not found, allows the user to choose to register an account.
        while True: #loops until Y/N is entered.
            choice = input("[Y/N]: ")
            choice=choice.upper()
            if choice == "Y":
                while True:
                    f_name = input("Enter your first name: ")
                    if f_name.isalpha():
                        break
                    else:
                        print("Please enter only letters.")
                while True:
                    s_name = input("Enter your second name: ")
                    if s_name.isalpha():
                        break
                    else:
                        print("Please enter only letters.")
                while True: #loops the account number generation until no matches are found, to ensure it is unique.
                    account_no = random.randint(0,99999999)
                    account_no = str(account_no).zfill(8) #converts account number to a string, and fills it to 8-digits.
                    for account in accounts_list: #linear search for a matching account number.
                        account = account.split("|")
                        if account_no == account[3]: #if the account number matches another, the for loop is broke and the while loop runs again.
                            break
                    else: #if the for loop finishes without breaking, the while loop is exited as the account number is unique.
                        break
                f = open("accounts.txt","a")
                f.write(pin+"|"+f_name+"|"+s_name+"|"+account_no+"|0|0|\n") #writes the user details to the accounts file, 'registering' them.
                f.close()
                print("You have been registered, logging in.")
                account=[pin,f_name,s_name,account_no,"0","0"]
                return account
            elif choice == "N":
                print("You will not be registered. Exiting the program.")
                sys.exit(0)
            else:
                print("Enter either Y or N.")

def log_out(new_details):
    f = open("accounts.txt","a")
    f.write(new_details[0]+"|"+new_details[1]+"|"+new_details[2]+"|"+new_details[3]+"|"+new_details[4]+"|"+new_details[5]+"|\n")
    f.close()
    print("\nYour account details have been updated accordingly. Now logging out...")

def get_int_input(input_message):
    while True:
        try:
            user_input = int(input(f"\n{input_message}: "))
            if user_input < 0:
                print("Error: Please enter a positive amount.")
            else:
                return user_input
        except:
            print("Error: Please enter a whole number.")

main()

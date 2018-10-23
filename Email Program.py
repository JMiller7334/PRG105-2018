import pickle


def get_file():
    try:
        data_file = open('emails.dat', 'rb')
        data_table = pickle.load(data_file)
        data_file.close()
    except FileNotFoundError:
        print("NOTICE: file emails.dat was not found. new file: emails.dat will be created.")
        data_table = {}
    return data_table


def save_file(data):
    output_file = open('emails.dat', 'wb')
    pickle.dump(data, output_file)
    print("NOTICE: email.dat has been saved.")


def menu():
    user_input = 0
    try:
        while user_input < 1 or user_input > 5:
            print("----------- Menu -----------")
            print("1: add email address entry.")
            print("2. remove email address entry.")
            print("3. look up entry by email.")
            print("4. edit  existing entry")
            print("5. Exit program and save data.")
            user_input = int(input("Please enter a number to perform it's corresponding action. please refer to the"
                                   " list above"". "))
            if user_input < 1 or user_input > 5:
                print("\n")
                print("error: " + str(user_input) + " is not valid. Your selection must be between 1 and 5.")
            else:
                return user_input
    except ValueError:
        print("\n")
        print("error: invalid user entry. Please ensure to enter a number between 1 and 5")
        main()


def add_entry(data):
    user_email = str(input("Please enter the email you would like to add to the database. "))
    search = data.get(user_email.lower())
    if search is not None:
        print(str(user_email) + " already exists within the database.")
        print("returning to main menu.")
        print("\n")
        main()
    else:
        user_name = str(input("Please enter the name of person to whom this email belongs. "))
        data.update({user_email.lower(): user_name.lower()})
        print("Database updated! " + user_email + " has been added as the email and " + user_name +
              " has been added as the email's owner")
        print("Returning to menu")
        print("\n")
        save_file(data)
        main()


def delete_entry(data):
    user_email = str(input("Please enter the email for the entry you would like to delete. "))
    search = data.get(user_email.lower())
    if search is None:
        print(user_email + " is not a valid entry within the database.")
        main()
    else:
        print("Entry deleted! Data for this entry has been deleted.")
        print("\n")
        data.pop(user_email)
        save_file(data)
        main()


def edit_entry(data):
    user_email = str(input("Please enter the email for the entry you would like to search. ")).lower()
    search = data.get(user_email)
    if search is None:
        print(user_email + " is not a valid entry within the database.")
        main()
    else:
        print("Entry found! Data for this entry is listed below.")
        print("Email Address: " + user_email + " | Email Owner: " + search)
        choice = str(input("Would like to change the email for this entry? y/n ")).lower()
        if choice == "y":
            new_email = str(input("Please enter the new email address for this entry. ")).lower()
            data[new_email] = data[user_email]
            data.pop(user_email)
            user_email = new_email
            print("Entry now appears as: Email Address: " + user_email + " | Email Owner: " + search)
            print("\n")
        choice = str(input("Would you like to change the owner's name for this entry? y/n ")).lower()
        if choice == "y":
            new_name = str(input("Please enter new name of the email owner for this entry. ")).lower()
            data[user_email] = new_name
            print("Entry now appears as: Email Address: " + user_email + " | Email Owner: " + new_name)
            print("\n")
        save_file(data)
        main()


def search_entry(data):
    user_email = str(input("Please enter the email for the entry you would like to search. "))
    search = data.get(user_email.lower())
    if search is None:
        print(user_email + " is not a valid entry within the database.")
        main()
    else:
        print("Entry found! Data for this entry is listed below.")
        print("Email Address: " + user_email + " | Email Owner: " + search)
        print("\n")
        main()


def main():
    file = get_file()
    user_entry = menu()
    print("\n")
    if user_entry == 1:
        add_entry(file)
    elif user_entry == 2:
        delete_entry(file)
    elif user_entry == 3:
        search_entry(file)
    elif user_entry == 4:
        edit_entry(file)
    else:
        save_file(file)
        print("data in file is as appear below")
        print(file)  # mainly for debug reasons.


main()

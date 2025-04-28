phonebook={}

while True:
    print("\n=====phonebook Menu ===")
    print("1. Add contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Show All Contacts")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name= input("enter name: ").strip()
        number=input("enter phone number: ").strip()
        phonebook[name]=number
        print(f"{name} added sucessfully")


    elif choice == "2":

        name = input("Enter name to search: ").strip()
        if name in phonebook:
            print(f"{name}'s number is {phonebook[name]}")
        else:
            print(f"{name} not found.")

    elif choice == "3":
        name= input("enter name to delete").strip()

        if name in phonebook:
            del phonebook[name]
            print(f'{name}')
        else:
            print("not found")

    elif choice == "4":
        if phonebook:
            print("--- All Contacts ---")
            for name, number in phonebook.items():
                print(f"{name} -> {number}")
        else:
            print("Phonebook is empty.")

    elif choice == "5":
        print("Exiting Phonebook. Bye bro!")
        break

    else:
        print("Invalid choice! Please select 1-5.")  
        break            


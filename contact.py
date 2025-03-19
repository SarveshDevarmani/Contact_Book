contact = {}

while True:

    print("Hey User, Welcome to Contact Book App!\n")

    print("1. Create Contact: ")
    print("2. View Contact: ")
    print("3. Delete Contact: ")
    print("4. Search Contact: ")
    print("5. Update Contact: ")
    print("6. Count Contact: ")
    print("7. Exit: ")

    ch = input("Enter your choice: ")

    if ch == '1':
       name = input("Enter your name: ")
       if name in contact:
         print(f'Contact name {name} already exits!')
       else:
         age = int(input("Enter your age: "))
         email =input("Enter your email: ")
         mobile = int(input("Enter mobile number: "))

         contact[name] = {'age':int(age),'email':email,'mobile':mobile}
         print("Contact created successfully!")

    elif ch == '2':
       name = input("Enter contact name to view: ")
       if name in contact:
         contact = contact[name]
         print(f'Name{name}Age{age},email{email},mobile{mobile}')
       else:
         print("Contact not found!")

    elif ch == '3':
       name = input("Enter contact name to delete: ")
       if name in contact:
         del contact[name]
         print(f'Contact{name} has successfully deleted!')
       else:
         print('Contact not found!')
      
    elif ch == '4':
       search_name = input("Enter contact name to search: ")
       found = False
       for name,contact in contact.items():
            if search_name.lower() in name.lower():
                print(f'found-name:{name},age{age},email:{email},mobile:{mobile}')
                found = True
       if not found:
             print("No Contact found with that name...")

    elif ch == '5':
        name = input("Enter contact name to update: ")
        if name in contact: 
            up_age = int(input("Enter updated age: "))
            up_email = input("Enter the updated email: ")
            up_mobile = int(input("Enter updated mobile number: "))
            print(f'Name: {name},Age: {age},Email:{email},Mobile:{mobile}')
        else:
         print("Contact not found!")

    elif ch == '6':
         print(f'Total number of contacts: {len(contact)}')

    elif ch == '7':
        print("Good Bye!")
        break








        

      




      



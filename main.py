#contact book project 

contact={}

while True:
    print("\n Welcome to contact book app")
    print()
    print("Press 1 - Create Contact")
    print("Press 2 - View Contact")
    print("Press 3 - Update Contact")
    print("Press 4 - Delete Contact")
    print("Press 5 - Search Contact")
    print("Press 6 - Count Contact")
    print("Press 7 - Terminate Programme")
    print()
    
    choice=input("Enter Your Choice = ")
    
    if choice=='1':
        name=input("Enter name : ")
        if name in contact:
            print("This contact already exist")
        else :
            age = input("Enter age : ")
            email = input("Enter emial : ")
            mobile = input("Enter mobile : ")
            contact[name] = {'age':int(age),'email':email,'mobile':mobile } 
            print(f'The contact with name {name} is added successfully')
    elif choice=='2':
        name=input("Enter name : ")
        if name in contact:
            contacts=contact[name]
            print(f'Name:{name},Age:{age},Mobil:{mobile},Email:{email}')
        else:
            print("contact not found")
    elif choice=='3':
         name=input("Enter name : ")
        
         if name in contact:
             age = input("Enter new age : ")
             email = input("Enter new emial : ")
             mobile = input("Enter new mobile : ")
             contact[name]={'age':{age},'email':{email},'mobile':{mobile}}
             print(f'contact {name} has been updated successfully')
         else :
            print("contact not found")
    elif choice=='4':
        name=input("Enter name : ")
        
        if name in contact:
          del contact[name]
          print(f'{name} deleted successfully from the book')
        else :
            print("contact not found")
    elif choice=='5':
        search=input("enter name : ")
        found=False
        for name, contacts in contact.items():
            if search.lower() in name.lower():
                print(f'found - Name:{name} , Age:{age} , Email:{email},mobile:{mobile}')
                found=True
        if not found:
            print("contact not found")
    elif choice=='6':
        print(f"Total no. of contacts in yout book is count {len(contact)}")
    elif choice=='7':
        print("bye bye")    
    else:
        print("Invalid entity")

                                                                                                                                        














     
 
     

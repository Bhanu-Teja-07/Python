contacts={"bhanu":773208,"vardhan":80960}

#add contact
def add_contact(name:str,mobile:int):
    if name not in contacts:
        contacts[name]=mobile
        return "contact Saved"
    return "contact name already exists"

def update_contact(name:str,mobile:int):
    if name in contacts:
        contacts[name]=mobile
        return "contact updated"
    return " contact not exists"

def delete_contact(name:str):
    if name in contacts:
        contacts.pop(name)
        return "contact deleted"
    return "contact not found"

def get_contact(name:str):
    return contacts.get(name,"contact name note exists")
def all_contacts():
    return contacts

'''def main():
    name=input("enter the name:")
    mobile=int(input("enter the mobile no:"))
    print(add_contact(name,mobile))
    print(contacts)
    print(update_contact(name,mobile))
    print(contacts)
    print(delete_contact(name))
    print(contacts)
    print(get_contact(name))
    '''

if __name__=="__main__":
    print("welcome to contact management")
    while True:
        print("select your operation \n 1.add contact \n 2.update contact \n 3.delete contact \n 4.search mobile number by name \n 5.show contacts \n 6.exit")
        choice=int(input())
        if choice ==1:
            name=input("Enter the contact name : ").strip()
            mobile=int(input("enter mobile number :"))
            res=add_contact(name=name,mobile=mobile)
            print(res)
        elif choice==2:
            name=input("Enter the contact name : ").strip()
            mobile=int(input("enter mobile number :"))
            res=update_contact(name=name,mobile=mobile)
            print(res)
        elif choice==3:
            name=input("Enter the contact name : ").strip()
            res=delete_contact(name=name)
            print(res)
        elif choice==4:
            name=input("Enter the contact name : ").strip()
            res=get_contact(name=name)
            print(res)
        elif choice==5:
            res=all_contacts()
            for name,mobile in res.items():
                print(f"{name}:{mobile}")
        elif choice==6:
            exit()
        else:
            print("invalid choice")

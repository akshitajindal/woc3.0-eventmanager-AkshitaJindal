class contact:
    def __init__(self, name, contactNo):
        self.name = name
        self.contactNos = [contactNo]

def get_name(self):
    return self.name

print("Actions:")
print("1. Make new contact")
print("2. Add to existing contact")
print("3. Search a contact")

contactList = []

while(1):
    action = input("Action: ")
    if int(action)==1:
        name = input("Name: ")
        contactNo = input("Contact Number: ")
        obj = contact(name,int(contactNo))
        contactList.append(obj)
        contactList= sorted(contactList, key=get_name)
    elif int(action)==2: 
        name = input("Name: ")
        flag = 0
        for obj in contactList:
            if obj.name == name:
                contactNo = input("Contact Number: ")
                obj.contactNos.append(int(contactNo))
                flag = 1
                break
        if flag == 0:
            print("Contact name does not exist")
    elif int(action)==3:
        subString = input("Substring: ")
        count = 0
        contactWithSubstring = []
        for obj in contactList:
            if subString in obj.name:
                contactWithSubstring.append(obj)
                print(obj.name)
                count = count + 1
        if count > 0:
            index = input("Choose out of the given contacts(enter the index of the contact): ")
            print(contactWithSubstring[int(index)].name, contactWithSubstring[int(index)].contactNos)
        else:
            print("The given substring was not found in your existing contacts")
    else:
        break

for obj in contactList:
    print(obj.name, obj.contactNos)
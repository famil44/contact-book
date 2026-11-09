import json
import os

FILE_NAME = 'contacts.json'

def load_contacts():
    if not os.path.exists(FILE_NAME):   # checks whether contacts.json exists
        return []
    try:
        with open(FILE_NAME, 'r') as f:
            return json.load(f)   # reads the  file and turns it into a python list of dictionaries
    except json.JSONDecodeError:  # catches a file that is empty or damaged
        return []

def save_contacts(contacts):
    with open(FILE_NAME,'w') as file:   # opens the file for writing,creates file if doesnt exist and overwrites it if it does exist
        json.dump(contacts, file, indent=4)  # writes the list of dictionaries into the file as json,indentation for readability
    
def is_valid_phone(phone):
    phone=phone.replace(' ','').replace('-','')   # removes spaces and -
    return phone.isdigit() and len(phone) == 10

def is_valid_email(email):
    email=email.strip()  # removes extra spaces in starting and ending
    if email.count('@') != 1 or ' ' in email:
        return False
    local,domain = email.split('@')
    return len(local)>0 and '.' in domain and not domain.startswith('.') and not domain.endswith('.')
    
def is_duplicate(contacts, phone, email, ignore=None):
    for contact in contacts:
        if contact is ignore:
            continue
        if contact['phone']==phone or contact['email'].lower()==email.lower():
            return True
    return False
        
def add_contact(contacts):
    name = input("Enter Your Name:").strip()
    while not name:
        name = input("Enter Your Name:").strip()
    phone = input("Enter Your Mobile Number:")
    while not is_valid_phone(phone):
        phone = input("Invalid! Try Again:")
    phone = phone.replace(' ', '').replace('-', '')
    email = input('Enter Your Email:').strip()
    while not is_valid_email(email):
        email = input('Invalid! Try Again:').strip()
    if is_duplicate(contacts, phone, email):
        print('A Contact With This Mobile Number or Email Already Exists !')
        return
    contacts.append({'name':name.lower(), 'phone':phone, 'email':email.lower()})
    save_contacts(contacts)
    print('Contact Added!')
    
def view_contacts(contacts):
    if not contacts:
        print('No Contacts Found')
        return
    for i,contact in enumerate(contacts,start=1):
        print(i,'.','Name:',contact['name'],'\n    Number:',contact['phone'],'\n    Email:',contact['email'])
        
def search(contacts):
    keyword = input('Enter What You Want To Search:').lower()
    results = []
    for contact in contacts:
        if (keyword in contact['name']
            or keyword in contact['phone']
            or keyword in contact['email']):
            results.append(contact)
    if not results:
        print("No results found!")
        return results
    print(f"\nFound {len(results)} contacts:")
    for i, c in enumerate(results,start=1):
        print(f"{i}. {c['name']} | {c['phone']} | {c['email']}")
    return results
    
#Editing contact
def edit_contact(contacts):
    results = search(contacts)
    if not results:
        return
    try:
        choice = int(input('Enter number to edit: '))
        if not 1 <= choice <= len(results):
            raise IndexError
        contact = results[choice-1]
    except (ValueError, IndexError):
        print('Invalid choice!')
        return
    name = input(f"Name [{contact['name']}]: ").strip().lower() or contact['name']
    phone = input(f"Phone [{contact['phone']}]: ").strip().replace(' ', '').replace('-', '') or contact['phone']
    while not is_valid_phone(phone):
        phone = input('Invalid! Try Again: ').strip().replace(' ', '').replace('-', '')
    email = input(f"Email [{contact['email']}]: ").strip().lower() or contact['email']
    while not is_valid_email(email):
        email = input('Invalid! Try Again: ').strip().lower()
    if is_duplicate(contacts, phone, email, ignore=contact):
        print('Another contact already has this phone or email!')
        return
    contact.update(name=name, phone=phone, email=email)
    save_contacts(contacts)
    print('Contact Updated!')
    
def delete_contact(contacts):
    results = search(contacts)
    if not results:
        return
    try:
        choice = int(input('Enter number to delete: '))
        if not 1 <= choice <= len(results):
            raise IndexError
        contact = results[choice-1]
    except (ValueError, IndexError):
        print('Invalid choice!')
        return
    if input(f"Delete {contact['name']}? (y/n): ").lower() == 'y':
        contacts.remove(contact)
        save_contacts(contacts)
        print('Contact Deleted!')
    else:
        print('Cancelled.')
        
def main():
    contacts = load_contacts()
    while True:
        print('\n1. Add  2. View  3. Search  4. Edit  5. Delete  6. Exit')
        choice = input('Choose an option: ').strip()
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search(contacts)
        elif choice == '4':
            edit_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print('Goodbye!')
            break
        else:
            print('Invalid option!')

if __name__ == '__main__':
    main()
#Alexa Nelson
#CSCI 101 - Section G
#Create Project

import csv
csv_info = ['Name', 'Number', 'Email']
contact_lists = open('contact_list_names.txt', 'a')

def newList(): #creates new contact list
    ogList = False
    print('you have chosen "create a new contact list" is that correct?')
    confirmation = input('y/n > ')
    confirmation == confirmation.lower()
    if confirmation == 'y' or 'yes':
        print('what do you want to name the list?')
        while ogList == False: #makes sure the new list name is unique
            contact_list = input('LIST NAME> ')
            contact_lists = open('contact_list_names.txt')
            names = contact_lists.read()
            if contact_list in names:
                print('this contact list already exists, pick another name')
            else:
                ogList = 'True'     
        contact_lists = open('contact_list_names.txt', 'a')#keeps track of all the contact lists
        contact_lists.write(contact_list)
        contact_list = contact_list + '.csv'
        with open(contact_list, 'w', newline='') as csvFile:
            writer = csv.writer(csvFile)#initializes the new list as an empty csv
            writer.writerow(csv_info)
        csvFile.close()

def newContact(list_name):#creates new contact
    print('what is the full name of the new contact?')
    name = input('NAME> ')#add something here for name confirmation
    print("what is the contact's number?")
    number = input('NUMBER> ')#maybe go back to format the number with hyphens and apostrophes
    print("what is the contact's email?")
    email = input('EMAIL> ')
    with open(list_name, 'a', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow([name, number, email])
    csvFile.close()

def deleteContact(list_name):
    print('What contact do you want to delete?')
    nameIn = False
    while nameIn == False:#checks if contact exists
        name = input('NAME> ')
        list_names = open(list_name)
        list_string = list_names.read()
        if name in list_string:
            nameIn = True
        else:
            if name == ('x' or 'X'):
                return
            print('that name is not in the contact list, try again or enter x to exit')
    lines = list()
    with open(list_name, 'r') as readFile:
        reader = csv.reader(readFile)#removes lines with the name in it
        for row in reader:
            lines.append(row)
            for field in row:
                if field == name:
                    lines.remove(row)
    with open(list_name, 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)

def editContact(list_name):
    csv_file = []
    contact_info = []
    lines = list()
    print('What Contact do you wish to edit?')
    valid = False
    nameIn = False
    while nameIn == False:#checks if contact exists
        name = input('NAME> ')
        list_names = open(list_name)
        list_string = list_names.read()
        if name in list_string:
            nameIn = True
        else:
            if name == ('x' or 'X'):
                return
            print('that name is not in the contact list, try again or enter x to exit')
    print('what field do you wish to edit? (email or phone number)')
    while valid == False:
        field = input('FIELD> ')
        if field == ('email' or 'phone number'):
            valid = True
        else:
            if field == ('x' or 'X'):
                return
            print('That is not a valid field, please enter agian or press x to exit')
    if field == 'email':
        print('What is the new email?')
        new_email = input('NEW EMAIL> ')
        with open(list_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                csv_file.append(row)
        for contacts in csv_file:
            if name == contacts[0]:
                contact_info = contacts#creates new edited contact as list
        old_email = contact_info[2]
        contact_info[2] = new_email
        with open(list_name, 'r') as readFile:
            reader = csv.reader(readFile)#removes lines with the name in it
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == name:
                        lines.remove(row)
        with open(list_name, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines + [contact_info])
            
        
    if field == 'phone number':
        print('What is the new number?')#this is the same code for email but for number now
        new_number = input('NEW NUMBER> ')
        with open(list_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                csv_file.append(row)
        for contacts in csv_file:
            if name == contacts[0]:
                contact_info = contacts
        old_number = contact_info[1]
        contact_info[1] = new_number
        with open(list_name, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == name:
                        lines.remove(row)
        with open(list_name, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines + [contact_info])    

def findContact(file_name):
    csv_file = []
    print('What Contact do you wish to look up?')
    nameIn = False
    while nameIn == False:#checks if contact exists
        name = input('NAME> ')
        list_names = open(file_name)
        list_string = list_names.read()
        if name in list_string:
            nameIn = True
        else:
            if name == ('x' or 'X'):
                return
            print('that name is not in the contact list, try again or enter x to exit')
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            csv_file.append(row)
    for contacts in csv_file:
        if len(contacts) > 0:
            if name == contacts[0]:
                contact_info = contacts
    print(contact_info)

program_done = False
print('welcome to the contacts keeper, what would you like to do?')
while program_done == False:
    print("""
    list of commands
    1. Create Contact      2. Create Contact List
    3. Delete Contact      4. Edit a Contact
    5. Find Contact        6. exit      
    """)
    command = input('COMMAND> ')
    if command == '1':
        print("what is the name of the csv file? (include '.csv')")
        file_name = input('FILE NAME> ')
        newContact(file_name)
    if command == '2':
        newList()
    if command == '3':
        print("what is the name of the csv file? (include '.csv')")
        file_name = input('FILE NAME> ')
        deleteContact(file_name)
    if command == '4':
        print("what is the name of the csv file? (include '.csv')")
        file_name = input('FILE NAME> ')
        editContact(file_name)
    if command == '5':
        print("what is the name of the csv file? (include '.csv')")
        file_name = input('FILE NAME> ')
        findContact(file_name)
    if command == '6':
        print('goodbye')
        program_done = True










    

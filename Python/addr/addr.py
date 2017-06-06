#!/usr/bin/python3
# addr.py
# This is a simple application to keep track of contact information from the terminal

''' TODO
  develop add_contact
  develop build_contact
  develop delete_contact
  develop get_book
  develop search_book
  develop update_contact
  develop help function to explain cli syntax
  debug *
  move cli args handling to a seperate function

'''
import os, pprint

def build_contact(line): # Reads in data from a csv and returns dictionaries
  # templete for contact
  # contact = {Name: '', Cell Phone: '', Home Phone: '', Work Phone: '', Email: ''}
  

def delete_contact():
    
def get_help(arg): # prints helpfull information on how to use the program
  print('''This is a simple application to keep track of contact information from the terminal
        
           format:
             addr [arguments/function] [arguments]

           funtions:
             add    - create new contact 
             delete - delete an existing contact
             update - update an existing contact

           arguments:
             name         - first name | last name | first + last
             phone number - xxx-xxxx | xxx-xxx-xxxx
             email        - account@domain.com
             { }          - new contact information 
             *            - selects all contacts

           contact keys:
               name  - first and last name
               cellp - cell phone number
               homep - home phone number
               workp - work phone number
               email - email address
               address - physical address

           examples:
             addr update 'John Doe' - updates an existing contact named 'John Doe'
             addr add {name: 'John Doe', cellp: '555-555-5555', email: 'user@domain.com'}
        ''')

'''def menu(contacts[]): # print the list of available actions and handle cli
  exit = False
  contacts = 
  while exit != True:
    print('1. Print all \n2. Search \n3. New \n4. Update \n5.Delete \n6. Quit \n\
           ----------------------------------------------------------\n\
            What would you like to do (enter action number): ')
    response = input()
    if response == '1': print_book(); continue
    elif response == '2': search_book(); continue
    elif response == '3': add_contact(); continue
    elif response == '4': update_contact(); continue
    elif response == '5': delete_contact(); continue
    elif response == '6': exit = True; continue
    else: print('That is not a valid response. Note the numbers next to the actions.\n\n')

  exit, response = None
  del exit, response
'''

def open_book(book_path): # opens/creates the contact book and loads it into the contacts list
  contacts = []
  try:
    if not os.path.isfile(book_path):
      print('File does not exist. Do you want to create a new contacts file?')
      response = input().lower().strip()
      if response == 'y':
        file(book_path, 'w').close()
        print(os.path.basename(book_path) + ' did not exist in ' + os.path.dirname(book_path) + \
            ', so a new contacts file was made for you.')
        book = open(book_path, 'r')
      elif response == 'n':
          print('A file was not provided, exiting.')
          sys.exit()
      else:
          print('An response was not provided, exiting.')
          sys.exit()
    for line in book:
        contacts.append(build_contact(book.readline()))
  except OSError, err1:
      print('Error 1: There was an issue opening the file. The program will now close.')
      sys.exit()
  finally:
      book = None
      del book
      book.close()
      print('The contact book has been loaded into memory.')
      print('You have: ' + contacts.len() + ' contacts.')
      return contacts

def print_book():

def search_book(contacts_list): 
  '''.isalpha(query.strip()) = Name search
     .isdecimal(query.strip(-()) = Phone search
     .isalnum(query.lower().strip()) = Email search
  '''

def update_contact():

def main():
  '''len = 0 -> bring up menu
     len = 1 -> identify (path, function, or error)
     len = 2 -> identify function and pass the second item as param
     len = 2... -> parameters to pass to the next function
  '''
  default_path = os.path.join('$HOME', '.addr_book')

  if len(sys.argv) < 2: 
    get_help()
    sys.exit()
  elif args.len() == 1:
    if os.path.isabs(args[0]) or os.path.isrel(args[0]):
      menu(open_book(args[0]))
    else:
      get_help(args[0])
  elif args.len() == 2:
      




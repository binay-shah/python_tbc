# -phones.py *- coding: utf-8 -*-
"""
This program maintains a database of names and phone numbers in a csv
file called myphones.csv.  It is run from the command line and is menu
driven.  To start it, save it in a directory and from the terminal run
>python phones.py

Version FINAL:
"""
import sqlite3



phones = []
name_pos = 0
phone_pos = 1
phone_header = ('id', 'Name', 'Phone Number')

def proper_menu_choice(which):
    if not which.isdigit():
        print ("'" + which + "' needs to be the number of a phone!")
        return False
    which = int(which)
    if which < 1:
        print ("'" + str(which) + "' needs to be the number of a phone!")
        return False
    return True
    
def delete_phone(cursor):
    which = input("Which item do you want to delete? ")
    print("which is ", which)
    if not proper_menu_choice(which):
        return
    which = int(which)

    query = "delete from myphones where id = ?"
    cursor.execute(query, (which,))
    print( "Deleted phone #", which)

def edit_phone(cursor):
    which = input("Which item do you want to edit? ")
    print("which is ", which)
    if not proper_menu_choice(which):
        return
    which = int(which)

    query = "select name, num from myphones where id = ?"
    cursor.execute(query, (which, ))
    result = cursor.fetchone()
        
    phone = result[phone_pos]
    print("Enter the data for a new phone. Press <enter> to leave unchanged.")
    
    print(result[name_pos])
    newname = input("Enter phone name to change or press return: ")
    if newname == "":        
        newname = result[name_pos]
        
    print(result[phone_pos])    
    newphone_num = input("Enter new phone number to change or press return: ")
    if newphone_num == "":
        newphone_num = phone[phone_pos]
            
    
    query = "update myphones set name = ?, num = ? where id = ?"
    cursor.execute(query, (newname, newphone_num, which))
    cursor.execute("commit")
    

  
def save_phone_list(cursor):
    cursor.execute("commit")
    
  
def load_phone_list():
    conn = sqlite3.connect("pnones.db")
    cursor = conn.cursor()
    return cursor

def show_phones(cursor):
    show_phone(phone_header[0], phone_header[1], phone_header[2])
    query = "select * from myphones"
    cursor.execute(query)
    results = cursor.fetchall()
    
    for row in results:
        show_phone(row[0], row[1], row[2])
        
    print()

def show_phone(id, name, phone_num):
    outputstr = "{0:>3}  {1:<20}  {2:>16}"
    print(outputstr.format(id, name, phone_num))

def create_phone(cursor):
    print("Enter the data for a new phone:")
    newname = input("Enter name: ")
    newphone_num = input("Enter phone number: ")
    phone = (newname,newphone_num)
    query = "insert into myphones(name, num) values(?, ?)"
    cursor.execute(query, phone)
    cursor.execute("commit")
    
    
def menu_choice():
    """ Find out what the user wants to do next. """
    print("Choose one of the following options?")
    print("   s) Show")
    print("   n) New")
    print("   d) Delete")
    print("   e) Edit")
    print("   q) Quit")
    choice = input("Choice: ")    
    if choice.lower() in ['n','d', 's','e', 'q']:
        return choice.lower()
    else:
        print(choice +"?")
        print("Invalid option")
        return None


def main_loop():
    
    cursor = load_phone_list()
    
    while True:
        choice = menu_choice()
        if choice == None:
            continue
        if choice == 'q':
            print( "Exiting...")
            break     # jump out of while loop
        elif choice == 'n':
            create_phone(cursor)
        elif choice == 'd':            
            delete_phone(cursor)
        elif choice == 's':
            show_phones(cursor)
        elif choice == 'e':
            
            edit_phone(cursor)
        else:
            print("Invalid choice.")
            
    save_phone_list()
    

# The following makes this program start running at main_loop() 
# when executed as a stand-alone program.    
if __name__ == '__main__':
    main_loop()
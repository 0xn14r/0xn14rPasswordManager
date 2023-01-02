#IMPORTED PACKAGES
import sys
import random
import sqlite3
import rsa
import string


#POOLS 
numbersPool = [0,1,2,3,4,5,6,7,8,9]
specialCharactersPool = ['~','!','@','#','$','%','^','&','(',')','-','_','+','=','{','}',':',";",'"','?','/','>','<','.',","]
lettersPool = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def Printable2():
    goodbye='''
#############################################################
#          Thank you for using my password manager          #
#############################################################

Contact Information
    
    ) Whatsapp  + 961 3 490 468

    ) Linkedin  https://www.linkedin.com/in/nizarridaa

    ) Email     NizarRida98@outlook.com

#############################################################
#                         by 0xn14r                         # 
#############################################################
'''
    print(goodbye)

def Printable1():
    welcome='''
#############################################################
#             Python Password Manager by 0xn14r             #
#############################################################
#                         CONTACT                           #
#############################################################
#   DEVELOPER: 0xn14r  Nizar Rida                           #
#   Email Address:  NizarRida98@outlook.com                 #
#   Linkedin  https://www.linkedin.com/in/nizarridaa        #
#   Whatsapp  + 961 03 490 468                              #
#############################################################
'''
    print(welcome)

def Exit():
    Printable2()
    input("\nPress any key to continue . . .")
    sys.exit()

def GeneratePasswd():

  #ASSIGNING GLOBAL VARIABLES 

    global chosen_Numbers
    global chosen_Scharacters
    global chosen_letters
    global random_index_Upper
    global final_draft
    global n
     
#GENERATING RANDOM NUMBERS

    while True:
      chosen_Numbers=random.choices(numbersPool,k=numbers)
      print("\nYour randomly chosen numbers are: ",chosen_Numbers)
      m=input("Enter 'y' to continue 'n' to regenerate.\n")
      if(m=='y'):
        final_draft=chosen_Numbers
        break
      if(m=='n'):
        continue
      else:
        print("\nYou can only enter (y or n)")

#GENERATING RANDOM LETTERS 
    
    while True:
      n=passLength-numbers-specialC
      chosen_letters=random.choices(lettersPool,k=n)
      print("\nYour randomly chosen letters are: ",chosen_letters)
      m=input("Enter 'y' to continue 'n' to regenerate.\n")
      if(m=='y'):
        final_draft.extend(chosen_letters)
        break
      if(m=='n'):
        continue
      else:
        print("\nYou can only enter (y or n)")
       
#GENERATING RANDOM SPECIAL CHARACTERS
       
    while True:
      chosen_Scharacters=random.choices(specialCharactersPool,k=specialC)
      print("\nYour randomly chosen special characters are:\n",chosen_Scharacters)
      m=input("Enter 'y' to continue 'n' to regenerate.\n")
      if(m=='y'):
        final_draft.extend(chosen_Scharacters)
        break
      if(m=='n'):
        continue
      else:
        print("\nYou can only enter (y or n)")

#GENRATING RANDOM INDEXES FOR CAPITALIZED LETTERS

    while True:
      random_index_Upper=random.sample(range(0,passLength),upperC)
      print("\nYour capitalized letters will be at positions: ",random_index_Upper," out of: [",passLength,"]\nNote: if it was not a letter it will be redirected to the closest letter to it.")
      m=input("Enter 'y' to continue 'n' to regenerate.\n")
      if(m=='y'):
        break
      if(m=='n'):
        continue
      else:
        print("\nYou can only enter (y or n)")
   
   
#ASSIGN THE FINAL DRAFT PASSWORD TO A STRING AND DISPLAY

    password = ''.join(map(str, final_draft))
    print("\nYour final draft is: ",password)
   
#SHUFFLING THE PASSWORD

    while True:
      password="".join(random.sample(password,len(password)))
      print("Your shuffled password is: ",password)
      m=input("\nWould you like to shuffle again?\n")
      if(m=='n'):
        subMenu(password)
      if(m=='y'):
        continue
      else:
        print("\nYou can only enter (y or n)")

def subMenu(password):
  #SUB MENU FOR PASSWORD FINALIZING
  print("""
  What would you like to do with your generated password?
  
  1) Save in program and Encrypt (RSA Encryption)
     Your private key will not be stored in the database make sure to save it elsewhere.

  2) Encrypt password and Display it (RSA Encryption)
     For one time use only! Nothing will be saved in the Database.

  3) Go back to menu.
  """)
  while True:
    c=input()
    if(c=='1'):
      publicKey, privateKey = rsa.newkeys(512)
      encPass= rsa.encrypt(password.encode(),publicKey)
      a = str(encPass)
      RandId=''.join(random.choices(string.ascii_uppercase + string.digits, k=32))
      while True:
        conn = sqlite3.connect('Userlocal.db')
        cur=conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS User (id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT, last_name TEXT, pass_word TEXT, public_key TEXT)')
        x=input("Enter your first name:\n")
        y=input("Enter your last name:\n")
        cur.execute("INSERT INTO User (first_name, last_name, pass_word, public_key) VALUES (?,?,?,?)", (x,y,str(a),str(publicKey)))
        conn.commit()
        with open(f'PrivateKeyOf:{RandId}.txt', 'w') as f:
          f.write(f'Your private key is: {privateKey}'"\n")
        print("\nRecord saved. \nYour private key is: ",privateKey,"\n")
        conn.close()
        return Menu()
    if(c=='2'):
      RandId=''.join(random.choices(string.ascii_uppercase + string.digits, k=32))
      publicKey, privateKey = rsa.newkeys(512)
      encPass = rsa.encrypt(password.encode(),publicKey)
      print("This session ID is: ",RandId)
      print("\n")
      print("Your password is: ",password)
      print("Your encrypted password is: ",encPass)
      print("Your public key is: ",publicKey)
      print("Your private key is: ",privateKey)
      with open(f'{RandId}.txt', 'w') as f: 
        f.write(f'Your password is: {password}'"\n")
        f.write(f'Your encrypted password is: {encPass}'"\n")
        f.write(f'Your public key is: {publicKey} '"\n")
        f.write(f'Your private key is: {privateKey}'"\n")
        f.write(f'Thank you for using my software')
      print("File saved with your session ID")
      input("Press any key to continue . . .")
      return Menu()      
    if(c=='3'):
      Menu()
      break
    else:
      print("Invalid entry choose another option")

#CONNECTION TO DATABASE INITIALIZATION IF NEEDED

def InitializeConn():
  conn = sqlite3.connect('Userlocal.db')
  cur=conn.cursor()

#DUMP DATABASE 

def PrintTable():
  cur.execute("SELECT * FROM User")
  result= cur.fetchall()
  for row in result:
    print("\nRecord ID:",row[0],"\nFirst Name:",row[1],"\nLast Name:",row[2],"\nPassword:",row[3],"\nPK:",row[4])

#NESTED MENU PART 1 OF 2
 
def ModifyRecordMenu1():
  print("""
1)Change first name on record
2)Change last name on record
3)Change password on record
4)Back
""")

#NESTED MENU PART 2 OF 2

def ModifyRecordMenu2():
  print("""
Search using:
1) ID
2) First name
3) Last name
4) Back
""")

#CHANGING FIRST NAME IN DB FUNCTION

def ChangeFirstName():
  modby_=input("What is the ID of the record you would like to modify?: \n")
  newname=input("Enter the new first name for your record:\n")
  queryOP="UPDATE User set first_name = ? where id = ?"
  cur.execute(queryOP,(newname,modby_))
  conn.commit()

#CHANGING LAST NAME IN DB FUNCTION
     
def ChangeLastName():
  modby_=input("What is the ID of the record you would like to modify?: \n")
  newname=input("Enter the new last name for your record:\n")
  queryOP="UPDATE User set last_name = ? where id = ?"
  cur.execute(queryOP,(newname,modby_))
  conn.commit()

#CHANGING PASSWORD IN DB FUNCTION

def ChangePassword():
  modby_=input("What is the ID of the record you would like to modify?: \n")
  newname=input("Enter the new password for your record:\n")
  queryOP="UPDATE User set pass_word = ? where id = ?"
  cur.execute(queryOP,(newname,modby_))
  conn.commit()

#SEARCHING IN DB BY ID 

def QueryByID():
  cur=conn.cursor()
  global searchByID
  searchByID=input("Enter ID to search\n")
  cur.execute("SELECT * FROM User WHERE id = ? ",(searchByID,))
  search_result = cur.fetchall()
  for all in search_result:
    print(all)

#SEARCHING IN DB BY FIRST NAME

def QueryByFname():
  cur=conn.cursor()
  global searchByFName
  searchByFName=input("Enter first name to search\n")
  cur.execute("SELECT * FROM User WHERE first_name = ? ",(searchByFName,))
  search_result = cur.fetchall()
  for all in search_result:
    print(all)

#SEARCHING IN DB BY LAST NAME

def QueryByLname():
  cur=conn.cursor()
  global searchByLName
  searchByLName=input("Enter last name to search\n")
  cur.execute("SELECT * FROM User WHERE last_name = ? ",(searchByLName,))
  search_result= cur.fetchall()
  for all in search_result:
    print(all)

#MAIN MENU FUNCTION

def Menu():

    #ASSIGNING GLOBAL VARIABLES
    global passLength
    global numbers
    global upperC
    global specialC
    

    #MENU OPTIONS
    print("[1] Generate a password.")
    print("[2] Save a password.")
    print("[3] Manage all passwords.")
    print("[4] Show all data.")
    print("[5] Exit.")

    #MENU AND USER SELECTION AND BRIEFING
    userSelection=input("Please enter your choice\n")

    
    if userSelection=='1':
      print("""\n\nWelcome to the password generator, the rules are simple, we will generate a strong password for you that should be:

1)At Least 8 Characters long. (although we do not advise that).
2)A Maximum of 32 Characters.
3)Your password will contain at least 2 special characters.
4)Your password will contain at least 2 numbers
5)Your password will contain at least 2 upper case characters.
6)The rest of your password will be lower case characters. 

Do you agree to the conditions? (y/n)
""")
 #USER ACCEPTANCE CONDITIONS + OPTION TO QUIT

      while True:
         a=input()
         if(a == 'y' or a =='Y'):
           break
         elif(a == 'n' or a =='N'):
           return Menu()
         else:
          print(a,"is not recongnized as an option, please choose 'y' for yes or 'n' for no.")
    

#PASSWORD LENGTH CONDITIONING

      while True:
        passLength = int (input("\n\nHow many characters long would you like your password to be? (Min 8 - Max 32).\n"))
        if(passLength<  8 or passLength> 32):
          print("There was an error with your entry.")
        else:
          break


#NUMBER OF NUMBERS CONDITIONING
      while True:
        numbers = int (input("\n\nHow many numbers would you like to include? (Minimum is 2).\n"))
        if(numbers  > int(passLength/4)):
          print("The recommended number of numbers for your password is" , int(passLength/4) , "or lower. (Min = 2)\n")
        else:
          break


#NUMBER OF UPPER CASE CHARACTERS CONDITIONING
      while True:
        upperC = int (input("\n\nHow many upper case characters would you like to include? (Minimum is 2).\n"))
        if(upperC > int(passLength/4)):
          print("The recommended number of numbers for your password is" , int(passLength/4) ," or lower. (Min = 2)\n")
        else:
          break


#NUMBER OF SPECIAL CHARACTERS CONDITIONING
      while True:
        specialC = int(input("\n\nHow many special characters would you like to include (Minimum is 2)?\n"))
        if(specialC > int(passLength/4)):
         print("The recommended number of special characters for your password is " , int(passLength/4), "  or lower. (Min = 2)\n")
        else:
          break
      GeneratePasswd()
      return Menu()

#ENTER FIRST NAME, LAST NAME, AND PASSWORD MANUALLY TO DB

    elif userSelection=='2':
      conn = sqlite3.connect('Userlocal.db')
      cur=conn.cursor()
      cur.execute('CREATE TABLE IF NOT EXISTS User (id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT, last_name TEXT, pass_word TEXT, public_key TEXT)')
      x=input("Enter your first name:\n")
      y=input("Enter your last name:\n")
      password=input("Enter your password:\n")
      cur.execute("INSERT INTO User (first_name, last_name, pass_word) VALUES (?,?,?)", (x,y,password))
      conn.commit()
      conn.close()
      return Menu()
    
#MODIFYING DATABASE MENUS (2/2)
#PART 1 AND 2 IMPLEMENTATION
    
    elif userSelection=='3':
      while True:
        ModifyRecordMenu1()
        m=input()
        if(m=='1'):
          ModifyRecordMenu2()
          k=input()
          if(k=='1'):
            QueryByID()
            ChangeFirstName()
          if(k=='2'):
            QueryByFname()
            ChangeFirstName()
          if(k=='3'):
            QueryByLname()
            ChangeFirstName()
          if(k=='4'):
            break
          else:
            print("Invalid Option.")

        if(m=='2'):
          ModifyRecordMenu2()
          k=input()
          if(k=='1'):
            QueryByID()
            ChangeLastName()
          if(k=='2'):
            QueryByFname()
            ChangeLastName()
          if(k=='3'):
            QueryByLname()
            ChangeLastName()
          if(k=='4'):
            break
          else:
            print("Invalid Option.")
        
        if(m=='3'):
          ModifyRecordMenu2()
          k=input()
          if(k=='1'):
            QueryByID()
            ChangePassword()
          if(k=='2'):
            QueryByFname()
            ChangePassword()
          if(k=='3'):
            QueryByLname()
            ChangePassword()
          if(k=='4'):
            break
          else:
            print("Invalid Option.")

        if(m=='4'):
          Menu()
        
        else:
          print("Invalid option.\n")

#DUMP DATABASE IMPLEMENTATION

    elif userSelection=='4':
      PrintTable()
      print("\n\n")
      return Menu()

#EXIT PROGRAM OPTION

    elif userSelection=='5':
      Exit()

    else:
      print("Invalid option.")
      return Menu()

#PROGRAM STARTS HERE 

conn = sqlite3.connect('Userlocal.db')
cur=conn.cursor()  
Printable1()
Menu()


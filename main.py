import sys
import random
import os
global passLength
passLength=0
global passLengthF
passLength=0
def Printable2():
    goodbye="""
#############################################################
#          Thank you for using my password manager          #
#############################################################

Contact Information:
    
    *) Whatsapp : + 961 3 490 468

    *) Linkedin : https://www.linkedin.com/in/nizarridaa

    *) Email    : NizarRida98@outlook.com

#############################################################
#                         by 0xn14r                         # 
#############################################################
"""
    print(goodbye)

def Printable1():
    welcome="""
#############################################################
#             Python Password Manager by 0xn14r             #
#############################################################
#                         CONTACT                           #
#############################################################
#   DEVELOPER: 0xn14r | Nizar Rida                          #
#   Email Address : NizarRida98@outlook.com                 #
#   Linkedin : https://www.linkedin.com/in/nizarridaa       #
#   Whatsapp : + 961 03 490 468                             #
#############################################################
"""
    print(welcome)

def Exit():
    Printable2()
    input("\n\nPress any key to continue . . .")
    sys.exit()

def GeneratePasswd():

    print("\n\nWelcome to the password generator, the rules are simple, we will generate a strong password for you that should be:\n\n1)At Least 8 Characters long (although we do not advise that)\n2)Maximum 32 Characters\n3)Your password will contain at least 1 special character & 1 number\n4)Your password will contain at least 2 upper case characters.\n\nDo you agree to the conditions? (y/n):")
    while True:
     a=input()
     if(a == "y"):
        break
     elif(a == "n"):
        return(Menu())
     else:
        print( a ,"is not recongnized as an option, please choose 'y' for yes or 'n' for no.")
 
    passLength(input("\n\nHow many characters long would you like your password to be? (Min: 8 - Max: 32)\n"))
    passLengthF=int(passLength)
    while True:
        if(passLengthF<8 or passLengthF>32):
            print("Invalid entry. Please try again.")
        else:
            break



    numbers=int=input(print("\n\nHow many numbers would you like to include? (Default is 1)"))
    int=upperC=input(print("\n\nHow many upper case characters would you like to have?\n\nDefault is 2 for 8-15 characters long passwords & 4 for 16+ characters long passwords.\n\nAlternatively enter 'default' for default options, or any number above 2 for bigger passwords."))
    int=specialC=input(print("\n\nHow many special characters would you like to have?\n\nDefault is 1 for 8-15 characters long passwords & 2 for 16+ characters long passwords.\n\nAlternatively enter 'default' for default options, or any number above 4 for bigger passwords."))
    

def Menu():
    print("[1] Generate a password.")
    print("[2] Save a password.")
    print("[3] Export passwords.")
    print("[4] Enable auto-fill.")
    print("[5] Exit.")

    userSelection=input("Please enter your choice\n")
    userSelectionF = int(userSelection)

    while userSelectionF!=0 :
        if userSelectionF==1:
            GeneratePasswd()

        elif userSelectionF==2:
            #do2
            pass

        elif userSelectionF==3:
            #do3
            pass

        elif userSelectionF==4:
            #do4
            pass

        elif userSelectionF==5:
            Exit()

        else:
            print("Invalid option.")

Printable1()
Menu()
def SavePasswd():
    pass

def ManagePasswd():
    pass

def ExportPasswd():
    pass

def EnableAutoFill():
    pass

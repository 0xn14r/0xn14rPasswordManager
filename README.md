# 0xn14rPasswordManager
Inspired by the recent data breach of well-known password manager platforms such as LastPass, I decided to create my own offline version of this service.

Straightforward, user-friendly, and simple to use.

The tool is written solely in Python and SQLite3.
it's still in beta and will be subject to regular updates as it nears completion. 

Encryption is handled using the RSA Python package.

Requirements: Python IDE updated to the latest version.

For windows hosts:

Create a virtual environment to install required python packages:

    python3 -m venv /path/to/new/virtual/environment

Check python documentation for further information:

    https://docs.python.org/3/library/venv.html
    
Features:

I) Generate a password.

Password generation of (8 up to 32) characters based on random letters, numbers, and special characters. Once the user chooses the length of their password they will be prompted to choose how many numbers, special characters, and upper case letters to include in their password.

The rules are simple: The minimum number of numbers to include is ( PasswordLength / 4 ) : Meaning for 8 characters long the Minimum and Maximum number of numbers to include is 2.

The same rule is applied to special characters and upper case letters whereas if you had a 16 characters long password for example:

The Minimum number of numbers you can include is 2, and the Maximum number is ( PasswordLength / 4 ) which is 4 in this use case.

Upon generating the user will prompted to accept lists of numbers, letters, and special characters and upper case letters indexes.

Not accepting will result in re-generation of those lists until the user accepts.

The final draft of the password will be generated, shuffled, and displayed on screen with the option to shuffle as much as the user intends to.

When the user accepts the final shuffled draft, the password will be encrypted with RSA(512) keys and prompted to enter their first and last name.

User has the option to either save in program, export to a txt file or just void.

If user chooses to save in program:

First name, last name, encrypted password, and public key will be saved to the Database. while the private key will be saved to a .txt file named with a random session ID Identifier. 

If user chooses to save to .txt file:

First name, last name, encrypted password, public key, and private key will be saved to a .txt file named after a random session ID Identifier.

Program saves and goes back to the Main Menu.

II) Save a password.

Having already come up with your perfectly memorable secure password, you can save the password in the database by choosing option number 2.

User will be prompted to enter their first name, last name, and password.

The tool will automatically encrypt the password with RSA(512) keys and save the data in the database just like in option number 1.

III) Manage Database.

Query through the Database by either the Unique ID, first name, or last name.

User can Update the first name, last name, or password of a specific record.

IV) Dump Database.

As simple as the title says. Prints the whole database on screen.

V) Delete a record.

Query through the Database to delete a certain record.

VI) Exit

.. just exit, really.



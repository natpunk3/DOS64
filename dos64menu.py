#!/usr/bin/python3
import os
from getpass import getpass
password = "qwerty_32"
login = getpass("Sys32's Password: ")
os.system("clear")
grid = """
\n\n\n
      __             _______ ___ ___
  .--|  .-----.-----|   _   |   Y   |
  |  _  |  _  |__ --|   1___|   |   |
  |_____|_____|_____|.     \|____   |
                    |:  1   |   |:  |
                    |::.. . |   |::.|
                    `-------'   `---'\n\n\n\n
======DOS64=====
    __             _______ ___ ___
.--|  .-----.-----|   _   |   Y   |
|  _  |  _  |__ --|   1___|   |   |
|_____|_____|_____|.     \|____   |
                  |:  1   |   |:  |
                  |::.. . |   |::.|
                  `-------'   `---'
-->
(1). New User
(2). Delete User
(3). FS Tree
(4). Exit"""
print(grid)
option = float(input("Select Option 1-4.\n >> "))
if option == 1:
    print("Not Programed Yet. :(")
    exit(0)
elif option == 2:
    print("No Dont Ever Do That!")
    exit(1)
elif option == 3:
    os.system("dos64")
elif option == 4:
    print("Shutting down DOS64...")
# os.system("pipes2")
    exit(1)


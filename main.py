import os, sys
from PIL import Image
import functions as Fn

def menu():
    os.system('cls')
    print '''
    =====================
    Image Editor
    =====================
    1 - Cut Image
    2 - Change Format
    3 - Make thumbnail
    4 - Close
    =====================
    '''
    choice = raw_input('Choose and press Enter: ')
    return choice

# Choose function
choice = ""
while choice != "4":
    choice = menu()
    if choice == "1":
        os.system('cls')
        Fn.cut_image()
    elif choice == "2":
        os.system('cls')
        Fn.change_format()
    elif choice == "3":
        os.system('cls')
        Fn.make_thumbnail()
    elif choice == "4":
        raw_input('Press anything to close..')
        sys.exit()
        os.system('cls')


menu()


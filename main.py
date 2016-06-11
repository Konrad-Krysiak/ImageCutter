import os, sys
from PIL import Image
from functions import ImageResizer

class Main:
    def menu(self):
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
    
    def choose_function(self):
        image_resizer = ImageResizer()
        choice = ""
        while choice != "4":
            choice = self.menu()
            if choice == "1":
                os.system('cls')
                print '''
        =====================
        CUT IMAGE
        =====================
        1. File
        2. Folder
        3. Close
        =====================
                '''
                method_choice = raw_input(">> ")
                
                if method_choice == "1":
                    directory = raw_input('Directory to file: ')
                    width = input('Width: ')
                    height = input('Height: ')
                    name = raw_input('Save as: ')
                    image_resizer.cut_image(directory, width, height, name)

                elif method_choice == "2":
                    f_directory = raw_input('Directory to folder: ')
                    width = input('Width: ')
                    height = input('Height: ')
                    image_resizer.cut_image_folder(f_directory, width, height)
                    
                elif method_choice == "3":
                    os.system('clear')
                    sys.exit()
                
            elif choice == "2":
                os.system('cls')
                print '''
        =====================
        CHANGE FORMAT
        =====================
        1. File
        2. Folder
        3. Close
        =====================
                '''
                method_choice = raw_input(">> ")
                
                if method_choice == "1":
                    directory = raw_input('Directory to file: ')
                    ext = raw_input('Save as: ')
                    image_resizer.change_format(directory, ext)

                elif method_choice == "2":
                    f_directory = raw_input('Directory to folder: ')
                    ext = raw_input('Format: ')
                    image_resizer.change_format_folder(f_directory, ext)
                    
                elif method_choice == "3":
                    os.system('clear')
                    sys.exit()

            elif choice == "3":
                os.system('cls')
                print '''
        =====================
        MAKE THUMBNAIL
        =====================
        1. File
        2. Folder
        3. Close
        =====================
                '''
                method_choice = raw_input(">> ")
                
                if method_choice == "1":
                    directory = raw_input('Directory to file: ')
                    name = raw_input('Save as: ')
                    image_resizer.make_thumbnail(directory, name)

                elif method_choice == "2":
                    f_directory = raw_input('Directory to folder: ')
                    image_resizer.make_thumbnail_folder(f_directory)
                    
                elif method_choice == "3":
                    os.system('clear')
                    sys.exit()
                    
            elif choice == "4":
                raw_input('Press anything to close..')
                sys.exit()
                os.system('cls')
m = Main()
m.choose_function()
    


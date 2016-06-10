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
        # Choose function
        choice = ""
        while choice != "4":
            choice = self.menu()
            if choice == "1":
                os.system('cls')
                image_resizer.choose_cut_image()
            elif choice == "2":
                os.system('cls')
                image_resizer.choose_change_format()
            elif choice == "3":
                os.system('cls')
                image_resizer.choose_make_thumbnail()
            elif choice == "4":
                raw_input('Press anything to close..')
                sys.exit()
                os.system('cls')
m = Main()
m.choose_function()
    


#Functions to Image Editor
from PIL import Image
import os, sys


def cut_image():
    print '''
    =====================
    CUT IMAGE
    =====================
    1. File
    2. Folder
    3. Close
    =====================
    '''
    choice = raw_input(">> ")
    if choice == "1":
        directory = raw_input('Directory to file: ')
        width = input('Width: ')
        height = input('Height: ')
        name = raw_input('Save as: ')
        im = Image.open(directory)
        im = im.resize((width, height))
        if not os.path.exists('resized_images'):
            os.mkdir('resized_images')
        try:
            print "Size: " + str(width) + " x " + str(height)
            im.save('resized_images/'+name)
            print "- " + name + " : " + "DONE"
            raw_input("Saved in resized_images.")
        except:
            raw_input('Error..')

    elif choice == "2":
        f_directory = raw_input('Directory to folder: ')
        width = input('Width: ')
        height = input('Height: ')
        try:
            fieldlist = os.listdir(f_directory)
        except OSError:
            raw_input('Folder does not exist.')
            sys.exit()
        extensions = ['JPG', 'PNG', 'JPEG', 'GIF']
        if not os.path.exists('resized_images'):
            os.mkdir('resized_images')
        print "Size: " + str(width) + " x " + str(height)
        for item in fieldlist:
            directory = f_directory+ "\\" + item
            im = Image.open(directory)
            if im.format in extensions:
                im = im.resize((width, height))
                im.save('resized_images/'+item)
                print "- " + item + " : " + "DONE"
        raw_input("Saved in resized_images.")
    elif choice == "3":
        os.system('clear')
        sys.exit()
        
def change_format():
    print '''
    =====================
    Change Format
    =====================
    1. File
    2. Folder
    3. Close
    =====================
    '''
    choice = raw_input(">> ")
    if choice == "1":
        directory = raw_input('Directory to file: ')
        ext = raw_input('Save as: ')
        im = Image.open(directory)
        if not os.path.exists('formated_images'):
            os.mkdir('formated_images')
        try:
            print "Name: " + os.path.splitext(ext)[0]
            print "Format: " + os.path.splitext(ext)[1]
            im.save('formated_images/'+ext)
            raw_input('Saved in formated_images.')
        except:
            raw_input('Error..')

    elif choice == "2":
        f_directory = raw_input('Directory to folder: ')
        ext = raw_input('Format: ')
        try:
            fieldlist = os.listdir(f_directory)
        except OSError:
            raw_input('Folder does not exist.')
            sys.exit()
        if not os.path.exists('formated_images'):
            os.mkdir('formated_images')
        print "Format: " + ext
        fieldlist_range = len(fieldlist)
        for item in fieldlist:
            directory = f_directory+ "\\" + item
            im = Image.open(directory)
            try:
                im.save('formated_images/'+os.path.splitext(item)[0]+'.'+ext)
                print "- " + os.path.splitext(item)[0] + " : " + "DONE"
                fieldlist_range-=1
                if fieldlist_range == 0:
                    raw_input('Saved in formated_images.')
            except:
                raw_input('Error..')
    elif choice == "3":
        os.system('cls')
        sys.exit()
    else:
        raw_input('Error')
        sys.exit()
        os.system('cls')

def make_thumbnail():
    print '''
    =====================
    Make thumbnail
    =====================
    1. File
    2. Folder
    3. Close
    =====================
    '''
    choice = raw_input(">> ")
    if choice == "1":
        directory = raw_input('Directory to file: ')
        name = raw_input('Save as: ')
        im = Image.open(directory)
        im.thumbnail((128, 128))
        if not os.path.exists('min_images'):
            os.mkdir('min_images')
        try:
            im.save('min_images/'+name)
            print "Name: " + name
            print "Size: " + str(im.size)
            raw_input('Saved in min_images.')
        except:
            raw_input('Error..')
    elif choice == "2":
        f_directory = raw_input('Directory to folder: ')
        try:
            fieldlist = os.listdir(f_directory)
        except OSError:
            raw_input('Folder does not exist.')
            sys.exit()
        extensions = ['JPG', 'PNG', 'JPEG', 'GIF']
        if not os.path.exists('min_images'):
            os.mkdir('min_images')
        for item in fieldlist:
            directory = f_directory+ "\\" + item
            im = Image.open(directory)
            if im.format in extensions:
                im.thumbnail((128, 128))
                im.save('min_images/'+item)
                print "- " + item + " " + str(im.size) + " : " + "DONE"
        raw_input('Saved in min_images.')
    elif choice == "3":
        os.system('cls')
        sys.exit()

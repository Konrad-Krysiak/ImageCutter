#Functions to Image Editor
from PIL import Image
import os, sys

class ImageResizer:

    def cut_image(self, directory, width, height, name):
        im = Image.open(directory)
        im = im.resize((width, height))
        if not os.path.exists('resized_images'):
            os.mkdir('resized_images')
        try:
            im.save('resized_images/'+name)
            print "- " + name + " : " + "DONE"
            raw_input("Saved in resized_images.")
            print "Size: " + str(width) + " x " + str(height)
        except:
            raw_input('Error..')
            
    def cut_image_folder(self, f_directory, width, height):
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
    
    def change_format(self, directory, ext):
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
            
    def change_format_folder(self, f_directory, ext):
        try:
            fieldlist = os.listdir(f_directory)
        except OSError:
            raw_input('Folder does not exist.')
            sys.exit()
        if not os.path.exists('formated_images'):
            os.mkdir('formated_images')
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

    def make_thumbnail(self, directory, name):
        im = Image.open(directory)
        im.thumbnail((128, 128))
        if not os.path.exists('thumbnails'):
            os.mkdir('thumbnails')
        try:
            im.save('thumbnails/'+name)
            print "Name: " + name
            print "Size: " + str(im.size)
            raw_input('Saved in thumbnails.')
        except:
            raw_input('Error..')
            
    def make_thumbnail_folder(self, f_directory):
        try:
            fieldlist = os.listdir(f_directory)
        except OSError:
            raw_input('Folder does not exist.')
            sys.exit()
        extensions = ['JPG', 'PNG', 'JPEG', 'GIF']
        if not os.path.exists('thumbnails'):
            os.mkdir('thumbnails')
        for item in fieldlist:
            directory = f_directory+ "\\" + item
            im = Image.open(directory)
            if im.format in extensions:
                im.thumbnail((128, 128))
                im.save('thumbnails/'+item)
                print "- " + item + " " + str(im.size) + " : " + "DONE"
        raw_input('Saved in thumbnails.')        

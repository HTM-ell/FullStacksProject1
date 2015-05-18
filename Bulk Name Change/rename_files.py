import os
from Tkinter import Tk
from tkFileDialog import askdirectory


def select_Dir():
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        dirname = askdirectory() # show an "Open" dialog box and return the path to the selected file
        return dirname

def rename_files():
    #(1) get file names from a folder
        selected_dir = select_Dir()
        file_list = os.listdir(selected_dir)
        saved_path = os.getcwd()
        print("Current Working Directory is " + saved_path)
        os.chdir(selected_dir)
    #(2) for each file, rename filename
        for file_name in file_list:
            os.rename(file_name, ''.join(i for i in file_name if not i.isdigit()))
        os.system('explorer ' + saved_path)
        os.chdir(saved_path)

rename_files()


        

import os
import Tkinter, Tkconstants, tkFileDialog

class RenameFiles(Tkinter.Frame):
    def __init__(self, root):
        Tkinter.Frame.__init__(self, root)
    
        # options for buttons
        button_opt = {'fill': Tkconstants.BOTH, 'padx': 1, 'pady': 1}
        Tkinter.Button(self, text='Rename Files', command=self.rename_files).pack(**button_opt)
    
    
      

    def rename_files(self):
    #(1) get file names from a folder
        dirname = tkFileDialog.askdirectory()
        file_list = os.listdir(dirname)
        print(file_list)
        return

if __name__=='__main__':
  root = Tkinter.Tk()
  RenameFiles(root).pack()
  root.mainloop()

        

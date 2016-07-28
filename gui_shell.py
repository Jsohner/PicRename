from Tkinter import *
import tkFileDialog
import Tkconstants
import pic_rename

class App(Frame):
    def __init__(self, master):
        # options for opening a directory
        self.dir_opt = options = {}
        options['initialdir'] = 'C:\\'
        options['mustexist'] = False
        options['parent'] = root
        options['title'] = 'Photo Rename'

        # options for buttons
        button_opt = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}

        frame =  Frame(width=400, height=400)
        frame.pack()

        # Input Directory
        self.import_directory_name = ''
        self.import_directory_label = Label(frame, text=self.import_directory_name)
        self.import_directory_label.grid(row=0)
        self.import_directory = Button(frame, text='Choose Import Directory', command=self.getInputDirectoryDialog)
        self.import_directory.grid(row=1)

        # Output Directory
        self.output_directory_name = ''
        self.output_directory_label = Label(frame, text=self.import_directory_name)
        self.output_directory_label.grid(row=2)
        self.output_directory = Button(frame, text='Choose Output Directory', command=self.getOutputDirectoryDialog)
        self.output_directory.grid(row=3)

        # Rename Button
        self.rename_button = Button(frame, text="Rename", command=self.rename)
        self.rename_button.grid(row=4)

        # Exit Button
        self.exit_button = Button(frame, text="Quit", command=frame.quit)
        self.exit_button.grid(row=5)

    def getInputDirectoryDialog(self):
        directory = tkFileDialog.askdirectory(**self.dir_opt)
        if directory:
            self.import_directory_name = directory
            self.import_directory_label['text'] = self.import_directory_name

    def getOutputDirectoryDialog(self):
        directory = tkFileDialog.askdirectory(**self.dir_opt)
        if directory:
            self.output_directory_name = directory
            self.output_directory_label['text'] = self.output_directory_name

    def rename(self):
        if not '/' in self.import_directory_name:
            print 'Please choose an input directory'
        if not '/' in self.output_directory_name:
            print 'Please choose an output directory'
        pic_rename.rename_pics(self.import_directory_name, self.output_directory_name)


if __name__ == '__main__':
    root = Tk()
    app = App(root)
    root.mainloop()
    root.destroy()

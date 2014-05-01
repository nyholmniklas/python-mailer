from Tkinter import *
from pymailer import PyMailer

class Gui:
    def __init__(self):
        threading.Thread.__init__(self)
        self.root = Tk()
        self.root.geometry("500x500")
        self.root.title("python-mailer")
        self._mailer = None
        self._init_components()
        self.root.mainloop()
        
    def _init_components(self):
        self._html_chooser_button = Tkinter.Button(self, text='Select HTML File', command=self._html_file_chooser)
        self._html_chooser_button = Tkinter.Button(self, text='Select CSV File', command=self._csv_file_chooser)
    
    def _layout_components(self):
        #TODO
        print("TODO")
        
    def _html_file_chooser(self):
        #TODO
        print("TODO")
        
    def _csv_file_chooser(self):
        #TODO
        print("TODO")
        
     
    
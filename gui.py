from Tkinter import *
#from pymailer import PyMailer

class Gui:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x500")
        self.root.title("python-mailer")
        self._mailer = None
        self._init_components()
        self._layout_components()
        self.root.mainloop()
        
    def _init_components(self):
        #Init frames
        self._input_frame = Frame(self.root, width = "240");
        
        #Init labels
        self._name_label = Label(self._input_frame, text="From Name: ")
        self._email_label = Label(self._input_frame, text="From Email: ")
        self._html_label = Label(self._input_frame, text="Load email: ")
        self._csv_label = Label(self._input_frame, text="Load recipients: ")
        self._host_label = Label(self._input_frame, text="Host: ")
        self._port_label = Label(self._input_frame, text="Port: ")
        self._subject_label = Label(self._input_frame, text="Subject: ")
        
        #Init entry widgets
        self._name_entry = Entry(self._input_frame)
        self._email_entry = Entry(self._input_frame)
        self._host_entry = Entry(self._input_frame)
        self._port_entry = Entry(self._input_frame)
        self._subject_entry = Entry(self._input_frame)
        
        #Init buttons
        self._html_button = Button(self._input_frame, text='Select HTML File', command=self._html_file_chooser)
        self._csv_button = Button(self._input_frame, text='Select CSV File', command=self._csv_file_chooser)
    
    def _layout_components(self): 
        #Layout frame
        self._input_frame.pack(pady=15, padx=15)
        
        #Layout labels
        self._name_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self._email_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        self._html_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)
        self._csv_label.grid(row=3, column=2, padx=5, pady=5, sticky=W)
        self._host_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        self._port_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)
        self._subject_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        
        #Layout entry widgets
        self._name_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        self._email_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        self._host_entry.grid(row=0, column=3, padx=5, pady=5, sticky=W)
        self._port_entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)
        self._subject_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        
        #Layout buttons
        self._html_button.grid(row=3, column=1, padx=5, pady=5, sticky=W)
        self._csv_button.grid(row=3, column=3, padx=5, pady=5, sticky=W)
        
    def _html_file_chooser(self):
        #TODO
        print("TODO")
        
    def _csv_file_chooser(self):
        #TODO
        print("TODO")

#MAIN
if __name__ == '__main__':
    ui = Gui()
     
    
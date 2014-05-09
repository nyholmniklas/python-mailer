from Tkinter import *
from config import *
from pymailer import PyMailer

class Gui:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("600x500")
        self.root.title("python-mailer")
        self._mailer = None
        self._init_widgets()
        self._layout_widgets()
        self._update_widgets()
        self.root.mainloop()
        
    def _init_widgets(self):
        #Init frames
        self._input_frame = Frame(self.root, width = "600");
        
        #Init labels
        self._name_label = Label(self._input_frame, text="From Name: ")
        self._email_label = Label(self._input_frame, text="From Email: ")
        self._html_label = Label(self._input_frame, text="Load email: ")
        self._csv_label = Label(self._input_frame, text="Load recipients: ")
        self._host_label = Label(self._input_frame, text="Host: ")
        self._port_label = Label(self._input_frame, text="Port: ")
        self._subject_label = Label(self._input_frame, text="Subject: ")
        self._username_label = Label(self._input_frame, text="Username: ")
        self._password_label = Label(self._input_frame, text="Password: ")
        
        #Init entry widgets
        self._name_entry = Entry(self._input_frame, width=30)
        self._email_entry = Entry(self._input_frame, width=30)
        self._host_entry = Entry(self._input_frame)
        self._port_entry = Entry(self._input_frame)
        self._subject_entry = Entry(self._input_frame, width=30)
        self._username_entry = Entry(self._input_frame)
        self._password_entry = Entry(self._input_frame, show="*")
        
        #Init checkbox
        self._auth_checkbox_checked = BooleanVar()
        self._auth_checkbox_checked.set(AUTH_SMTP)
        self._auth_checkbox = Checkbutton(self._input_frame, text="Use authentication", onvalue=True, offvalue=False, var=self._auth_checkbox_checked)
        self._auth_checkbox.configure(command=self._auth_checkbox_pressed)
        
        #Init buttons
        self._html_button = Button(self._input_frame, text='Select HTML File', command=self._html_file_chooser, width=25)
        self._csv_button = Button(self._input_frame, text='Select CSV File', command=self._csv_file_chooser, width=25)
        self._send_button = Button(self._input_frame, text='Send', command=self._send_button_pressed)
    
    def _layout_widgets(self): 
        #Layout frame
        self._input_frame.pack(pady=15, padx=15)
        
        #Layout labels
        self._name_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self._email_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        self._html_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)
        self._csv_label.grid(row=4, column=0, padx=5, pady=5, sticky=W)
        self._host_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        self._port_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)
        self._subject_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        self._username_label.grid(row=3, column=2, padx=5, pady=5, sticky=W)
        self._password_label.grid(row=4, column=2, padx=5, pady=5, sticky=W)
        
        #Layout entry widgets
        self._name_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        self._email_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        self._host_entry.grid(row=0, column=3, padx=5, pady=5, sticky=W)
        self._port_entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)
        self._subject_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        self._username_entry.grid(row=3, column=3, padx=5, pady=5, sticky=W)
        self._password_entry.grid(row=4, column=3, padx=5, pady=5, sticky=W)
        
        #Layout checkbox
        self._auth_checkbox.grid(row=2, column=3, padx=5, pady=5)
        
        #Layout buttons
        self._html_button.grid(row=3, column=1, padx=5, pady=5, sticky=W)
        self._csv_button.grid(row=4, column=1, padx=5, pady=5, sticky=W)
        self._send_button.grid(row=5, column=3, padx=10, pady=10, sticky=E)
        
    #Clear the widgets, assign values from config to widgets and update auth
    def _update_widgets(self):
        self._clear_widgets()
        self._name_entry.insert(0, FROM_NAME)
        self._email_entry.insert(0, FROM_EMAIL)
        self._host_entry.insert(0, SMTP_HOST)
        self._port_entry.insert(0, SMTP_PORT)
        self._username_entry.insert(0, USERNAME)
        self._password_entry.insert(0, PASSWORD)
        if (AUTH_SMTP):
            self._auth_checkbox_checked.set(True)
        else:
            self._auth_checkbox_checked.set(False)
        self._update_login_entries_enabled()
    

    #Clear all the entry widgets
    def _clear_widgets(self):
        self._name_entry.delete(0, END)
        self._email_entry.delete(0, END)
        self._host_entry.delete(0, END)
        self._port_entry.delete(0, END)
        self._subject_entry.delete(0, END)
        self._username_entry.delete(0, END)
        self._password_entry.delete(0, END)
    
    #Assign values from entry widgets to config variables
    def _update_config(self):
        global FROM_NAME, FROM_EMAIL, SMTP_HOST, SMTP_PORT, USERNAME, PASSWORD, AUTH_SMTP
        FROM_NAME = self._name_entry.get()
        FROM_EMAIL = self._email_entry.get()
        SMTP_HOST = self._host_entry.get()
        SMTP_PORT = self._port_entry.get()
        USERNAME = self._username_entry.get()
        PASSWORD = self._password_entry.get()
        AUTH_SMTP = self._auth_checkbox_checked.get()
    
    #Enable or disable the login entries depending on config variable AUTH_SMTP
    def _update_login_entries_enabled(self):
        if (AUTH_SMTP):
            self._username_entry.configure(state='normal')
            self._password_entry.configure(state='normal')
        else:
            self._username_entry.configure(state='disabled')
            self._password_entry.configure(state='disabled')
            
    #This function is given as command to auth_checkbox and is called when the checkbox is clicked
    def _auth_checkbox_pressed(self):
        self._update_config()
        self._update_widgets()

    def _html_file_chooser(self):
        #TODO
        print("TODO")
        
    def _csv_file_chooser(self):
        #TODO
        print("TODO")
        
    def _send_button_pressed(self):
        #TODO
        print("TODO")

#MAIN
if __name__ == '__main__':
    ui = Gui()
     
    
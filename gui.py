from Tkinter import *
from config import *
from pymailer import PyMailer

class Gui:
    def __init__(self, presenter):
        self.root = Tk()
        self.root.geometry("600x500")
        self.root.title("python-mailer")
        self.presenter = presenter

    def init(self):
        self._init_widgets()
        self._layout_widgets()
        self.presenter.update()
        self.root.mainloop()

    def _init_widgets(self):
        #Init frames
        self._input_frame = Frame(self.root, width = "600");

        #Init labels
        self.name_label = Label(self._input_frame, text="From Name: ")
        self.email_label = Label(self._input_frame, text="From Email: ")
        self.html_label = Label(self._input_frame, text="Load email: ")
        self.csv_label = Label(self._input_frame, text="Load recipients: ")
        self.host_label = Label(self._input_frame, text="Host: ")
        self.port_label = Label(self._input_frame, text="Port: ")
        self.subject_label = Label(self._input_frame, text="Subject: ")
        self.username_label = Label(self._input_frame, text="Username: ")
        self.password_label = Label(self._input_frame, text="Password: ")

        #Init entry widgets
        self.name_entry = Entry(self._input_frame, width=30)
        self.email_entry = Entry(self._input_frame, width=30)
        self.host_entry = Entry(self._input_frame)
        self.port_entry = Entry(self._input_frame)
        self.subject_entry = Entry(self._input_frame, width=30)
        self.username_entry = Entry(self._input_frame)
        self.password_entry = Entry(self._input_frame, show="*")

        #Init checkbox
        self.auth_checkbox_checked = BooleanVar()
        self.auth_checkbox_checked.set(AUTH_SMTP)
        self.auth_checkbox = Checkbutton(self._input_frame, text="Use authentication", onvalue=True, offvalue=False, var=self.auth_checkbox_checked)
        self.auth_checkbox.configure(command=self.presenter.auth_checkbox_pressed)

        #Init buttons
        self.html_button = Button(self._input_frame, text='Select HTML File', command=self.presenter.html_button_pressed, width=25)
        self.csv_button = Button(self._input_frame, text='Select CSV File', command=self.presenter.csv_button_pressed, width=25)
        self.send_button = Button(self._input_frame, text='Send', command=self.presenter.send_button_pressed)

    def _layout_widgets(self):
        #Layout frame
        self._input_frame.pack(pady=15, padx=15)

        #Layout labels
        self.name_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.email_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        self.html_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)
        self.csv_label.grid(row=4, column=0, padx=5, pady=5, sticky=W)
        self.host_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        self.port_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)
        self.subject_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        self.username_label.grid(row=3, column=2, padx=5, pady=5, sticky=W)
        self.password_label.grid(row=4, column=2, padx=5, pady=5, sticky=W)

        #Layout entry widgets
        self.name_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        self.host_entry.grid(row=0, column=3, padx=5, pady=5, sticky=W)
        self.port_entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)
        self.subject_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        self.username_entry.grid(row=3, column=3, padx=5, pady=5, sticky=W)
        self.password_entry.grid(row=4, column=3, padx=5, pady=5, sticky=W)

        #Layout checkbox
        self.auth_checkbox.grid(row=2, column=3, padx=5, pady=5)

        #Layout buttons
        self.html_button.grid(row=3, column=1, padx=5, pady=5, sticky=W)
        self.csv_button.grid(row=4, column=1, padx=5, pady=5, sticky=W)
        self.send_button.grid(row=5, column=3, padx=10, pady=10, sticky=E)


class Presenter():

    def __init__(self):
        self.model = ViewModel()
    
    def set_gui(self, gui):
        self.gui = gui
        
    def update(self):
        self._update_widgets()
        self._update_model()
    
    #Clear the widgets, assign values from model to widgets and update auth
    def _update_widgets(self):
        self._clear_widgets()
        self.gui.name_entry.insert(0, self.model.name)
        self.gui.email_entry.insert(0, self.model.email)
        self.gui.host_entry.insert(0, self.model.host)
        self.gui.port_entry.insert(0, self.model.port)
        self.gui.username_entry.insert(0, self.model.username)
        self.gui.password_entry.insert(0, self.model.password)
        if (self.model.auth):
            self.gui.auth_checkbox_checked.set(True)
        else:
            self.gui.auth_checkbox_checked.set(False)
        self._update_login_entries_enabled()
        
    #Clear all the entry widgets
    def _clear_widgets(self):
        self.gui.name_entry.delete(0, END)
        self.gui.email_entry.delete(0, END)
        self.gui.host_entry.delete(0, END)
        self.gui.port_entry.delete(0, END)
        self.gui.subject_entry.delete(0, END)
        self.gui.username_entry.delete(0, END)
        self.gui.password_entry.delete(0, END)
        
    #Assign values from entry widgets to model
    def _update_model(self):
        self.model.name = self.gui.name_entry.get()
        self.model.email = self.gui.email_entry.get()
        self.model.host = self.gui.host_entry.get()
        self.model.port = self.gui.port_entry.get()
        self.model.username = self.gui.username_entry.get()
        self.model.password = self.gui.password_entry.get()
        self.model.auth = self.gui.auth_checkbox_checked.get()
        self.model.subject = self.gui.subject_entry.get()
        
    #Enable or disable the login entries depending on model variable
    def _update_login_entries_enabled(self):
        if (self.model.auth):
            self.gui.username_entry.configure(state='normal')
            self.gui.password_entry.configure(state='normal')
        else:
            self.gui.username_entry.configure(state='disabled')
            self.gui.password_entry.configure(state='disabled')
        
    #This function is given as command to auth_checkbox and is called when the checkbox is clicked
    def auth_checkbox_pressed(self):
        #Cannot call update() here because we need to update model before widgets
        self._update_model()
        self._update_widgets()

    def html_button_pressed(self):
        #TODO
        print("TODO")

    def csv_button_pressed(self):
        #TODO
        print("TODO")

    def send_button_pressed(self):
        #TODO
        print("TODO")

class ViewModel():

    def __init__(self):
        self.name = FROM_NAME
        self.email = FROM_EMAIL
        self.host = SMTP_HOST
        self.port = SMTP_PORT
        self.username = USERNAME
        self.password = PASSWORD
        self.auth = AUTH_SMTP
        self.subject = ""
        
    
#MAIN
if __name__ == '__main__':
    presenter = Presenter()
    gui = Gui(presenter)
    presenter.set_gui(gui)
    gui.init()


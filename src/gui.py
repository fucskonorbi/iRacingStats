import customtkinter as ctk
import tkinter

import iracing_api as ir

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

appWidth, appHeight = 600, 700

class App(ctk.CTk):

    frames = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.username = None
        self.password = None
        self.valid_login = False
        self.title("iRacing API")
        self.geometry(f"{appWidth}x{appHeight}")
        self.resizable(False, False)

        # App.frames['loginframe'] = ctk.CTkFrame(self, width=appWidth, height=appHeight, bg_color="red")
        App.frames["loginframe"] = ctk.CTkFrame(self, width=appWidth, height=appHeight, bg_color="red")
        self.usernameLabel = ctk.CTkLabel(App.frames['loginframe'], text="Username")
        self.usernameLabel.grid(row=0, column=0, padx=20, pady=10)

        self.usernameEntry = ctk.CTkEntry(App.frames['loginframe'], placeholder_text="Enter your username", width=appWidth//2)
        self.usernameEntry.grid(row=0, column=1, padx=20, pady=10)

        self.passwordLabel = ctk.CTkLabel(App.frames['loginframe'], text="Password")
        self.passwordLabel.grid(row=1, column=0, padx=20, pady=10)

        self.passwordEntry = ctk.CTkEntry(App.frames['loginframe'], placeholder_text="Enter your password", show="*", width=appWidth//2)
        self.passwordEntry.grid(row=1, column=1, padx=20, pady=10)

        rememberMe = ctk.CTkCheckBox(App.frames['loginframe'], text="Remember me")
        rememberMe.grid(row=2, column=0, columnspan=2, padx=20, pady=20)

        self.loginButton = ctk.CTkButton(App.frames['loginframe'], text="Login", command=self.login)
        self.loginButton.grid(row=3, column=0, columnspan=2, padx=20, pady=20)

        App.frames["mainframe"] = ctk.CTkFrame(self, width=appWidth, height=appHeight, bg_color="blue")
        self.loginframe_selector()

        if self.valid_login:
            self.mainframe_selector()



    def login(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()

        self.username = username
        self.password = password
        self.valid_login = True
        print(self.username, self.password)


    def mainframe_selector(self):
        App.frames["loginframe"].pack_forget()
        App.frames["mainframe"].pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)


    def loginframe_selector(self):
        App.frames["mainframe"].pack_forget()
        App.frames["loginframe"].pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)


if __name__ == "__main__":
    app = App()
    app.mainloop()


import tkinter
import password
import customtkinter as CTk
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from PIL import Image
import pyperclip

class App(CTk.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("460x370")
        self.title("Password Generator")
        self.resizable(False, False)

        self.logo = CTk.CTkImage(dark_image=Image.open("img.png"), size=(460, 160))
        self.logo_label = CTk.CTkLabel(master=self, text="", image=self.logo)
        self.logo_label.grid(row=0, column=0)

        self.password_frame = CTk.CTkFrame(master=self, fg_color="transparent")
        self.password_frame.grid(row=1, column=0, padx=(20, 20), pady=(10, 10), sticky="nsew")

        self.entry_password = CTk.CTkEntry(master=self.password_frame, width=250)
        self.entry_password.grid(row=0, column=0, padx=(10, 20))

        # Button - Generate
        self.btn_generator = CTk.CTkButton(master=self.password_frame, text="Generate", width=50,
                                           command=self.set_password)
        self.btn_generator.grid(row=0, column=1)

        # Button - Copy
        self.btn_copy = CTk.CTkButton(master=self.password_frame, text="Copy", width=50,
                                      command=self.copy_password)
        self.btn_copy.grid(row=0, column=2, padx=10)

        self.settings_frame = CTk.CTkFrame(master=self)
        self.settings_frame.grid(row=2, column=0, padx=(20, 20), pady=(10, 0), sticky='nsew')

        self.password_length_slider = CTk.CTkSlider(master=self.settings_frame, from_=0, to=100, number_of_steps=100,
                                                    command=self.slider_event)
        self.password_length_slider.grid(row=1, column=0, columnspan=3, pady=(20, 20), sticky="ew")

        self.password_length_entry = CTk.CTkEntry(master=self.settings_frame, width=50)
        self.password_length_entry.grid(row=1, column=3, padx=(20, 10), sticky="we")

        self.cb_digits_var = tkinter.StringVar()
        self.cb_digits = CTk.CTkCheckBox(master=self.settings_frame, text="0-9", variable=self.cb_digits_var,
                                         onvalue=digits, offvalue="")
        self.cb_digits.grid(row=2, column=0, padx=10)

        self.cb_lower_var = tkinter.StringVar()
        self.cb_lower = CTk.CTkCheckBox(master=self.settings_frame, text="a-z", variable=self.cb_lower_var,
                                        onvalue=ascii_lowercase, offvalue="")
        self.cb_lower.grid(row=2, column=1)

        self.cb_upper_var = tkinter.StringVar()
        self.cb_upper = CTk.CTkCheckBox(master=self.settings_frame, text="A-Z", variable=self.cb_upper_var,
                                        onvalue=ascii_uppercase, offvalue="")
        self.cb_upper.grid(row=2, column=2)

        self.cb_symbol_var = tkinter.StringVar()
        self.cb_symbol = CTk.CTkCheckBox(master=self.settings_frame, text="@#$%", variable=self.cb_symbol_var,
                                         onvalue=punctuation, offvalue="")
        self.cb_symbol.grid(row=2, column=3)

        self.appearance_mode_option_menu = CTk.CTkOptionMenu(master=self.settings_frame,
                                                             values=["Light", "Dark"],
                                                             command=self.change_appearance_mode_event)
        self.appearance_mode_option_menu.grid(row=3, column=0, columnspan=4, pady=(10, 10))

        self.password_length_slider.set(12)
        self.password_length_entry.insert(0, 12)
        self.appearance_mode_option_menu.set("System")

    def change_appearance_mode_event(self, new_appearance_mode):
        CTk.set_appearance_mode(new_appearance_mode)

    def slider_event(self, value):
        self.password_length_entry.delete(0, "end")
        self.password_length_entry.insert(0, int(value))

    def get_charaterst(self):
        chars = "".join(self.cb_digits_var.get() + self.cb_lower_var.get() + self.cb_upper_var.get() + self.cb_symbol_var.get())
        return chars

    def set_password(self):
        try:
            self.entry_password.delete(0, "end")
            self.entry_password.insert(0, password.create_new(length=int(self.password_length_slider.get()),
                                                              characters=self.get_charaterst()))
        except:
            pass
    def copy_password(self):
        password = self.entry_password.get()
        pyperclip.copy(password)


if __name__ == '__main__':
    app = App()
    app.mainloop()

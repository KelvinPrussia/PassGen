import customtkinter
import customtkinter as ctk
import password_generator

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")


class app():

    def __init__(self):

        ## root window
        self.root = ctk.CTk()
        self.root.geometry("600x300")
        self.root.title("Password Generator")

        ## validate commands
        self.vcmd_num = (self.root.register(self.validate_num), '%P')
        self.vcmd_len = (self.root.register(self.validate_len), '%P')

        ## frames
        self.header_fr = ctk.CTkFrame(self.root, width=600)
        self.body_fr = ctk.CTkFrame(self.root)
        self.input_fr = ctk.CTkFrame(self.body_fr, height=250)
        self.output_fr = ctk.CTkFrame(self.body_fr, height=250)

        # root frame configuration
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.header_fr.grid(row=0, sticky="ew", ipady=5)
        self.body_fr.grid(row=1, sticky="nsew")

        self.body_fr.grid_rowconfigure(0, weight=1)
        self.body_fr.grid_columnconfigure(1, weight=1)

        self.input_fr.grid(row=0, column=0, sticky="nsew", padx=(5, 5), pady=5)
        self.output_fr.grid(row=0, column=1, sticky="nsew", padx=(0, 5), pady=5)

        # Widgets
        self.header_text = ctk.CTkLabel(self.header_fr, text="Password Generator", font=("Arial", 28), text_color="#2fa572")
        self.header_text.pack(expand=True)

        self.num = ctk.IntVar(value=1)
        self.num_slider_text = ctk.CTkLabel(self.input_fr, text="Number of Passwords", font=("Arial", 18), text_color="#2fa572")
        self.num_slider_text.pack(pady=(10, 0))
        self.num_entry = ctk.CTkEntry(self.input_fr, validate='all', validatecommand=self.vcmd_num,
                                      textvariable=self.num)
        self.num_entry.pack()
        self.num_slider = ctk.CTkSlider(self.input_fr,
                                        from_=1, to=10,
                                        variable=self.num)
        self.num_slider.pack(padx=5)

        self.pwd_len = ctk.IntVar(value=6)
        self.len_slider_text = ctk.CTkLabel(self.input_fr, text="Password length", font=("Arial", 18), text_color="#2fa572")
        self.len_slider_text.pack(pady=(20, 0))
        self.len_entry = ctk.CTkEntry(self.input_fr, validate='all', validatecommand=self.vcmd_len,
                                      textvariable=self.pwd_len)
        self.len_entry.pack()
        self.len_slider = ctk.CTkSlider(self.input_fr,
                                        from_=6, to=16,
                                        variable=self.pwd_len)
        self.len_slider.pack()

        self.gen_button = ctk.CTkButton(self.input_fr, text="Generate!", font=("Arial", 20), command=self.gen_pwds)
        self.gen_button.pack(expand=True, anchor=ctk.S, pady=(0, 10))

        self.output_text = ctk.CTkTextbox(self.output_fr,
                                          font=("arial", 19),
                                          corner_radius=10,
                                          state="disabled")

        self.output_text.pack(fill=ctk.BOTH, expand=True)

        # run
        self.root.mainloop()

    def gen_pwds(self):
        pwds = password_generator.gen_pwds(int(self.num_slider.get()), int(self.len_slider.get()))
        pwds_text = "\n".join(pwds)
        self.output_text.configure(state="normal")
        self.output_text.delete("0.0", ctk.END)
        self.output_text.insert("0.0", pwds_text)
        self.output_text.tag_config("center", justify="center")
        self.output_text.tag_add("center", "0.0", ctk.END)
        self.output_text.configure(state="disabled")

    def validate_num(self, P):
        if str.isdigit(P):
            if 1 <= int(P) <= 10:
                return True
            else:
                return False
        elif str(P) == "":
            return True
        else:
            return False

    def validate_len(self, P):
        if str.isdigit(P):
            if 6 <= int(P) <= 16:
                return True
            else:
                return False
        elif str(P) == "":
            return True
        else:
            return False


app()

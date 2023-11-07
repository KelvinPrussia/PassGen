import customtkinter
import customtkinter as ctk
import password_generator

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")


class GUI:

    def __init__(self):
        root = ctk.CTk()
        root.geometry("800x400")
        root.title("Password Generator")
        vcmd_num = (root.register(self.validate_num), '%P')
        vcmd_len = (root.register(self.validate_len), '%P')
        vcmd_sld = (root.register(self.validate_sld), '%P')

        header_fr = ctk.CTkFrame(root)
        body_fr = ctk.CTkFrame(root)
        input_fr = ctk.CTkFrame(body_fr)
        output_fr = ctk.CTkFrame(body_fr)

        body_fr.columnconfigure(0, weight=1)
        body_fr.columnconfigure(0, weight=1)

        header_text = ctk.CTkLabel(header_fr, text="Password Generator", font=("Arial", 15))
        header_text.pack()

        num = ctk.IntVar(value=1)
        num_slider_text = ctk.CTkLabel(input_fr, text="Number of Passwords")
        num_slider_text.pack()
        num_entry = ctk.CTkEntry(input_fr, validate='all', validatecommand=vcmd_num, textvariable=num)
        num_entry.pack()
        self.num_slider = ctk.CTkSlider(input_fr,
                                        from_=1, to=10,
                                        variable=num)
        self.num_slider.pack()

        pwd_len = ctk.IntVar(value=6)
        len_slider_text = ctk.CTkLabel(input_fr, text="Length of Passwords")
        len_slider_text.pack()
        len_entry = ctk.CTkEntry(input_fr, validate='all', validatecommand=vcmd_len, textvariable=pwd_len)
        len_entry.pack()
        self.len_slider = ctk.CTkSlider(input_fr,
                                        from_=6, to=16,
                                        variable=pwd_len)
        self.len_slider.pack()

        gen_button = ctk.CTkButton(input_fr, text="Generate!", font=("Arial", 10), command=self.gen_pwds)
        gen_button.pack()

        pwds = [""]
        output_text = ctk.CTkLabel(output_fr,
                                   text="Passwords will generate here",
                                   height=160,
                                   width=300,
                                   font=("arial", 16),
                                   textvariable=pwds,
                                   justify="left",
                                   anchor="nw",
                                   corner_radius=10,
                                   fg_color="transparent")
        output_text.pack()

        header_fr.pack()
        input_fr.grid(row=0, column=0)
        output_fr.grid(row=0, column=1, padx=10)
        body_fr.pack(pady=25)

        root.mainloop()

    def gen_pwds(self):
        password_generator.gen_pwds(int(self.num_slider.get()), int(self.len_slider.get()))

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

    def validate_sld(self, P):
        if str.isdigit(P):
            return True
        else:
            return False



GUI()

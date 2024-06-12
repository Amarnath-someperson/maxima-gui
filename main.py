import tkinter
import customtkinter as ctk
from PIL import Image
import latex  # latex.py


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_ctk_parent_class(tkinter.Tk)
        self.theme = "dark"
        # Modes: "System" (standard), "Dark", "Light"
        ctk.set_appearance_mode(self.theme)
        self.theme_col = "green"
        # Themes: "blue" (standard), "green", "dark-blue"
        ctk.set_default_color_theme(self.theme_col)

        self.title("MaximaGUI: An implmentation of maxima")
        self.geometry("550x650")
        self.minsize(400, 500)
        self.bind("<Return>", self.on_press)

        self.create()

    # ==========================================
    # structure of the app
    # ==========================================

    def create(self):
        latex.default_tex()
        self.in_frame = ctk.CTkFrame(master=self)
        self.in_frame.grid(row=0, column=0, padx=(20, 5), pady=20)

        self.out_frame = ctk.CTkFrame(master=self)
        self.out_frame.grid(row=0, column=1, padx=(5, 20), pady=20)

        input_heading = ctk.CTkLabel(
            master=self.in_frame, justify=ctk.LEFT, text="INPUT", font=("serif", 40, "bold"))
        input_heading.pack(pady=10, padx=10)

        input_help = ctk.CTkLabel(master=self.in_frame, justify=ctk.LEFT,
                                  text="If the input doesn't look quite right, use ().\n As of now, only matplotlib-latex commands work.")
        input_help.pack(pady=10, padx=10, anchor="w")

        self.textbox = ctk.CTkEntry(master=self.in_frame, width=300)
        self.textbox.pack(pady=10, padx=10, anchor="w")
        self.textbox.insert("0", "input (erase this)")

        self.image = ctk.CTkImage(Image.open('input.png'), size=(200, 200))
        self.image_label = ctk.CTkLabel(
            master=self.in_frame, image=self.image, text="")
        self.image_label.pack()

        self.report = ctk.CTkLabel(
            master=self.in_frame, text="No error logs (yet).")
        self.report.pack()

        output_heading = ctk.CTkLabel(
            master=self.out_frame, justify=ctk.LEFT, text="OUTPUT", font=("serif", 40, "bold"))
        output_heading.pack(pady=10, padx=10)

        footer_frame = ctk.CTkFrame(master=self)
        footer_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=(0, 20))

        theme_button = ctk.CTkButton(
            master=footer_frame, command=self.change_theme, text="Theme")
        theme_button.pack()

        footer = ctk.CTkLabel(master=footer_frame,
                              text="Bugs? Report them on github at my repo: Amarnath-someperson/maxima-gui")
        footer.pack()

    # ==========================================
    # on press of a button
    # ==========================================

    def on_press(self, event):
        try:
            expression = self.textbox.get()
            print(f"\033[0;35m>> \033[0;32mINPUT : {expression}\033[0;0m")
            print(f"\033[0;35m>> \033[0;34mEVENT : {event}\n\033[0;0m")
            latex.plt_tex(str(expression))
            self.image = ctk.CTkImage(Image.open(
                'input.png'), size=(self.in_frame.winfo_width()-20, 200))
            self.image_label.configure(image=self.image)
            self.report.configure(
                text="No errors detected.", text_color='green')
        except Exception as e:
            print(
                f"\033[0;36m{'='*20} EXCEPTION {'='*20}\n{e}\n{'='*20} EXCEPTION {'='*20}\n\033[0;0m")
            self.report.configure(
                text="Errors found. Check terminal for log.", text_color='red')

    # ==========================================
    # change theme
    # ==========================================

    def change_theme(self):
        def new_theme(
            self): return "dark" if self.theme == "light" else "light"
        self.theme = new_theme(self)
        ctk.set_appearance_mode(self.theme)


# ==========================================
# run if main
# ==========================================

if __name__ == "__main__":
    app = App()
    print(type(app), isinstance(app, tkinter.Tk))

    app.mainloop()

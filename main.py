import customtkinter as ctk
import tkinter
from PIL import Image
from customtkinter.windows.ctk_tk import CTk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_ctk_parent_class(tkinter.Tk)
        self.theme="dark"
        ctk.set_appearance_mode(self.theme)  # Modes: "System" (standard), "Dark", "Light"
        self.theme_col="blue"
        ctk.set_default_color_theme(self.theme_col)  # Themes: "blue" (standard), "green", "dark-blue"

        self.title("MaximaGUI: An implmentation of maxima")
        self.geometry("800x800")
        self.minsize(500,500)
        self.bind("<Enter>", self.on_press)

        self.create()

    def create(self):
        in_frame = ctk.CTkFrame(master=self)

        in_frame.grid(row=0,column=0)

        out_frame = ctk.CTkFrame(master=self)

        out_frame.grid(row=0,column=1)

        input_heading = ctk.CTkLabel(master=in_frame, justify=ctk.LEFT, text="INPUT", font=("serif",40, "bold"))
        input_heading.pack(pady=10, padx=10)

        output_heading = ctk.CTkLabel(master=out_frame, justify=ctk.LEFT, text="OUPUT", font=("serif",40, "bold"))
        output_heading.pack(pady=10, padx=10)

        textbox = ctk.CTkTextbox(master=in_frame)
        textbox.pack(pady=10, padx=10)
        textbox.insert("0.0", "Insert math here")

    def on_press(self, event):
        print("press of a button detected")
        pass









if __name__=="__main__":
    app=App()
    print(type(app), isinstance(app, tkinter.Tk))

    app.mainloop()

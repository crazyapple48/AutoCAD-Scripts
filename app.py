""" Main GUI File using CustomTkinter """

import tkinter as tk
import customtkinter as ctk

from tb import create_tb


class Windows(ctk.CTk):
    """"Main Window for App"""

    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)

        # Add Title to Window
        self.wm_title("AutoCAD Scripts")

        # creating a frame and assigning it to a container
        container = tk.Frame(self, height=400, width=600)
        # specifying where frame is packed in root
        container.pack(side="top", fill="both", expand=True)

        # configuring hte loation of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # create a dictionary of frames
        self.frames = {}
        # add components to the dictionary
        for f in (MainPage, TbForm):
            frame = f(container, self)

            # the windows class acts as the root window for the frames
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Method to switch frames
        self.show_frame(MainPage)

    def show_frame(self, cont):
        """Changes Visible Frame"""
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()


class MainPage(tk.Frame):
    """Welcome Page"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ctk.CTkLabel(self, text="Welcome to AutoCAD Scripts!")
        label.pack(padx=10, pady=10)

        switch_window_button = ctk.CTkButton(
            self, text="Titleblock Generator", command=lambda: controller.show_frame(TbForm))
        switch_window_button.pack(side="bottom", fill=ctk.X)


class TbForm(tk.Frame):
    """Titleblock Generator"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ctk.CTkLabel(self, text="Insert Relevant TB Information Below")
        label.pack(padx=10, pady=10)

        switch_window_button = ctk.CTkButton(
            self, text="Go back to main page", command=lambda: controller.show_frame(MainPage))
        switch_window_button.pack(side="bottom", fill=ctk.X)


if __name__ == "__main__":
    app = Windows()
    app.mainloop()

# # window
# window = ctk.CTk()
# window.title("AutoCAD Scripts")
# window.geometry('1080x720')

# # functions


# def run_tb_script():
#     """Runs tb.py Script"""
#     project = project_entry.get()
#     plate = page_title.get()
#     page = int(page_number.get())
#     page_var.set(page_var.get() + 1)
#     create_tb(project, plate, page)


# # widgets
# # title_block = ctk.CTkButton(
# #     window, text="Start Create TitleBlock", command=create_title_block)
# # title_block.pack()
# page_var = tk.IntVar(window, value=1)

# project_entry = ctk.CTkEntry(
#     window, placeholder_text="Enter Project Name")

# page_title = ctk.CTkEntry(window, placeholder_text="Enter Plate Title")

# page_number = ctk.CTkEntry(window, textvariable=page_var)

# project_entry.pack()
# page_title.pack()
# page_number.pack()


# submit_button = ctk.CTkButton(
#     window, text="Create TitleBlock", command=run_tb_script)
# submit_button.pack()


# # run
# window.mainloop()

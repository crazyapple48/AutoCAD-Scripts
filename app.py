""" Main GUI File using CustomTkinter """

import tkinter as tk
import customtkinter as ctk


# window
window = ctk.CTk()
window.title("AutoCAD Scripts")
window.geometry('1080x720')

# functions


def run_tb_script():
    """Runs tb.py Script"""
    project = project_entry.get()
    plate = page_title.get()
    page = int(page_number.get())
    page_var.set(page_var.get() + 1)
    print(project)
    print(plate)
    print(page)


# widgets
# title_block = ctk.CTkButton(
#     window, text="Start Create TitleBlock", command=create_title_block)
# title_block.pack()
page_var = tk.IntVar(window, value=1)

project_entry = ctk.CTkEntry(
    window, placeholder_text="Enter Project Name")

page_title = ctk.CTkEntry(window, placeholder_text="Enter Plate Title")

page_number = ctk.CTkEntry(window, textvariable=page_var)

project_entry.pack()
page_title.pack()
page_number.pack()


submit_button = ctk.CTkButton(
    window, text="Create TitleBlock", command=run_tb_script)
submit_button.pack()


# run
window.mainloop()

import tkinter
from tkinter import filedialog
import customtkinter
import pyttsx3
import PyPDF2
import os

def select_file():
    """Opens filedialog and uploads selected PDF file"""
    global pdf_file, name_without_filetype
    # Load file
    filetypes = (("PDF files", '.pdf'), ("all files", "*.*"))
    pdf_file = filedialog.askopenfilename(title="Select a file", initialdir="/", filetypes=filetypes)
    # Gets name of the selected file
    name_with_filetype = os.path.basename(pdf_file)
    name_without_filetype = os.path.splitext(name_with_filetype)[0]
    # Shows name of the selected file on screen
    text.configure(text=f"File selected:\n{name_with_filetype}", text_color="white")

def talk():
    page_n = page_num_box.get()
    if pdf_file and page_n:
        speaker = pyttsx3.init()

        # open pdf
        book = open(pdf_file, 'rb')
        # read pdf
        read_file = PyPDF2.PdfFileReader(book)
        # selecting page
        count = read_file.numPages
        text = ''
        for i in range(1,count):
            page = read_file.getPage(i)
            text += page.extract_text()


        speaker.say(text)
        speaker.runAndWait()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

window = customtkinter.CTk()
window.title("Audiobook")
window.geometry("400x300")
window.config(padx=50, pady=50)


text = customtkinter.CTkLabel(master=window, text="File selected:\nnone", width=280, height=100,
                              fg_color=("white", "#2e2e2e"), corner_radius=8, text_font=('Arial', 18))
text.place(relx=0.5, rely=0, anchor=tkinter.CENTER)


info_box = customtkinter.CTkLabel(master=window,text='Enter page number below\n↓ ' ,width=280,fg_color=("white", "#2e2e2e"), corner_radius=8, text_font=('Arial', 18))
info_box.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)


page_num_box = customtkinter.CTkEntry(master=window, width=200)
page_num_box.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

upload_button = customtkinter.CTkButton(master=window, text="Upload PDF file", width=200, command=select_file)
upload_button.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)


speak = customtkinter.CTkButton(master=window, text="Speak", width=200, command=talk)
speak.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

exit_prog = customtkinter.CTkButton(master=window, text="Exit", width=200, command=window.destroy)
exit_prog.place(relx=0.5, rely=1.05, anchor=tkinter.CENTER)
window.mainloop()

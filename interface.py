"""
    Description: Interface for the script.py file which uses the tkinter library
    to create a simple GUI. This GUI will allow the user to select document type and 
    folder description to sort into their respective folders.
"""


# Import Modules
import script
import tkinter as tk
from tkinter.ttk import *

def search_selected_files():
    try:
        if directory.get() == "":
            directory_folder = str(script.os.path.join(script.Path.home(), "Downloads"))
        else:
            directory_folder = directory.get()

        files = script.retrieve_all_files(directory_folder)
        for file in files:
            split_text = file.split(".")
            if powerpoint.get():
                script.check_document(split_text, directory_folder, file, script.powerpoint_extension, "PowerPoint")
            if pdf.get():
                script.check_document(split_text, directory_folder, file, script.pdf_extension, "PDF")
            if program.get():
                script.check_document(split_text, directory_folder, file, script.programming_extension, "Program Script")
            if picture.get():
                script.check_document(split_text, directory_folder, file, script.picture_extension, "Pictures")
        success_window()
    except:
        print("Error had occurred during execution")
        print("Possible issue, duplicate files were found")
        error_window()

# Create a mini quit window after selecting the document type
# When successfull
def success_window():
    window = tk.Tk()
    window.resizable(width=False, height=False)
    window.title("Successful")

    label = tk.Label(window, text = "Successfully sorted the selected documents in the selected directory: " + directory_folder +  ".\nYou may close the window")
    quit_button = tk.Button(window, text = "Quit", bd = '5', command = window.quit)

    label.grid(row = 0, column =0)
    quit_button.grid(row=1,column=0)
# Create a mini quit window after selecting the document type
# When there is an error
def error_window():
    window = tk.Tk()
    window.resizable(width = False, height = False)
    window.title("Error")

    label = tk.Label(window, text = "An error occurred. Please try again!")
    quit_button = tk.Button(window, text = "Quit", bd = '5', command = window.quit)

    label.grid(row = 0, column =0)
    quit_button.grid(row=1,column=0)
# Function to create check boxes
def create_checkBox():
    powerpointBox = tk.Checkbutton(selectFrame, text = 'PowerPoint',variable = powerpoint, onvalue = 1, offvalue = 0)
    pdfBox = tk.Checkbutton(selectFrame, text = 'PDFs', variable = pdf, onvalue = 1, offvalue = 0)
    programBox = tk.Checkbutton(selectFrame, text = 'Program Files', variable = program, onvalue = 1, offvalue = 0)
    pictureBox = tk.Checkbutton(selectFrame, text = 'Pictures', variable = picture, onvalue = 1, offvalue = 0)
    powerpointBox.grid(row = 2, column = 1, sticky = tk.W)
    pdfBox.grid(row = 3, column = 1, sticky = tk.W)
    programBox.grid(row = 4, column = 1, sticky = tk.W)
    pictureBox.grid(row = 5, column = 1, sticky = tk.W)

# Creates the description area that describes the 
# purposes the script/executable
def create_description_area():
    description_title_label = tk.Label(bottomLeftFrame, text="Description",font= ('Helvetica 13 underline'))
    description_title_label.grid(row = 0, column = 0, pady=1,padx=1)
    description_label = tk.Label(bottomLeftFrame, 
                                 text = "This is a simple python script.\nIt will sort out a particular folder \ninto selected options.\nSimply select which type of \ndocuments you want to sort, and then\n click Submit Selection\nDefault Location is Downloads Folder")
    
    description_label.grid(row=1, column= 0, pady=1,padx=1)
    
# Creation of the folder location area
def create_folder_location_area():
    label_directory = tk.Label(folderFrame, text = "Folder Location", height = 4)
    label_directory.grid(row = 0, column = 1)

    directory_name = tk.Entry(folderFrame, textvariable = directory, width = 50)
    directory_name.grid(row = 0, column = 2)

# Main Function
if __name__ == "__main__":
    directory_folder = ""

    # Main Window GUI
    window = tk.Tk()
    window.geometry("620x260")
    title = "Sorting Documents 101"
    window.title(title)

    # Creation of TK variables used in the script
    directory = tk.StringVar()
    powerpoint = tk.IntVar()
    pdf = tk.IntVar()
    program = tk.IntVar()
    picture = tk.IntVar()

    # Creation of Frames/Quadrants
    # Top Half Frame
    topFrame = tk.Frame(window)
    title_label = tk.Label(topFrame, text = "Welcome to " + title, font = ("Helvetica 19 underline"))
    title_label.pack()
    topFrame.grid(row = 0, column = 0)

    # Bottom Half Frame
    bottomFrame = tk.Frame(window)
    bottomFrame.grid(row = 1, column = 0)
    bottomLeftFrame = tk.Frame(bottomFrame, highlightbackground="blue", highlightthickness=2)
    bottomLeftFrame.grid(row = 0, column = 0)
    bottomRightFrame = tk.Frame(bottomFrame, highlightbackground="blue", highlightthickness=2)
    bottomRightFrame.grid(row = 0, column = 1)

    # Folder Location Frame
    folderFrame = tk.Frame(bottomRightFrame, highlightbackground = "blue")
    folderFrame.grid(row = 0, column = 0)


    # Selection/Checkboxes Frame
    selectFrame = tk.Frame(bottomRightFrame, highlightbackground="blue")
    selectFrame.grid(row = 1, column = 0, sticky = "w")
    label = tk.Label(selectFrame, text = "Select document types you want to sort", bd = 5, font= ('Helvetica 13 underline'))
    label.grid(row = 1, column = 1, sticky = tk.N, pady=3)

    # Call all helper function
    create_description_area()
    create_folder_location_area()
    create_checkBox()
    
    # Creation of the submit button
    btn = tk.Button(selectFrame, text = "Submit Selection", bd = '3', command = search_selected_files)
    btn.grid(row=5, column = 1)

    window.mainloop()
"""
    Description: Python Script to organize the downloads folder by grouping particular file extension together
    i.e. PDFs, PowerPoints, and Pictures

"""

# Import Modules
import os
import shutil
from pathlib import Path
import tkinter as tk

""" 
    Resources Links:
    https://blog.filestack.com/thoughts-and-knowledge/complete-image-file-extension-list/
    https://support.microsoft.com/en-au/office/file-formats-that-are-supported-in-powerpoint-252c6fa0-a4bc-41be-ac82-b77c9773f9dc

"""
# Global Variables / Setting the directory paths
current_directory = "./Files"
picture_extension = {                                             # Formats
                    "jpg","jpeg","jpe","jif","jfif","jfi",        # JPEG 
                    "png",                                        # PNG
                    "gif",                                        # GIF
                    "webp",                                       # WEBP --> Google combination of JPGs and PNGs
                    "tiff", "tif",                                # TIFF (Tagged Image File Format)
                    "psd",                                        # PSD (Adobe Photoshope Files)
                    "raw","arw","cr2","nrw","k25",                # RAW
                    "bmp", "dib",                                 # BMP (Bitmap Image Files)
                    "heif","heic",                                # HEIF (High Efficiency Image File) 
                    "ind", "indd", "indt",                        # INDD (Adobe InDesign Format)  
                    "jp2", "j2k", "jpf", "jpx", "jpm", "mj2",     # JPEG 2000
                    "svg", "svgz",                                # SVG (Vector Image File)
                    "ai",                                         # AI (Adobe-based Vector Image) 
                    "eps"                                         # EPS (Encapsulated PostScript Files)
}
pdf_extension = {
                    "pdf"
}

powerpoint_extension = {
                    "pptx", "pptm", "ppt", "potx","potm", "ppsx", "odp"
}

programming_extension = {
                    "py", "ipynb", "cpp", "c", "java"
}

# From the specified directory, only collect those which are files
# and ignore any/all subdirectories
def retrieve_all_files(specified_directory: str):
    file_list = []
    # Check each file in the specified directory
    for file in os.listdir(specified_directory):
        file_path = os.path.join(specified_directory, file)
        # Ignores all folders and only look at files
        if os.path.isfile(file_path):
            file_list.append(file)
    return file_list

# Check if the file has the correct extension
def check_document(split_text: str,current_directory,  file: str, extension: str, type_file: str):
    if split_text[-1] in extension:           # Extension
        # Check if the corresponding folder exist
        # if not, create the corresponding folder
        if not os.path.exists(current_directory + "/" + type_file):
            
            os.makedirs(current_directory + "/" + type_file)
        shutil.move(current_directory + "/" + file, current_directory + "/" + type_file)




"""This is the main module of the application.
It acts as as a 'middle man' between the model and view files
"""

# TODO: convertButton needs to be disabled until output_directory chosen

import sys

from tkinter import filedialog

from model import main_model
from app.view import main_view


def run_open_file_dialog():
    filename = filedialog.askopenfilename(initialdir="~", title="Select file",
                                          filetypes=(("csv files", "*.csv"),))
    if filename:
        main_model.selectedFiles.add(filename)


def run_open_folder_dialog():
    folder_name = filedialog.askdirectory(initialdir="~",
                                          title="Select folder")
    if folder_name:
        main_model.selectedDirectories.add(folder_name)


def select_output_directory():
    folder_name = filedialog.askdirectory(initialdir="~",
                                          title="Select output folder")
    if folder_name:
        main_model.outputDirectory = folder_name
        main_view.outputDirectoryLabel.config(text="Output to: {}".format(
            folder_name))

print(sys.path)

main_view.openFileButton.config(command=run_open_file_dialog)
main_view.openFolderButton.config(command=run_open_folder_dialog)
main_view.outputDirectoryButton.config(command=select_output_directory)
main_view.convertButton.config(command=main_model.convert_selected_files)

main_view.root.mainloop()

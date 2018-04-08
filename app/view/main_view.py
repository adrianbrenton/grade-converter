"""This module uses tkinter to create the main gui window"""

# TODO: Add widget to display all currently selected files
# TODO: Add title to the main window to replace "tk"
from tkinter import Tk, Label, Button, BOTTOM

root = Tk()


welcomeMessage = Label(root, text="Welcome to the Grade Adjuster!")
openFileButton = Button(root, text="Open File")
openFolderButton = Button(root, text="Open Folder")
outputDirectoryButton = Button(root, text="Choose Output Folder")
outputDirectoryLabel = Label(root)
convertButton = Button(root, text="Convert!")


welcomeMessage.pack(side=BOTTOM)
openFileButton.pack()
openFolderButton.pack()
outputDirectoryButton.pack()
outputDirectoryLabel.pack()
convertButton.pack()



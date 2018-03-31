"""This module uses tkinter to create the main gui window"""

# TODO: Add widget to display all currently selected files

from tkinter import *

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



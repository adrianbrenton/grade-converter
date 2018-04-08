# grade-converter

To try out this desktop app without bundling, simply run app/main_controller.py 
using python 3.5.

Please note: The lack of classes is intentional - modules are more 
appropriate ('pythonic') for this project because all the 'would-be' classes
follow the Singleton design pattern (multiple instances would be unnecessary).

This application adjusts students' test scores from a system of uneven grade 
boundaries to a system of even grade boundaries. A teacher from the US 
requested that I make this tool for her. 

In its current form, the app only works on csv files of a very specific 
layout and ou. This layout has been chosen to match the csv files that the 
teacher 
needs the app to work onb(deadline was ASAP). It is my future goal to make 
the app accept a wider range of layouts. For a full list of intended 
future improvements, see below.

To be bundled with py2app v0.13 (v0.14 has a bug that makes it incompatible 
with tkinter).

This is an ongoing project.

#Future Improvements (TODO)
- Add installer(s) for distribution.

- Add more tests.

- Add the option for the user to specify the column containing the scores to
 be adjusted.
 
- Add the option for the user to specify columns to be included in the new 
spreadsheet.

- Add the option for the user to specify alternative output file types.

- Add option for user to set different grade boundaries.

- Add capability for reading and adjusting xls and xlsx files.

- Add tkinter widget to display all currently selected files and directories
 to be adjusted.


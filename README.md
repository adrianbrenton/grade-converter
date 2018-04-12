# grade-converter

To try out this desktop app without bundling, simply navigate to the root 
directory of the project and run the following command:
python3.5 -m app.main_controller.py

Please note: The lack of classes is intentional - modules are more 
appropriate ('pythonic') for this project because all the 'would-be' classes
follow the Singleton design pattern (multiple instances would be unnecessary).

This application adjusts students' test scores from a system of uneven grade 
boundaries to a system of even grade boundaries. A teacher from the US 
requested that I make this tool for her. 

This is an ongoing project. In its current form, the app only works on csv 
files of a very specific layout. This layout has been chosen to match the 
csv files that the teacher needs the app to work on (the deadline was ASAP).
It is my future goal to make the app accept a wider range of spreadsheet 
layouts and file formats.

To be bundled with py2app v0.13 (v0.14 has a bug that makes it incompatible 
with tkinter).



# Future Improvements (TODO list)
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
 
- Think of a better name for app.


from glob import glob

from model import csv_converter as converter


def files_in_directories(directory_set):
    """Return a set of file paths from a set of directories"""
    csv_set = set()
    for directory in directory_set:
        for file_path in glob(directory + '/*'):
            if file_path.endswith('.csv'):
                csv_set.add(file_path)
    # TODO: consider set comprehension above instead of nested for-loops.
    return csv_set


def convert_selected_files():
    """Calls operate_on_csv method of test_grade_converter on selected files"""
    file_set = selectedFiles.union(files_in_directories(selectedDirectories))
    for filename in file_set:
        converter.operate_on_csv(filename, output_dir=outputDirectory)


selectedFiles = set()
selectedDirectories = set()
outputDirectory = ''


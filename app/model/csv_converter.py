"""Adjust grade spreadsheets based on new grade boundaries"""

# TODO Create Docstrings
# TODO Add this module to the model directory (because this is part of the business logic)
# TODO (create model, view and controller directories)
# TODO: change all output directories to be specified by user

import csv
from math import ceil
from os.path import splitext
from typing import Union

import xlsxwriter


def percent_to_float(percentage: Union[int, float, str]) -> float:
    """Return a float by stripping whitespace and percent symbol"""
    return float(str(percentage).strip().rstrip('%').rstrip())


def converted_score(score: float) -> int:
    """Return the adjusted score as a float, calculated from score argument

    score should be given as an integer
    """
    # level = [i for i, boundary in enumerate]
    for i, boundary in enumerate(gradeBoundaries):
        if boundary > score:
            level = i
            break
    else:
        level = 5
    new_score = ceil(
        (40 + level * 10 + 10 * (score - gradeBoundaries[level - 1]) /
         (gradeBoundaries[level] - gradeBoundaries[level - 1])) * 100) / 100
    return new_score


def operate_on_line(line, adjuster=converted_score):
    """Return a line from the csv with the student's score converted"""
    score = percent_to_float(line[2])
    new_line = line[:2]
    new_line.append(adjuster(score))  # TODO: adjuster works?
    return new_line


def operate_on_csv(csv_path, output_dir=''):
    """Opens the given csv file and calls operate_on_line() on each line"""
    with open(csv_path, 'r') as scoresFile:
        reader = csv.reader(scoresFile)
        output_file_name = splitext(scoresFile.name)[0].split('/')[
                               -1] + '_adjusted'
        list_of_rows = list(reader)[2:]

    new_rows_list = [operate_on_line(line) for i, line in enumerate(
        list_of_rows[1:])]  # TODO: is this enumerate() necessary?

    workbook = xlsxwriter.Workbook(
        output_dir + '/' + output_file_name + '.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.set_column(0, 0, 12)
    worksheet.set_column(1, 1, 25)
    worksheet.set_column(2, 2, 14)

    bold_format = workbook.add_format({'bold': True})
    worksheet.write_row('A1', ('Student ID', 'Student Name', 'Adjusted Score'),
                        bold_format)

    for i, line in enumerate(new_rows_list):
        worksheet.write_row(i + 1, 0, line)

    workbook.close()


gradeBoundaries = [0, 41, 48, 62, 71, 100]

from __future__ import print_function
from __future__ import unicode_literals

import csv


def make_csv(filename, comma_separated_header, rows_as_dict):
    with open(filename, 'wt') as file:
        writer = csv.DictWriter(file, comma_separated_header.split(','))
        writer.writerows(rows_as_dict)


def make_rovat_0_csv(rows):
    make_csv('rovat_0.csv', 'ceg_id,alrovat_id,megj', rows)


def make_rovat_1_csv(rows):
    make_csv('rovat_1.csv', 'ceg_id,alrovat_id,hattol,hatig,megj', rows)


def make_rovat_2_csv(rows):
    make_csv('rovat_2.csv', 'ceg_id,alrovat_id,hattol,hatig,megj', rows)


def write_file(filename, content):
    with open(filename, 'wt') as file:
        file.write(content)

from __future__ import print_function
from __future__ import unicode_literals

import os
import sys
import complex_schema


def generate_date_fixer(r_export_txt_xls, input_dir, output_dir):
    tables = complex_schema.read_tables(r_export_txt_xls)

    for table in tables:
        date_fields = [
            field.name
            for field in table.fields
            if field.type == 'date'
        ]

        if date_fields:
            input_file = '{}.csv'.format(
                os.path.normpath(os.path.join(input_dir, table.name))
            )
            output_file = '{}.csv'.format(
                os.path.normpath(os.path.join(output_dir, table.name))
            )

            if os.path.exists(input_file):
                command = 'drop-invalid-dates {} {} {}'.format(
                    ','.join(date_fields),
                    input_file,
                    output_file,
                )

                yield command


def main():
    r_export_txt_xls, input_dir, output_dir = sys.argv[1:]

    commands = generate_date_fixer(r_export_txt_xls, input_dir, output_dir)

    for command in commands:
        print(command)


if __name__ == '__main__':
    main()

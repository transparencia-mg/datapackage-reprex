import os
import pandas as pd
import re
from unidecode import unidecode

def convert_csv():
  upload_files = os.listdir('upload')
  for file in upload_files:
    if file.endswith('.xlsx') or file.endswith('.xls'):
        read_file = pd.read_excel (f'upload/{file}')
        read_file = read_file \
                    .replace('\n', ' ', regex=True) \
                    .replace('\r', '', regex=True)
        columns = read_file.columns
        new_columns = []
        for column in columns:
            new_columns.append(snake_small_case(column))
        csv_name = file.split('.xls')[0] # to xlsx and xls
        read_file.columns=new_columns

    # Remove white spaces from the beginning and the end of all columns
    for column in new_columns:
        # if column == 'distrito':
        #     import ipdb; ipdb.set_trace(context=10)
        # read_file[column] = [read_file[column][i].strip() \
        #                     for i in range(0, len(read_file)) \
        #                     if isinstance(read_file[column][i], str) \
        #                     else 'Na']
        read_file[column] = [read_file[column][i].strip() \
                             if isinstance(read_file[column][i], str) \
                             else read_file[column][i] \
                             for i in range(0, len(read_file))]

    #     for i in range(0, len(read_file)):
    #         if isinstance(read_file[column][i], str):
    #            read_file[column][i] = read_file[column][i].strip()

    read_file.to_csv (f'dataset/data/{csv_name}.csv', \
                    index = None, \
                    header=True, \
                    sep = ';', \
                    decimal = ',', \
                    encoding = 'utf-8-sig', \
                    na_rep = ""\
                    )

def snake_small_case(column):
  column_lower = column.lower()
  column_unidecode = unidecode(column_lower)
  column_alphanumeric = re.sub('[^A-Za-z0-9]+', ' ', column_unidecode)
  column_split = column_alphanumeric.split(' ')
  column_empty = [x for x in column_split if x != '']
  column = '_'.join(column_empty)
  return column

if __name__ == '__main__':
  convert_csv()

import numpy as np

from pandas import read_csv


def extract_file_x():
    return read_csv('../X.csv')


def extract_file_y():
    return read_csv('../Y.csv')


def extract_x_data():
    columns = extract_file_x()
    for key in columns:
        print('%s Calculation' % key)
        print('Mean: ', np.mean(columns[key]))
        print('Maximum: ', np.max(columns[key]))
        print('Minimum: ', np.min(columns[key]))
        print('25th percentile: ', np.percentile(columns[key], 25))
        print('90th percentile: ', np.percentile(columns[key], 90))
        print('Standard deviation: ', np.std(columns[key]))
        print('\n')


def extract_y_data():
    columns = extract_file_y()
    for key in columns:
        print('%s Calculation' % key)
        print('Mean: ', np.mean(columns[key]))
        print('Maximum: ', np.max(columns[key]))
        print('Minimum: ', np.min(columns[key]))
        print('25th percentile: ', np.percentile(columns[key], 25))
        print('90th percentile: ', np.percentile(columns[key], 90))
        print('Standard deviation: ', np.std(columns[key]))
        print('\n')


extract_x_data()
extract_y_data()

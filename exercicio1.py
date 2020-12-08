import csv
import numpy as np


def extract_X_data():
    columns = {'timestamp': [], 'idle': [], 'memused': [], 'proc': [], 'cswch': [], 'file': [], 'sum_intr': [],
               'ldavg': [], 'tcpsck': [], 'pgfree': []}
    with open('X.csv', newline='\n') as csv_file_x:
        file_x = csv.reader(csv_file_x)
        next(file_x)
        for index, data_x in enumerate(file_x, start=1):
            columns['timestamp'].append(int(data_x[0]))
            columns['idle'].append(float(data_x[1]))
            columns['memused'].append(float(data_x[2]))
            columns['proc'].append(float(data_x[3]))
            columns['cswch'].append(float(data_x[4]))
            columns['file'].append(int(data_x[5]))
            columns['sum_intr'].append(float(data_x[6]))
            columns['ldavg'].append(float(data_x[7]))
            columns['tcpsck'].append(int(data_x[8]))
            columns['pgfree'].append(float(data_x[9]))
    for key in columns:
        print('%s Calculation' % key)
        print('Mean: ', np.mean(columns[key]))
        print('Maximum: ', np.max(columns[key]))
        print('Minimum: ', np.min(columns[key]))
        print('25th percentile: ', np.percentile(columns[key], 25))
        print('90th percentile: ', np.percentile(columns[key], 90))
        print('Standard deviation: ', np.std(columns[key]))
        print('\n')


extract_X_data()
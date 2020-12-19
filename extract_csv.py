import csv
from pandas import read_csv

def extract_file_x():
    # columns = {'timestamp': [], 'idle': [], 'memused': [], 'proc': [], 'cswch': [], 'file': [], 'sum_intr': [],
    #            'ldavg': [], 'tcpsck': [], 'pgfree': []}
    # with open('X.csv', newline='\n') as csv_file_x:
    #     file_x = csv.reader(csv_file_x)
    #     next(file_x)
    #     for index, data_x in enumerate(file_x, start=1):
    #         columns['timestamp'].append(int(data_x[0]))
    #         columns['idle'].append(float(data_x[1]))
    #         columns['memused'].append(float(data_x[2]))
    #         columns['proc'].append(float(data_x[3]))
    #         columns['cswch'].append(float(data_x[4]))
    #         columns['file'].append(int(data_x[5]))
    #         columns['sum_intr'].append(float(data_x[6]))
    #         columns['ldavg'].append(float(data_x[7]))
    #         columns['tcpsck'].append(int(data_x[8]))
    #         columns['pgfree'].append(float(data_x[9]))
    return read_csv('X.csv')


def extract_file_y():
    # columns = {'timestamp': [], 'dispframes': []}
    # with open('Y.csv', newline='\n') as csv_file_y:
    #     file_y = csv.reader(csv_file_y)
    #     next(file_y)
    #     for index, data_y in enumerate(file_y, start=1):
    #         columns['timestamp'].append(int(data_y[0]))
    #         columns['dispframes'].append(float(data_y[1]))
    return read_csv('Y.csv')
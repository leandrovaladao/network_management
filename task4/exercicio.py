import warnings

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from extract_csv import extract_file_x, extract_file_y
import numpy as np


BASE_DIRECTORY = '../plots/task2/'


def do_linear_regression():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        #Task 4
        #Execicio 1
        x = extract_file_x()
        y = extract_file_y()

        x['DispFrames'] = y['DispFrames']

        train_x, test_x = train_test_split(x, test_size=0.3)

        #Exercicio 2
        dict_results = {}
        train_x_idle = train_x[['all_..idle', 'DispFrames']]
        test_x_idle = test_x[['all_..idle', 'DispFrames']]

        dict_results['all_..idle'] = do_linear_regression_and_nmae(train_x_idle, test_x_idle, 'Model Idle', True)

        train_x_memused = train_x[['X..memused', 'DispFrames']]
        test_x_memused = test_x[['X..memused', 'DispFrames']]

        dict_results['X..memused'] = do_linear_regression_and_nmae(train_x_memused, test_x_memused, 'Model Memused', True)

        train_x_proc = train_x[['proc.s', 'DispFrames']]
        test_x_proc = test_x[['proc.s', 'DispFrames']]

        dict_results['proc.s'] = do_linear_regression_and_nmae(train_x_proc, test_x_proc, 'Model proc', True)

        train_x_cswch = train_x[['cswch.s', 'DispFrames']]
        test_x_cswch = test_x[['cswch.s', 'DispFrames']]

        dict_results['cswch.s'] = do_linear_regression_and_nmae(train_x_cswch, test_x_cswch, 'Model cswch', True)

        train_x_file = train_x[['file.nr', 'DispFrames']]
        test_x_file = test_x[['file.nr', 'DispFrames']]

        dict_results['file.nr'] = do_linear_regression_and_nmae(train_x_file, test_x_file, 'Model file', True)

        train_x_sum_intr = train_x[['sum_intr.s', 'DispFrames']]
        test_x_sum_intr = test_x[['sum_intr.s', 'DispFrames']]

        dict_results['sum_intr.s'] = do_linear_regression_and_nmae(train_x_sum_intr, test_x_sum_intr, 'Model sum_intr', True)

        train_x_ldavg = train_x[['ldavg.1', 'DispFrames']]
        test_x_ldavg = test_x[['ldavg.1', 'DispFrames']]

        dict_results['ldavg.1'] = do_linear_regression_and_nmae(train_x_ldavg, test_x_ldavg, 'Model ldavg', True)

        train_x_tcpsck = train_x[['tcpsck', 'DispFrames']]
        test_x_tcpsck = test_x[['tcpsck', 'DispFrames']]

        dict_results['train_x_tcpsck'] = do_linear_regression_and_nmae(train_x_tcpsck, test_x_tcpsck, 'Model tcpsck', True)

        train_x_pgfree = train_x[['pgfree.s', 'DispFrames']]
        test_x_pgfree = test_x[['pgfree.s', 'DispFrames']]

        dict_results['pgfree.s'] = do_linear_regression_and_nmae(train_x_pgfree, test_x_pgfree, 'Model pgfree', True)


def do_linear_regression_and_nmae(train_x, test_x, model_name='', execute_print=False):

    model = LinearRegression()

    model.fit(train_x, train_x['DispFrames'])

    naive_mean = np.mean(train_x['DispFrames']).item()
    predict_results = model.predict(test_x)

    test_x['predict_results'] = predict_results

    sum_values = 0
    # Lista criada para conferir valores
    list_values = []
    for index, predict_result in enumerate(predict_results):
        list_values.append(abs(test_x['DispFrames'][test_x['DispFrames'].index[index]] - predict_result))
        sum_values += abs(test_x['DispFrames'][test_x['DispFrames'].index[index]] - predict_result)

    test_x['list_values'] = list_values

    NMAE = (sum_values / len(test_x)) / naive_mean
    test_x['predict_results'] = predict_results
    if execute_print:
        print('\n\n', model_name)
        print("Naive Mean: ", naive_mean)
        print("Normalized Mean Absolute Error: ", NMAE)
    return NMAE


do_linear_regression()
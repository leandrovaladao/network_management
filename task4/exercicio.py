import warnings

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv


def extract_file_x():
    return read_csv('../X.csv')


def extract_file_y():
    return read_csv('../Y.csv')

BASE_DIRECTORY = '../plots/task4/'


def do_linear_regression():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        #Task 4
        #Execicio 1
        x = extract_file_x()
        y = extract_file_y()

        x['DispFrames'] = y['DispFrames']

        train_x, test_x = train_test_split(x, test_size=0.3)

        #Exercicio 2 e 3
        std_dispframes = np.std(train_x['DispFrames'])
        mean_dispframes = np.mean(train_x['DispFrames'])
        dict_results = {}
        dict_correlation = {}

        train_x_idle = train_x[['all_..idle', 'DispFrames']]
        test_x_idle = test_x[['all_..idle', 'DispFrames']]

        dict_results['all_..idle'] = do_linear_regression_and_nmae(train_x_idle['all_..idle'],
                                                                   train_x_idle['DispFrames'],
                                                                   test_x_idle['all_..idle'],
                                                                   test_x_idle['DispFrames'], 'Model Idle', True)

        dict_correlation['all_..idle'] = do_correlation(train_x, 'all_..idle', mean_dispframes, std_dispframes)

        train_x_memused = train_x[['X..memused', 'DispFrames']]
        test_x_memused = test_x[['X..memused', 'DispFrames']]

        dict_results['X..memused'] = do_linear_regression_and_nmae(train_x_memused['X..memused'],
                                                                   train_x_memused['DispFrames'],
                                                                   test_x_memused['X..memused'],
                                                                   test_x_memused['DispFrames'],
                                                                   'Model Memused', True)

        dict_correlation['X..memused'] = do_correlation(train_x, 'X..memused', mean_dispframes, std_dispframes)

        train_x_proc = train_x[['proc.s', 'DispFrames']]
        test_x_proc = test_x[['proc.s', 'DispFrames']]

        dict_results['proc.s'] = do_linear_regression_and_nmae(train_x_proc['proc.s'], train_x_proc['DispFrames'],
                                                               test_x_proc['proc.s'], test_x_proc['DispFrames'],
                                                               'Model proc', True)

        dict_correlation['proc.s'] = do_correlation(train_x, 'proc.s', mean_dispframes, std_dispframes)

        train_x_cswch = train_x[['cswch.s', 'DispFrames']]
        test_x_cswch = test_x[['cswch.s', 'DispFrames']]

        dict_results['cswch.s'] = do_linear_regression_and_nmae(train_x_cswch['cswch.s'], train_x_cswch['DispFrames'],
                                                                test_x_cswch['cswch.s'], test_x_cswch['DispFrames'],
                                                                'Model cswch', True)

        dict_correlation['cswch.s'] = do_correlation(train_x, 'cswch.s', mean_dispframes, std_dispframes)

        train_x_file = train_x[['file.nr', 'DispFrames']]
        test_x_file = test_x[['file.nr', 'DispFrames']]

        dict_results['file.nr'] = do_linear_regression_and_nmae(train_x_file['file.nr'], train_x_file['DispFrames'],
                                                                test_x_file['file.nr'], test_x_file['DispFrames'],
                                                                'Model file', True)

        dict_correlation['file.nr'] = do_correlation(train_x, 'file.nr', mean_dispframes, std_dispframes)

        train_x_sum_intr = train_x[['sum_intr.s', 'DispFrames']]
        test_x_sum_intr = test_x[['sum_intr.s', 'DispFrames']]

        dict_results['sum_intr.s'] = do_linear_regression_and_nmae(train_x_sum_intr['sum_intr.s'], train_x_sum_intr['DispFrames'],
                                                                   test_x_sum_intr['sum_intr.s'], test_x_sum_intr['DispFrames'],
                                                                   'Model sum_intr', True)

        dict_correlation['sum_intr.s'] = do_correlation(train_x, 'sum_intr.s', mean_dispframes, std_dispframes)

        train_x_ldavg = train_x[['ldavg.1', 'DispFrames']]
        test_x_ldavg = test_x[['ldavg.1', 'DispFrames']]

        dict_results['ldavg.1'] = do_linear_regression_and_nmae(train_x_ldavg['ldavg.1'], train_x_ldavg['DispFrames'],
                                                                test_x_ldavg['ldavg.1'], test_x_ldavg['DispFrames'],
                                                                'Model ldavg', True)

        dict_correlation['ldavg.1'] = do_correlation(train_x, 'ldavg.1', mean_dispframes, std_dispframes)

        train_x_tcpsck = train_x[['tcpsck', 'DispFrames']]
        test_x_tcpsck = test_x[['tcpsck', 'DispFrames']]

        dict_results['tcpsck'] = do_linear_regression_and_nmae(train_x_tcpsck['tcpsck'], train_x_tcpsck['DispFrames'],
                                                               test_x_tcpsck['tcpsck'], test_x_tcpsck['DispFrames'],
                                                               'Model tcpsck', True)

        dict_correlation['tcpsck'] = do_correlation(train_x, 'tcpsck', mean_dispframes, std_dispframes)

        train_x_pgfree = train_x[['pgfree.s', 'DispFrames']]
        test_x_pgfree = test_x[['pgfree.s', 'DispFrames']]

        dict_results['pgfree.s'] = do_linear_regression_and_nmae(train_x_pgfree['pgfree.s'], train_x_pgfree['DispFrames'],
                                                                 test_x_pgfree['pgfree.s'], test_x_pgfree['DispFrames'],
                                                                 'Model pgfree', True)

        dict_correlation['pgfree.s'] = do_correlation(train_x, 'pgfree.s', mean_dispframes, std_dispframes)

        print('\nResultados do NMAE: ', dict_results)

        print('\nCorrelações: ', dict_correlation)

        for key in dict_correlation:
            dict_correlation[key] = dict_correlation[key]*dict_correlation[key]

        print('\nRank de correlações')
        colors_list = [1, 'green', 'blue', 'purple', 'red', 'orange', 'gray', 'black', 'pink', 'yellow']
        sorted_correlations = sorted(dict_correlation.values(), reverse=True)
        key_list = []
        plt.figure(figsize=(10, 10))
        for index, sorted_correlation in enumerate(sorted_correlations, start=1):
            key = get_key(sorted_correlation, dict_correlation)
            key_list.append(key)
            print('\n{} - {} - {}'.format(index, key, sorted_correlation))
            plt.bar(key, dict_results[key], color=colors_list[index], bottom=False)
        plt.legend(key_list)
        plt.savefig(BASE_DIRECTORY + 'exercicio3Method2hist.png', facecolor='w')
        plt.clf()

        colors_list = ['green', 'blue', 'purple', 'red', 'orange', 'gray', 'black', 'pink', 'yellow']
        plt.figure(figsize=(10, 10))
        for index, key in enumerate(dict_results):
            plt.bar(key, dict_results[key], color=colors_list[index], bottom=False)
        plt.legend(dict_results.keys())
        plt.savefig(BASE_DIRECTORY + 'exercicio2Method1hist.png', facecolor='w')
        plt.clf()


def get_key(val, my_dict):
    for key, value in my_dict.items():
         if val == value:
             return key


def do_correlation(train_x, field_name, mean_dispframes, std_dispframes):
    std_field = np.std(train_x[field_name])
    mean_field = np.mean(train_x[field_name])

    sum_correlation = 0
    for index, field in enumerate(train_x[field_name]):
        sum_correlation += ((field - mean_field) * (train_x['DispFrames'].values[index] - mean_dispframes)) / (std_field * std_dispframes)

    result_correlation = sum_correlation/len(train_x)

    return result_correlation


def do_linear_regression_and_nmae(train_x, train_x_dispframes, test_x, test_x_dispframes, model_name='', execute_print=False):

    model = LinearRegression()

    model.fit(train_x.values.reshape(-1, 1), train_x_dispframes)

    naive_mean = np.mean(train_x_dispframes)
    predict_results = model.predict(test_x.values.reshape(-1, 1))

    test_x['predict_results'] = predict_results

    sum_values = 0
    # Lista criada para conferir valores
    list_values = []
    for index, predict_result in enumerate(predict_results):
        list_values.append(abs(test_x_dispframes[test_x_dispframes.index[index]] - predict_result))
        sum_values += abs(test_x_dispframes[test_x_dispframes.index[index]] - predict_result)

    test_x['list_values'] = list_values

    NMAE = (sum_values / len(test_x)) / naive_mean
    test_x['predict_results'] = predict_results
    if execute_print:
        print('\n\n', model_name)
        print("Naive Mean: ", naive_mean)
        print("Normalized Mean Absolute Error: ", NMAE)
    return NMAE


do_linear_regression()

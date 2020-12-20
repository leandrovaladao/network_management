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


BASE_DIRECTORY = '../plots/task2/'


def do_linear_regression():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        #Task 2
        #Execicio 1
        #Inicio 1 A
        x = extract_file_x()
        y = extract_file_y()

        # y = y.loc[:, y.columns != 'TimeStamp']

        x['DispFrames'] = y['DispFrames']

        train_x, test_x = train_test_split(x, test_size=0.3)

        tmp_train_x = train_x.iloc[:, 2:10]
        tmp_test_x = test_x.iloc[:, 2:10]

        model = LinearRegression()

        model.fit(tmp_train_x, train_x['DispFrames'])

        print("Coeficientes: ", model.coef_)

        #Inicio 1 B
        naive_mean = np.mean(train_x['DispFrames'])
        predict_results = model.predict(tmp_test_x)

        test_x['predict_results'] = predict_results

        sum_values = 0
        # Lista criada para conferir valores
        list_values = []
        for index, predict_result in enumerate(predict_results):
            list_values.append(abs(test_x['DispFrames'][test_x['DispFrames'].index[index]]-predict_result))
            sum_values += abs(test_x['DispFrames'][test_x['DispFrames'].index[index]]-predict_result)

        test_x['list_values'] = list_values

        NMAE = (sum_values/len(test_x))/naive_mean

        print("Naive Mean: ", naive_mean)
        print("Normalized Mean Absolute Error: ", NMAE)

        #Inicio 1 C
        test_x.plot(x='TimeStamp', y=['DispFrames', 'predict_results'], style='o', mfc='none')
        plt.ylabel('Video Frame Rates')
        plt.legend(['Measured Video Frame Rates', 'Predict Results(Model)'])
        plt.savefig(BASE_DIRECTORY + 'exercicio1c.png', facecolor='w')
        plt.clf()

        #Inicio 1 D
        single_column_dataframe = test_x['DispFrames']
        single_column_dataframe.plot.kde()
        plt.savefig(BASE_DIRECTORY + 'exercicio1Ddensity.png', facecolor='w')
        plt.clf()

        single_column_dataframe = test_x['DispFrames']
        single_column_dataframe.plot.hist(bins=[x for x in range(30)])
        plt.savefig(BASE_DIRECTORY + 'exercicio1Dhist.png', facecolor='w')
        plt.clf()

        #Inicio 1 E
        single_column_dataframe = test_x['list_values']
        single_column_dataframe.plot.kde()
        plt.savefig(BASE_DIRECTORY + 'exercicio1Edensity.png', facecolor='w')
        plt.clf()

        # Exercicio 2
        # Inicio 2 A
        train_x_n50, test_x_n50 = train_test_split(train_x, train_size=50)
        train_x_n100, test_x_n100 = train_test_split(train_x, train_size=100)
        train_x_n200, test_x_n200 = train_test_split(train_x, train_size=200)
        train_x_n500, test_x_n500 = train_test_split(train_x, train_size=500)
        train_x_n1000, test_x_n1000 = train_test_split(train_x, train_size=1000)
        # train_x_n2520, test_x_n2520 = train_test_split(train_x, train_size=2520)

        # Inicio 2 B
        do_linear_regression_and_nmae(train_x_n50, test_x_n50, 'Modelo 2B n50', True)
        do_linear_regression_and_nmae(train_x_n100, test_x_n100, 'Modelo 2B n100', True)
        do_linear_regression_and_nmae(train_x_n200, test_x_n200, 'Modelo 2B n200', True)
        do_linear_regression_and_nmae(train_x_n500, test_x_n500, 'Modelo 2B n500', True)
        do_linear_regression_and_nmae(train_x_n1000, test_x_n1000, 'Modelo 2B n1000', True)
        do_linear_regression_and_nmae(train_x, test_x, 'Modelo 2B n2520', True)

        #Inicio 2 C-D
        nmae_n50 = []
        nmae_n100 = []
        nmae_n200 = []
        nmae_n500 = []
        nmae_n1000 = []
        nmae_n2520 = []
        for i in range(50):
            train_x_n50, test_x_n50 = train_test_split(train_x, train_size=50)
            train_x_n100, test_x_n100 = train_test_split(train_x, train_size=100)
            train_x_n200, test_x_n200 = train_test_split(train_x, train_size=200)
            train_x_n500, test_x_n500 = train_test_split(train_x, train_size=500)
            train_x_n1000, test_x_n1000 = train_test_split(train_x, train_size=1000)

            nmae_n50.append(do_linear_regression_and_nmae(train_x_n50, test_x_n50, ''))
            nmae_n100.append(do_linear_regression_and_nmae(train_x_n100, test_x_n100, ''))
            nmae_n200.append(do_linear_regression_and_nmae(train_x_n200, test_x_n200, 'Modelo 2B n50'))
            nmae_n500.append(do_linear_regression_and_nmae(train_x_n500, test_x_n500, 'Modelo 2B n50'))
            nmae_n1000.append(do_linear_regression_and_nmae(train_x_n1000, test_x_n1000, 'Modelo 2B n50'))
            nmae_n2520.append(do_linear_regression_and_nmae(train_x, test_x, 'Modelo 2B n50'))

        plt.boxplot([nmae_n50, nmae_n100, nmae_n200, nmae_n500, nmae_n1000, nmae_n2520])
        plt.savefig(BASE_DIRECTORY + 'exercicio2DerrorN50.png', facecolor='w')
        plt.clf()


def do_linear_regression_and_nmae(train_x, test_x, model_name='', execute_print=False):
    tmp_train_x = train_x.iloc[:, 2:10]
    tmp_test_x = test_x.iloc[:, 2:10]

    model = LinearRegression()

    model.fit(tmp_train_x, train_x['DispFrames'])

    naive_mean = np.mean(train_x['DispFrames'])
    predict_results = model.predict(tmp_test_x)

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

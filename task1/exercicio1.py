import numpy as np

from pandas import read_csv
import matplotlib.pyplot as plt


def extract_file_x():
    return read_csv('../X.csv')


def extract_file_y():
    return read_csv('../Y.csv')


BASE_DIRECTORY = ''

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


def get_number_of_observations_larger_than_eighty_percent():
    columns = extract_file_x()
    amount_value = 0
    for it in columns['X..memused']:
        if it > 80:
            amount_value += 1

    print('Quantidade acima de 80%: ', amount_value)


def get_mean_of_tec_with_more_than_eighteen_thousand_interrupts():
    columns = extract_file_x()
    list_tcp = []
    for index, it in enumerate(columns['sum_intr.s']):
        if it > 18000:
            list_tcp.append(columns['tcpsck'][index])

    print('Media de conexões tcp: ', np.mean(list_tcp))


def get_min_memory_utilization_for_cpu_lower_than_twenty_percent():
    columns = extract_file_x()
    min_memory = 100
    for index, it in enumerate(columns['all_..idle']):
        if it < 20:
            min_memory = columns['X..memused'][index] if columns['X..memused'][index] < min_memory else min_memory
    print('Minimo de memoria utilizada: ', min_memory)


def plot_cpu_and_memory():
    columns = extract_file_x()

    columns.plot(x='TimeStamp', y=['all_..idle', 'X..memused'])
    plt.legend(['Percentage of Idle CPU', 'Used Memory'])
    plt.savefig(BASE_DIRECTORY + 'exercicio3a.png', facecolor='w')
    plt.clf()


def plot_cpu_and_memory_graphs():
    columns = extract_file_x()
    plt.subplots(facecolor='w')

    single_column_dataframe = columns['X..memused']
    single_column_dataframe.plot.kde()
    plt.legend(['Used Memory'])
    plt.savefig(BASE_DIRECTORY + 'exercicio3densitymemory.png')
    plt.clf()

    single_column_dataframe = columns['all_..idle']
    single_column_dataframe.plot.kde()
    plt.legend(['Percentage of Idle CPU'])
    plt.savefig(BASE_DIRECTORY + 'exercicio3densityidle.png')
    plt.clf()

    single_column_dataframe = columns['X..memused']
    single_column_dataframe.plot.hist()
    plt.legend(['Used Memory'])
    plt.savefig(BASE_DIRECTORY + 'exercicio3histmemory.png')
    plt.clf()

    single_column_dataframe = columns['all_..idle']
    single_column_dataframe.plot.hist()
    plt.legend(['Percentage of Idle CPU'])
    plt.savefig(BASE_DIRECTORY + 'exercicio3histidle.png')
    plt.clf()

    single_column_dataframe = columns['X..memused']
    single_column_dataframe.plot.box()
    plt.legend(['Used Memory'])
    plt.xlabel('Used Memory')
    plt.savefig(BASE_DIRECTORY + 'exercicio3boxplotmemory.png')
    plt.clf()

    single_column_dataframe = columns['all_..idle']
    single_column_dataframe.plot.box()
    plt.legend(['Percentage of Idle CPU'])
    plt.xlabel('Percentage of Idle CPU')
    plt.savefig(BASE_DIRECTORY + 'exercicio3boxplotidle.png')
    plt.clf()


plot_cpu_and_memory()
plot_cpu_and_memory_graphs()


get_number_of_observations_larger_than_eighty_percent()
get_mean_of_tec_with_more_than_eighteen_thousand_interrupts()
get_min_memory_utilization_for_cpu_lower_than_twenty_percent()

extract_x_data()
extract_y_data()

import matplotlib.pyplot as plt

from pandas import read_csv


def extract_file_x():
    return read_csv('../X.csv')


BASE_DIRECTORY = ''


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

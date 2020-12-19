import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
import numpy as np

from extract_csv import extract_file_x

BASE_DIRECTORY = 'plots/task1/'

def plot_cpu_and_memory():
    columns = extract_file_x()
    columns.plot(x='TimeStamp', y=['all_..idle', 'X..memused'])
    plt.savefig(BASE_DIRECTORY+'exercicio3a.png')
    plt.clf()


def plot_cpu_and_memory_graphs():
    columns = extract_file_x()

    single_column_dataframe = columns['X..memused']

    single_column_dataframe.plot.kde()

    plt.savefig(BASE_DIRECTORY+'exercicio3densitymemory.png')
    plt.clf()

    single_column_dataframe = columns['all_..idle']

    single_column_dataframe.plot.kde()

    plt.savefig(BASE_DIRECTORY+'exercicio3densityidle.png')
    plt.clf()

    single_column_dataframe = columns['X..memused']

    single_column_dataframe.plot.hist()

    plt.savefig(BASE_DIRECTORY+'exercicio3histmemory.png')
    plt.clf()

    single_column_dataframe = columns['all_..idle']

    single_column_dataframe.plot.hist()

    plt.savefig(BASE_DIRECTORY+'exercicio3histidle.png')
    plt.clf()

    single_column_dataframe = columns['X..memused']

    single_column_dataframe.plot.box()

    plt.savefig(BASE_DIRECTORY+'exercicio3boxplotmemory.png')
    plt.clf()

    single_column_dataframe = columns['all_..idle']

    single_column_dataframe.plot.box()

    plt.savefig(BASE_DIRECTORY+'exercicio3boxplotidle.png')
    plt.clf()


plot_cpu_and_memory()
plot_cpu_and_memory_graphs()

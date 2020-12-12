import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
import numpy as np

from extract_csv import extract_file_x


def plot_cpu_and_memory():
    columns = extract_file_x()
    plt.plot(columns['proc'])
    plt.plot(columns['memused'])
    plt.ylabel('percent')
    plt.xlabel('amount')
    plt.savefig('plots/exercicio3a.png')
    plt.clf()


def plot_cpu_and_memory_graphs():
    columns = extract_file_x()

    data = columns['proc']
    data += columns['memused']
    density = gaussian_kde(data)

    x_vals = np.linspace(0, 20, 200)  # Specifying the limits of our data
    density.covariance_factor = lambda: .5  # Smoothing parameter

    density._compute_covariance()
    plt.plot(x_vals, density(x_vals))

    plt.savefig('plots/exercicio3density.png')
    plt.clf()

    columns = extract_file_x()
    plt.hist(columns['proc'])
    plt.hist(columns['memused'])
    plt.savefig('plots/exercicio3hist.png')
    plt.clf()

    plt.boxplot(columns['proc'])
    plt.boxplot(columns['memused'])
    plt.savefig('plots/exercicio3boxplot.png')
    plt.clf()

plot_cpu_and_memory()
plot_cpu_and_memory_graphs()
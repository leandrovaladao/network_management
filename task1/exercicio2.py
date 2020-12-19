import numpy as np
from extract_csv import extract_file_x


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
    for index, it in enumerate(columns['proc.s']):
        if it < 20:
            min_memory = columns['X..memused'][index] if columns['X..memused'][index] < min_memory else min_memory
    print('Minimo de memoria utilizada: ', min_memory)


get_number_of_observations_larger_than_eighty_percent()
get_mean_of_tec_with_more_than_eighteen_thousand_interrupts()
get_min_memory_utilization_for_cpu_lower_than_twenty_percent()
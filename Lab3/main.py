import math
import random
import time

from prettytable import PrettyTable
from matplotlib import pyplot as plt
from alg_1 import alg_1 as a1
from alg_2 import alg_2 as a2
from alg_3 import alg_3 as a3
from alg_4 import alg_4 as a4
from alg_5 import alg_5 as a5

if __name__ == '__main__':

    n = 10000
    step = int(n/10)
    digit_num = 4
    image_num = 1
    arr = [i for i in range(step, n, step)]
    time_results = list()

    # Alg 1

    current_results = list()

    for i in arr:
        start_time = time.perf_counter()
        a1(i)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        current_results.append(round(elapsed_time, digit_num))

    time_results.append(current_results)

    plt.figure(image_num)
    plt.plot(arr, time_results[0], label='Algorithm 1', color='blue')
    plt.xlabel('N elements checked')
    plt.ylabel('Elapsed time, s')
    plt.title('Algorithm 1')
    plt.legend()
    image_num += 1

    # Alg 2

    current_results = list()

    for i in arr:
        start_time = time.perf_counter()
        a2(i)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        current_results.append(round(elapsed_time, digit_num))

    time_results.append(current_results)

    plt.figure(image_num)
    plt.plot(arr, time_results[1], label='Algorithm 2', color='blue')
    plt.xlabel('N elements checked')
    plt.ylabel('Elapsed time, s')
    plt.title('Algorithm 2')
    plt.legend()
    image_num += 1

    # Alg 3

    current_results = list()

    for i in arr:
        start_time = time.perf_counter()
        a3(i)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        current_results.append(round(elapsed_time, digit_num))

    time_results.append(current_results)

    plt.figure(image_num)
    plt.plot(arr, time_results[2], label='Algorithm 3', color='blue')
    plt.xlabel('N elements checked')
    plt.ylabel('Elapsed time, s')
    plt.title('Algorithm 3')
    plt.legend()
    image_num += 1

    # Alg 4

    current_results = list()

    for i in arr:
        start_time = time.perf_counter()
        a4(i)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        current_results.append(round(elapsed_time, digit_num))

    time_results.append(current_results)

    plt.figure(image_num)
    plt.plot(arr, time_results[3], label='Algorithm 4', color='blue')
    plt.xlabel('N elements checked')
    plt.ylabel('Elapsed time, s')
    plt.title('Algorithm 4')
    plt.legend()
    image_num += 1

    # Alg 5

    current_results = list()

    for i in arr:
        start_time = time.perf_counter()
        a5(i)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        current_results.append(round(elapsed_time, digit_num))

    time_results.append(current_results)

    plt.figure(image_num)
    plt.plot(arr, time_results[4], label='Algorithm 5', color='blue')
    plt.xlabel('N elements checked')
    plt.ylabel('Elapsed time, s')
    plt.title('Algorithm 5')
    plt.legend()
    image_num += 1

    # Time results

    myTable = PrettyTable(['Sieve of E. Algs', *arr])
    myTable.add_row(["Alg 1", *time_results[0]])
    myTable.add_row(["Alg 2", *time_results[1]])
    myTable.add_row(["Alg 3", *time_results[2]])
    myTable.add_row(["Alg 4", *time_results[3]])
    myTable.add_row(["Alg 5", *time_results[4]])
    print(myTable)

    # All the graphs

    plt.figure(image_num)
    plt.plot(arr, time_results[0], label='Alg 1', color='black')
    plt.plot(arr, time_results[1], label='Alg 2', color='cyan')
    plt.plot(arr, time_results[2], label='Alg 3', color='green')
    plt.plot(arr, time_results[3], label='Alg 4', color='blue')
    plt.plot(arr, time_results[4], label='Alg 5', color='red')
    plt.xlabel('N elements checked')
    plt.ylabel('Elapsed time, s')
    plt.title('Sieve of Eratosthenes Algorithms')
    plt.legend()
    plt.show()

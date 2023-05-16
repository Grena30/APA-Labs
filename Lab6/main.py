from algorithms import *
import decimal
import math
from mpmath import mp
import time
import numpy as np
from matplotlib import pyplot as plt
from prettytable import PrettyTable

mp.dps = 1000000
decimal.getcontext().prec = 1000000
digits = [10, 100, 500, 1000, 5000, 15000]
original_pi = mp.pi
image_num = 1
pi_digits = []
times = []

digit_len = []
digit_c = []
digit_m = []
digit_g = []
error_c = []
error_m = []
error_g = []
accuracy = []

times_c = list()
times_g = list()
times_m = list()

# Chudnovsky algorithm

num = 100000
start_time = time.perf_counter()
pi_c = chudnovsky_pi(10 ** num)
end_time = time.perf_counter()
times.append(end_time - start_time)
digit_len.append(len(str(pi_c))-2)
# Gauss Legendre algorithm

start_time = time.perf_counter()
pi_g = gauss_legendre_pi(100, math.floor(num/5))
end_time = time.perf_counter()
times.append(end_time - start_time)
digit_len.append(len(str(pi_g))-1)

# Machin formula

start_time = time.perf_counter()
pi_m = machin_pi(num)
end_time = time.perf_counter()
times.append(end_time - start_time)
digit_len.append(len(str(pi_m))-1)

# Digit finding
for i in digits:

    pi_o = str(original_pi)[i]
    pi_digits.append(int(pi_o))

    if str(pi_c)[i] != pi_o:
        error_c.append(False)
    else:
        error_c.append(True)
    digit_c.append(int(str(pi_c)[i]))

    if str(pi_g)[i] != pi_o:
        error_g.append(False)
    else:
        error_g.append(True)
    digit_g.append(int(str(pi_g)[i]))

    if str(pi_m)[i] != pi_o:
        error_m.append(False)
    else:
        error_m.append(True)
    digit_m.append(int(str(pi_m)[i]))

# Accuracy

acc_c = abs(round((original_pi - pi_c), 50))
accuracy.append(acc_c)

acc_g = abs(round((original_pi - pi_g), 50))
accuracy.append(acc_g)

acc_m = abs(round((original_pi - pi_m), 50))
accuracy.append(acc_m)

for i in digits:
    # Chudnovsky algorithm
    start_time = time.perf_counter()
    pi_c = chudnovsky_pi(10 ** i)
    end_time = time.perf_counter()
    times_c.append(round((end_time - start_time), 6))

    # Gauss Legendre algorithm
    start_time = time.perf_counter()
    pi_g = gauss_legendre_pi(100, i)
    end_time = time.perf_counter()
    times_g.append(round((end_time - start_time), 6))

    # Machin formula
    start_time = time.perf_counter()
    pi_m = machin_pi(i)
    end_time = time.perf_counter()
    times_m.append(round((end_time - start_time), 6))

# Tables
myTable = PrettyTable(['Nth PI digit algorithms', 'Accuracy', 'Time to compute PI (s)', 'PI Digits'])
myTable.add_row(["Chudnovsky algorithm", accuracy[0], times[0], digit_len[0]])
myTable.add_row(["Gauss-Legendre algorithm", accuracy[1], times[1], digit_len[1]])
myTable.add_row(["Machin formula algorithm", accuracy[2], times[2], digit_len[2]])
print(myTable)

for i in myTable:
    print(i)

len_digit = 'Nth digit accuracy ' + str(digits)
act_digits = 'Actual PI digits ' + str(pi_digits)

myTable = PrettyTable(['Nth PI digit algorithms', *[len_digit], *[act_digits]])
myTable.add_row(["Chudnovsky algorithm", *[error_c], *[digit_c]])
myTable.add_row(["Gauss-Legendre algorithm", *[error_g], *[digit_g]])
myTable.add_row(["Machin formula algorithm", *[error_m], *[digit_m]])
print(myTable)

for i in myTable:
    print(i)

search_digit = 'Nth digit time taken ' + str(digits)

myTable = PrettyTable(['Nth PI digit algorithms', *[search_digit]])
myTable.add_row(["Chudnovsky algorithm", *[times_c]])
myTable.add_row(["Gauss-Legendre algorithm", *[times_g]])
myTable.add_row(["Machin formula algorithm", *[times_m]])
print(myTable)

for i in myTable:
    print(i)

# Graphs

arr = [i for i in range(3)]
x = np.arange(1, len(arr) - 1)

plt.figure(image_num)
plt.plot(digits, times_c, label='Chudnovsky', color='orange')
plt.xlabel('Algorithms')
plt.ylabel('Elapsed time, s')
plt.title('Computation of PI digits')
plt.legend()
image_num += 1

plt.figure(image_num)
plt.plot(digits, times_g, label='Gauss-Legendre', color='orange')
plt.xlabel('Algorithms')
plt.ylabel('Elapsed time, s')
plt.title('Computation of PI digits')
plt.legend()
image_num += 1

plt.figure(image_num)
plt.plot(digits, times_m, label='Machin', color='blue')
plt.xlabel('Algorithms')
plt.ylabel('Elapsed time, s')
plt.title('Computation of PI digits')
plt.legend()
image_num += 1

plt.figure(image_num)
plt.plot(digits, times_c, label='Chudnovsky', color='orange')
plt.plot(digits, times_g, label='Gauss-Legendre', color='black')
plt.plot(digits, times_m, label='Machin', color='blue')
plt.xlabel('Algorithms')
plt.ylabel('Elapsed time, s')
plt.title('Computation of PI digits')
plt.legend()
image_num += 1

plt.show()


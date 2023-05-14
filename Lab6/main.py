from algorithms import *
import decimal
import math
from mpmath import mp
import time
import numpy as np
from matplotlib import pyplot as plt
from prettytable import PrettyTable

mp.dps = 100000
decimal.getcontext().prec = 100000
digits = [5, 12, 25, 105, 970, 6780, 25430]
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

# Chudnovsky algorithm

start_time = time.perf_counter()
pi_c = chudnovsky_pi(100000)
end_time = time.perf_counter()
times.append(end_time - start_time)

# Set the decimal floating point to be at 3.14
len_c = len(str(pi_c))-1
digit_len.append(len_c)
pi_c = decimal.Decimal(pi_c)
pi_c = pi_c.scaleb(-len_c)

# Gauss Legendre algorithm

start_time = time.perf_counter()
pi_g = gauss_legendre_pi(100, 30000)
end_time = time.perf_counter()
times.append(end_time - start_time)
digit_len.append(len(str(pi_g))-1)

# Machin formula

start_time = time.perf_counter()
pi_m = machin_pi(100000)
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


# Tables
myTable = PrettyTable(['Nth PI digit algorithms', 'Accuracy', 'Time to compute PI (s)', 'PI Digits'])
myTable.add_row(["Chudnovsky algorithm", accuracy[0], times[0], digit_len[0]])
myTable.add_row(["Gauss-Legendre algorithm", accuracy[1], times[1], digit_len[1]])
myTable.add_row(["Machin formula algorithm", accuracy[2], times[2], digit_len[2]])
print(myTable)

for i in myTable:
    print(i)

digits = 'Nth digit accuracy ' + str(digits)
act_digits = 'Actual PI digits ' + str(pi_digits)

myTable = PrettyTable(['Nth PI digit algorithms', *[digits], *[act_digits]])
myTable.add_row(["Chudnovsky algorithm", *[error_c], *[digit_c]])
myTable.add_row(["Gauss-Legendre algorithm", *[error_g], *[digit_g]])
myTable.add_row(["Machin formula algorithm", *[error_m], *[digit_m]])
print(myTable)

for i in myTable:
    print(i)

# Graphs

arr = [i for i in range(1)]
x = np.arange(1, len(arr)+1)

plt.figure(image_num)
plt.bar(x-0.3, times[0], 0.2, label='Chudnovsky ', color='orange')
plt.bar(x-0.2, times[1], 0.2, label='Gauss-Legendre', color='cyan')
plt.bar(x-0.1, times[2], 0.2, label='Machin', color='blue')
plt.xlabel('Algorithms')
plt.ylabel('Elapsed time, s')
plt.title('Computation of PI')
image_num += 1
plt.legend()
plt.show()



import time
from matplotlib import pyplot as plt
from fibonacci_binet import fibonacci_binet as fib_b
from fibonacci_doubling import fib as fib_d
from fibonacci_dynamic_programming import fibonacci_dp as fib_dp
from fibonacci_kartik import fibonacci_kartik as fib_k
from fibonacci_matrix import fibonacci_matrix as fib_m
from fibonacci_matrix_optimized import fibonacci_matrix_op as fib_m_op
from fibonacci_recursive import fibonacci_recursive as fib_r

test_case1 = list(range(1, 40, 2))
test_case2 = list(range(1, 115000, 10000))
time_results = list()
x = 6

# Fibonacci Recursive graph

current_results = list()

for i in test_case1:
    start_time = time.perf_counter()
    fib_r(i)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    current_results.append(round(elapsed_time, x))

time_results.append(current_results)

plt.figure(1)
plt.plot(test_case1, time_results[0], label='Recursive', color='blue')
plt.xlabel('Nth Fibonacci Term')
plt.ylabel('Elapsed time, s')
plt.title('Recursive fibonacci')
plt.legend()

# Fibonacci Binet graph

current_results = list()

for i in test_case2:
    start_time = time.perf_counter()
    fib_b(i)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    current_results.append(round(elapsed_time, x))

time_results.append(current_results)

plt.figure(2)
plt.plot(test_case2, time_results[1], label='Binet', color='blue')
plt.xlabel('Nth Fibonacci Term')
plt.ylabel('Elapsed time, s')
plt.title('Binet fibonacci')
plt.legend()

# Fibonacci Doubling graph

current_results = list()

for i in test_case2:
    start_time = time.perf_counter()
    fib_d(i)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    current_results.append(round(elapsed_time, x))

time_results.append(current_results)

plt.figure(3)
plt.plot(test_case2, time_results[2], label='Doubling', color='blue')
plt.xlabel('Nth Fibonacci Term')
plt.ylabel('Elapsed time, s')
plt.title('Doubling fibonacci')
plt.legend()

# Fibonacci Dynamic programming graph

current_results = list()

for i in test_case2:
    start_time = time.perf_counter()
    fib_dp(i)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    current_results.append(round(elapsed_time, x))

time_results.append(current_results)

plt.figure(4)
plt.plot(test_case2, time_results[3], label='DP', color='blue')
plt.xlabel('Nth Fibonacci Term')
plt.ylabel('Elapsed time, s')
plt.title('Dynamic programming fibonacci')
plt.legend()

# Fibonacci Kartik graph

current_results = list()

for i in test_case2:
    start_time = time.perf_counter()
    fib_k(i+1)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    current_results.append(round(elapsed_time, x))

time_results.append(current_results)

plt.figure(5)
plt.plot(test_case2, time_results[4], label='Kartik', color='blue')
plt.xlabel('Nth Fibonacci Term')
plt.ylabel('Elapsed time, s')
plt.title('Kartik fibonacci')
plt.legend()

# Fibonacci matrix graph

current_results = list()

for i in test_case2:
    start_time = time.perf_counter()
    fib_m(i)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    current_results.append(round(elapsed_time, x))

time_results.append(current_results)

plt.figure(6)
plt.plot(test_case2, time_results[5], label='Matrix', color='blue')
plt.xlabel('Nth Fibonacci Term')
plt.ylabel('Elapsed time, s')
plt.title('Matrix fibonacci')
plt.legend()

# Fibonacci matrix optimized graph

current_results = list()

for i in test_case2:
    start_time = time.perf_counter()
    fib_m_op(i)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    current_results.append(round(elapsed_time, x))

time_results.append(current_results)

plt.figure(7)
plt.plot(test_case2, time_results[6], label='Matrix optimized', color='blue')
plt.xlabel('Nth Fibonacci Term')
plt.ylabel('Elapsed time, s')
plt.title('Matrix optimized')
plt.legend()

print("Test case 1:")
print(test_case1)
print("Recursive Fibonacci")
print(time_results[0])

print("Test case 2:")
print(test_case2)
print("Binet")
print(time_results[1])
print("Doubling Fibonacci")
print(time_results[2])
print("Dynamic Programming Fibonacci")
print(time_results[3])
print("Kartik's K Sequence")
print(time_results[4])
print("Matrix Fibonacci")
print(time_results[5])
print("Optimized Matrix")
print(time_results[6])

plt.figure(8)
plt.plot(test_case2, time_results[1], label='Binet', color='black')
plt.plot(test_case2, time_results[2], label='Doubling', color='cyan')
plt.plot(test_case2, time_results[3], label='Dynamic Programming', color='magenta')
plt.plot(test_case2, time_results[4], label='Kartik', color='green')
plt.plot(test_case2, time_results[5], label='Matrix', color='red')
plt.plot(test_case2, time_results[6], label='Optimized Matrix', color='blue')
plt.xlabel('Nth Fibonacci Term')
plt.ylabel('Elapsed time, s')
plt.title('Fibonacci graphs')
plt.legend()
plt.show()

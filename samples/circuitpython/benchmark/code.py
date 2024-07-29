import math
from gc import collect
from sys import platform


if platform in ["RP2040", "NXP IMXRT10XX"]:
    import ulab.numpy as np          # type: ignore
    #import circuitpython_csv as csv  # type: ignore
    MCU=True
else:
    import numpy as np               # type: ignore
    import csv                       # type: ignore
    MCU=False


def garbagecollect():
    collect()
    if MCU:
        from gc import mem_free
        memory_free = mem_free()
        print(memory_free)
        return memory_free
    else:
        return None


ITERATIONS = 1000000


def now():
    if MCU:
        from time import monotonic
        return monotonic()
    else:
        from time import perf_counter_ns
        return perf_counter_ns() / 1000000000

def measure(operation, x, y, name, iter=ITERATIONS):
    start_time = now()
    for _ in range(iter):
        operation(x, y)
    end_time = now()
    elapsed_time = end_time - start_time

    name = name.split(" ")
    print(f"{round(elapsed_time, 8)},{name[0]},{name[1]}")
    results.append([round(elapsed_time, 8), name[0], name[1]])
    return elapsed_time

# bitwise
def test_bitwise_and(x, y): return x & y
def test_bitwise_or(x, y): return x | y
def test_bitwise_xor(x, y): return x ^ y
def test_bitshift(x, y): return x << y  # left shift

# arithmetic
def test_add(x, y): return x + y
def test_sub(x, y): return x - y
def test_mul(x, y): return x * y
def test_div(x, y): return x / y
def test_mod(x, y): return x % y

# algebra
def test_sqrt(x, _): return math.sqrt(x)
def test_exp(x, _): return math.exp(x)  # x % 100
def test_log(x, _): return math.log(x)
def test_sqrt_np(x, _): return np.sqrt(x)
def test_exp_np(x, _): return np.exp(x)
def test_log_np(x, _): return np.log(x)

# trigonometry
def test_sin(x, _): return math.sin(x)
def test_cos(x, _): return math.cos(x)
def test_tan(x, _): return math.tan(x)
def test_sin_np(x, _): return np.sin(x)
def test_cos_np(x, _): return np.cos(x)
def test_tan_np(x, _): return np.tan(x)

# linear algebra
def test_matmul_np(A, B): return np.dot(A, B)

def test_matmul(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])

    # Create the result matrix
    C = [[0 for row in range(cols_B)] for col in range(rows_A)]

    # Perform the multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return C


bitshift_n = 100

# doubles
d1 = 1.2345678912345678
d2 = 9.876543219876543

# ints
i1 = int(d1*100000000)
i2 = int(d2*100000000)

# float32 1D arrays
array_len = 400  # 1000
float_dtype = np.float if MCU else np.float32
f1_array = np.full(array_len, d1, dtype=float_dtype)
f2_array = np.full(array_len, d2, dtype=float_dtype)

# reduced iterator count for arrays
iter = int(ITERATIONS/array_len)

garbagecollect()

results = []

print("\nWARMUP..")
warum_iterations = int(ITERATIONS/10) if MCU else int(ITERATIONS*10)
for _ in range(warum_iterations):
    test_add(i1, i2)

print("RUN BENCHMARK\n")

#bitwise
measure(test_bitshift, i1, bitshift_n, "int bitshift")
measure(test_mod, i1, i2, "int modulo")
measure(test_bitwise_and, i1, i2, "int bitwise-and")
measure(test_bitwise_or, i1, i2, "int bitwise-or")
measure(test_bitwise_xor, i1, i2, "int bitwise-xor")
# add
measure(test_add, i1, i2, "int add")
measure(test_add, d1, d2, "float add")
measure(test_add, f1_array, f2_array, "array(np.float) add", iter=iter)
# sub
measure(test_sub, i1, i2, "int sub")
measure(test_sub, d1, d2, "float sub")
measure(test_sub, f1_array, f2_array, "array(np.float) sub", iter=iter)
# mul
measure(test_mul, i1, i2, "int mul")
measure(test_mul, d1, d2, "float mul")
measure(test_mul, f1_array, f2_array, "array(np.float) mul", iter=iter)
# div
measure(test_div, i1, i2, "int div")
measure(test_div, d1, d2, "float div")
measure(test_div, f1_array, f2_array, "array(np.float) div", iter=iter)
# exp
measure(test_exp, i1//1000000, None, "int exp")
measure(test_exp, d1, None, "float exp")
measure(test_exp_np, f1_array, None, "array(np.float) exp", iter=iter)
# sqr
measure(test_sqrt, i1, None, "int sqr")
measure(test_sqrt, d1, None, "float sqr")
measure(test_sqrt_np,f1_array, None, "array(np.float) sqr", iter=iter)
# sin
measure(test_sin, d1, None, "float sin")
measure(test_sin_np, f1_array, None, "array(np.float) sin", iter=iter)
# cos
measure(test_cos, d1, None, "float cos")
measure(test_cos_np, f1_array, None, "array(np.float) cos", iter=iter) 
# tan
measure(test_tan, d1, None, "float tan")
measure(test_tan_np, f1_array, None, "array(np.float) tan", iter=iter)
# log
measure(test_log, d1, None, "float log")
measure(test_log_np, f1_array, None, "array(np.float) log", iter=iter)


garbagecollect()
    

mat_shape = [40,10]
mat_len = mat_shape[0]*mat_shape[1]
iter = 100

A_int = [[i+j for i in range(1, mat_shape[0]+1)] for j in range(mat_shape[1])]
B_int = [[i+j+10 for i in range(1, mat_shape[1]+1)] for j in range(mat_shape[0])]
measure(test_matmul, A_int, B_int, "for(int) matmul", iter=iter)

garbagecollect()
    
A_float = [[i/3+j for i in range(1, mat_shape[0]+1)] for j in range(mat_shape[1])]
B_float = [[i/3+j+10 for i in range(1, mat_shape[1]+1)] for j in range(mat_shape[0])]
measure(test_matmul, A_float, B_float, "for(float) matmul", iter=iter)

garbagecollect()
    
A_int16 = np.array(A_int, dtype=np.int16)
B_int16 = np.array(B_int, dtype=np.int16)
measure(test_matmul_np, A_int16, B_int16, "M(np.int16) matmul", iter=iter)

garbagecollect()
    
# A_float = np.array(A_float, dtype=float_dtype)
# B_float = np.array(B_float, dtype=float_dtype)
# measure(test_matmul_np, A_float, B_float, "M(np.float) matmul", iter=iter)

if not MCU:
    A_float64 = np.array(A_float, dtype=np.float64)
    B_float64 = np.array(B_float, dtype=np.float64)
    measure(test_matmul_np, A_float64, B_float64, "M(np.float64) matmul", iter=iter)

# save benchmark as CSV
if not MCU:
    with open('results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        # write header
        writer.writerow(['duration', 'datatype', 'operation'])
        # write data
        for result in results:
            writer.writerow(result)
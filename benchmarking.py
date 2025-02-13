import timeit
import numpy as np
#import multiprocessing
from gurke import BK#encapsulation, decapsulation, forking

# Benchmarking
num_trials = 5#200
sizes = [2**i for i in range(1, 11)]  # 2^1 bis 2^10
results = {"encapsulation": [], "decapsulation": [], "forking": []}

bk = BK.standard()
ad = 'ad'



for size in sizes:
    
    ek, dks = bk.gen(size)

    # Messung für jede Operation
    encap_time = timeit.repeat(lambda: bk.enc(ek), repeat=num_trials, number=1)

    u,c = bk.enc(ek)
    decap_time = timeit.repeat(lambda: bk.dec(dks[0], ad, c), repeat=num_trials, number=1)
    fork_time = timeit.repeat(lambda: bk.fork(ek), repeat=num_trials, number=1)

    # Median berechnen
    results["encapsulation"].append(np.median(encap_time))
    results["decapsulation"].append(np.median(decap_time))
    results["forking"].append(np.median(fork_time))

# Ergebnisse ausgeben
print("Benchmarking abgeschlossen!")
for key, values in results.items():
    print(f"{key}: {values}")


import matplotlib.pyplot as plt

# Data from the benchmarking
encapsulation = results['encapsulation']
decapsulation = results['decapsulation']
forking = results['forking']

# X-axis values (assumed as index values of the lists)
x = np.arange(1, 11)

# Plotting encapsulation
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.plot(x, encapsulation, marker='o', color='b', label='Encapsulation')
plt.title('Encapsulation')
plt.xlabel('Test Case')
plt.ylabel('Time (seconds)')
plt.grid(True)

# Plotting decapsulation
plt.subplot(1, 3, 2)
plt.plot(x, decapsulation, marker='o', color='g', label='Decapsulation')
plt.title('Decapsulation')
plt.xlabel('Test Case')
plt.ylabel('Time (seconds)')
plt.grid(True)

# Plotting forking
plt.subplot(1, 3, 3)
plt.plot(x, forking, marker='o', color='r', label='Forking')
plt.title('Forking')
plt.xlabel('Test Case')
plt.ylabel('Time (seconds)')
plt.grid(True)

# Show the plots
plt.tight_layout()
plt.savefig('benchmarking.png')
import matplotlib.pyplot as plt
import numpy as np

R = 200000
C = 100*10**(-6)

N = 1000
T = 80

t1 = np.linspace(0, T, N)
t2 = np.linspace(T, 2*T, N)

# Teoretisk
def v1(t):
    return 9*(1 - np.e**(-t/(R*C)))
def v2(t):
    return 9*np.e**(-t/(R*C))

# Praktisk
t_p1 = np.arange(0,90,10)
v_p1 = [0, 3.36, 5.63, 6.82, 7.60, 8.07, 8.32, 8.49, 8.60]

t_p2 = np.arange(80, 170, 10)
v_p2 = [8.60, 5.42, 3.38, 2.12, 1.35, 0.86, 0.57, 0.38, 0.25]

plt.plot(t1, v1(t1), 'b', t_p1, v_p1, 'r--')
plt.plot(t2, v2(t1), 'b', t_p2, v_p2, 'r--')
legends = ["Teoretisk modell","Praktiske målinger"]
plt.legend(legends)
plt.xlabel("Tid [s]")
plt.ylabel("Spenning over kondensator [V]")
plt.grid()
plt.show()
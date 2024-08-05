from fourier_katugampola import katugampola_fourier
import numpy as np

# Definisikan fungsi yang akan ditransformasikan
def my_function(x):
    return np.sin(x)

alpha = 1.5  # Contoh nilai alpha

results, k_values = katugampola_fourier(my_function, alpha)
print(results)
print(k_values)

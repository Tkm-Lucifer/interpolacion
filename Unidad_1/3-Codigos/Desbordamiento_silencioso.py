# Demostración: Desbordamiento Silencioso
# En numpy/enteros de ancho fijo, el overflow ocurre sin aviso

import numpy as np

print("Desbordamiento en enteros de 8 bits (int8, rango: -128 a 127)")
a = np.int8(120)
b = np.int8(20)
print(f"  120 + 20 = {a + b}  <- desbordamiento! el resultado correcto es 140")
print()

print("Desbordamiento en enteros de 16 bits (int16)")
c = np.int16(32000)
d = np.int16(1000)
print(f"  32000 + 1000 = {c + d}  <- desbordamiento! el resultado correcto es 33000")
print()

print("Python nativo no desborda (enteros de precision arbitraria):")
print(f"  120 + 20 = {120 + 20}  <- correcto")
print(f"  32000 + 1000 = {32000 + 1000}  <- correcto")

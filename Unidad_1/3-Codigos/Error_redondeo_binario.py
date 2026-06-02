# Demostración: Error de Redondeo Binario
# Algunos números no tienen representación exacta en binario

print("Ejemplos de error de redondeo binario:")
print()

# Muestra la representación real de algunos números
numeros = [0.1, 0.2, 0.3, 1.0 / 3.0, 2.0 / 3.0]
for n in numeros:
    print(f"  {n} -> representacion real: {n:.20f}")

print()
print("La famosa suma 0.1 + 0.2:")
resultado = 0.1 + 0.2
print(f"  0.1 + 0.2 = {resultado}")
print(f"  ¿Es igual a 0.3? {resultado == 0.3}")
print(f"  Diferencia: {abs(resultado - 0.3):.2e}")
print()
print(f"Epsilon de maquina (float64): {2**-52:.4e}")
print("Este es el error relativo máximo que puede introducir una operacion.")

# Demostración: Acumulación de Errores en Bucles
# La suma repetida de 0.1 acumula errores de punto flotante

def suma_con_float(iteraciones):
    """Suma 0.1 n veces usando float normal"""
    total = 0.0
    for _ in range(iteraciones):
        total += 0.1
    return total

def suma_esperada(iteraciones):
    """Valor matemáticamente correcto"""
    return iteraciones * 0.1

n = 1000
resultado_float = suma_con_float(n)
resultado_real = suma_esperada(n)
error = abs(resultado_float - resultado_real)

print(f"Suma con float ({n} iteraciones): {resultado_float}")
print(f"Valor esperado:                   {resultado_real}")
print(f"Error acumulado:                  {error:.2e}")
print()
print("Detalle del problema:")
print(f"  0.1 en binario no es exacto -> representacion: {0.1:.20f}")
print(f"  Epsilon de maquina: {2**-52:.2e}")

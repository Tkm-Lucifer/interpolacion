# Demostración: Cancelación Catastrófica
# Al restar números muy cercanos se pierden dígitos significativos

import math

def raiz_inestable(x):
    """Fórmula matemáticamente correcta pero numéricamente inestable"""
    return math.sqrt(x + 1) - math.sqrt(x)

def raiz_estable(x):
    """Fórmula algebraicamente equivalente pero numéricamente estable"""
    return 1.0 / (math.sqrt(x + 1) + math.sqrt(x))

print("Comparación de estabilidad numérica")
print(f"{'x':>12} | {'Inestable':>20} | {'Estable':>20}")
print("-" * 58)
for x in [1e2, 1e6, 1e10, 1e14]:
    inestable = raiz_inestable(x)
    estable = raiz_estable(x)
    print(f"{x:12.0e} | {inestable:20.15f} | {estable:20.15f}")

print()
print("A medida que x crece, la versión inestable pierde precisión.")

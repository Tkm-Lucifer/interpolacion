# Demostración: Pérdida de Precisión por Magnitud
# Sumar un número pequeño a uno muy grande hace que el pequeño desaparezca

print("Pérdida de precisión por diferencia de magnitud")
print()

casos = [
    (1e10,  0.001),
    (1e14,  1.0),
    (1e16,  1.0),
    (1e18,  100.0),
]

print(f"{'Grande':>12} + {'Pequeño':>10} = {'Resultado':>15} | {'Pequeño sobrevivio?':>20}")
print("-" * 70)
for grande, pequeno in casos:
    resultado = grande + pequeno
    sobrevivio = resultado != grande
    print(f"{grande:12.0e} + {pequeno:10.3f} = {resultado:15.1f} | {'Si' if sobrevivio else 'NO - se perdio'}")

print()
print("Cuando el número pequeño es menor que (grande * epsilon_maquina),")
print("sus bits caen fuera del rango de precision y son descartados.")

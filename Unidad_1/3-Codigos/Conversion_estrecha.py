# Demostración: Conversión Estrecha (Narrowing)
# Perder precisión al convertir de float64 a float32

import struct

def float64_to_float32(valor):
    """Simula la conversión de double a float"""
    # Empaquetar como float32 y desempaquetar para ver la pérdida
    bytes_f32 = struct.pack('f', valor)
    return struct.unpack('f', bytes_f32)[0]

valores = [3.141592653589793, 1.23456789012345, 0.0001234567890123]

print("Pérdida de precision por conversion estrecha (float64 -> float32)")
print(f"{'Valor original':>25} | {'Convertido (f32)':>20} | {'Error':>15}")
print("-" * 65)
for v in valores:
    convertido = float64_to_float32(v)
    error = abs(v - convertido)
    print(f"{v:25.15f} | {convertido:20.10f} | {error:15.2e}")

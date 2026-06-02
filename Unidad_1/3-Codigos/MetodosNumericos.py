# Métodos Numéricos - Demostración General
# Muestra el problema básico de representación en punto flotante

def main():
    a = 0.1 + 0.1 + 0.1
    b = 0.3
    
    print("=== Problema de representación de punto flotante ===")
    print(f"  a = 0.1 + 0.1 + 0.1 = {a:.20f}")
    print(f"  b = 0.3             = {b:.20f}")
    print()
    
    if a == b:
        print("Son exactamente iguales")
    else:
        print("Son DISTINTOS (diferencia de punto flotante)")
        print(f"  Diferencia: {abs(a-b):.2e}")

if __name__ == "__main__":
    main()

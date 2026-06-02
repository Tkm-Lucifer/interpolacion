# Errores Numéricos y de Precisión en Computadoras

Las computadoras no pueden representar todos los números reales de manera exacta. Esto se debe a que trabajan con un sistema binario de punto flotante (estándar IEEE 754), el cual tiene una capacidad finita de almacenamiento. Como consecuencia, existen distintos tipos de errores numéricos que todo programador debe conocer.

---

## 1. Acumulación de Errores en Bucles

### Concepto
Cuando se realizan operaciones aritméticas repetidas dentro de un ciclo, los pequeños errores de redondeo se van sumando iteración a iteración. Aunque el error en una sola operación sea microscópico (del orden de 10⁻¹⁶), al multiplicarse por millones de iteraciones puede producir un resultado completamente erróneo.

### Causa raíz
El número `0.1` no tiene representación binaria exacta. En binario se convierte en una fracción periódica infinita: `0.0001100110011...`. Al truncarse para caber en 64 bits, queda una pequeña diferencia respecto al valor real. Esta diferencia se suma cada vez que usamos ese número en un bucle.

### Ejemplo clásico
El caso más conocido ocurrió en 1991 con el misil Patriot: un error de punto flotante acumulado durante 100 horas de funcionamiento desplazó el cálculo del tiempo en 0.34 segundos, lo suficiente para fallar en la intercepción de un misil enemigo.

### Solución
Para evitar este error en aplicaciones críticas se deben usar tipos de dato de precisión arbitraria como `Decimal` en Python o `BigDecimal` en Java, que operan en base 10 y no tienen estos problemas de representación binaria.

```python
# Código relacionado:
```
[Acumulacion_de_erroresEnBucles.py](../3-Codigos/Acumulacion_de_erroresEnBucles.py)

---

## 2. Cancelación Catastrófica

### Concepto
La cancelación catastrófica ocurre al restar dos números muy cercanos entre sí. Cuando ambos números tienen muchos dígitos decimales significativos iguales, al restarlos esos dígitos se "cancelan" y el resultado queda con muy pocos bits de información útil, amplificando el error relativo de forma dramática.

### Ejemplo matemático
Supongamos que `a = 1.0000001` y `b = 1.0000000`. La diferencia exacta sería `0.0000001`. Sin embargo, si ambos valores tienen un pequeño error de representación en sus últimos bits, ese error puede ser mayor que el resultado esperado, haciendo que el cálculo sea completamente inválido.

### Cuándo ocurre
- Al evaluar fórmulas que involucran raíces cuadradas de números muy similares.
- Al calcular derivadas numéricas con un paso `h` muy pequeño.
- En la fórmula cuadrática cuando el discriminante es cercano a cero.

### Solución
Reformular la expresión algebraicamente para evitar la resta directa. Por ejemplo, la expresión `sqrt(x+1) - sqrt(x)` puede reescribirse como `1 / (sqrt(x+1) + sqrt(x))`, que es matemáticamente equivalente pero numéricamente estable.

[Cancelacion_resta.py](../3-Codigos/Cancelacion_resta.py)

---

## 3. Desbordamiento y Conversión Estrecha

### Desbordamiento (Overflow)
Ocurre cuando el resultado de una operación supera el valor máximo que puede almacenar un tipo de dato. En Python puro esto no es problema porque los enteros crecen automáticamente, pero en librerías como NumPy o en lenguajes como C/C++ es un error crítico.

### Conversión estrecha (Narrowing)
Se produce al convertir un tipo de dato de mayor precisión a uno de menor precisión, por ejemplo de `float64` a `float32`, o de `double` a `int`. Los bits que no caben en el tipo destino simplemente se descartan, introduciendo un error permanente.

[Conversion_estrecha.py](../3-Codigos/Conversion_estrecha.py)
[Desbordamiento_silencioso.py](../3-Codigos/Desbordamiento_silencioso.py)

---

## 4. Error de Redondeo Binario

### Concepto
Es el error fundamental de la aritmética de punto flotante: la diferencia entre el valor matemático exacto de un número y su representación binaria más cercana dentro de los 64 bits disponibles.

### Epsilon de máquina
El "epsilon de máquina" es el número más pequeño que, sumado a 1.0, produce un resultado diferente a 1.0. En Python con `float64`, este valor es aproximadamente `2.22 × 10⁻¹⁶`.

[Error_redondeo_binario.py](../3-Codigos/Error_redondeo_binario.py)

---

## 5. Pérdida de Precisión por Magnitud

### Concepto
Al sumar un número muy grande con un número muy pequeño, los bits que representan al número pequeño quedan fuera del rango de precisión del número grande y son descartados. El número pequeño desaparece del resultado como si no existiera.

### Ejemplo
`1e16 + 1.0` en punto flotante da exactamente `1e16`, como si el `1.0` nunca se hubiera sumado. Esto es porque `1e16` necesita todos los bits disponibles para representar su magnitud, y no queda espacio para el decimal.

[Perdida_precisionpormagnitud.py](../3-Codigos/Perdida_precisionpormagnitud.py)

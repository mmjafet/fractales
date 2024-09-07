import matplotlib.pyplot as plt
import numpy as np

# Función para generar la curva de Koch
def koch_curve(order, p1, p2):
    if order == 0:
        return np.array([p1, p2])
    
    # Dividir el segmento en tres partes
    p3 = (2 * p1 + p2) / 3
    p4 = (p1 + 2 * p2) / 3
    
    # Calcular el vértice superior del triángulo equilátero
    angle = np.pi / 3  # 60 grados en radianes
    direction = p4 - p3
    p5 = p3 + np.array([direction[0] * np.cos(angle) - direction[1] * np.sin(angle),
                        direction[0] * np.sin(angle) + direction[1] * np.cos(angle)])
    
    # Recursivamente generar la curva de Koch
    return np.concatenate([
        koch_curve(order - 1, p1, p3),
        koch_curve(order - 1, p3, p5),
        koch_curve(order - 1, p5, p4),
        koch_curve(order - 1, p4, p2)
    ])

# Función para generar el copo de nieve de Koch
def koch_snowflake(order):
    # Definir los tres vértices del triángulo equilátero
    p1 = np.array([0, 0])
    p2 = np.array([0.5, np.sqrt(3) / 2])
    p3 = np.array([1, 0])
    
    # Generar cada lado del triángulo con la curva de Koch
    side1 = koch_curve(order, p1, p2)
    side2 = koch_curve(order, p2, p3)
    side3 = koch_curve(order, p3, p1)
    
    # Concatenar los tres lados
    return np.concatenate([side1, side2, side3])

# Parámetros de la gráfica
order = 4  # Nivel de detalle del fractal (puedes cambiar este valor)
snowflake = koch_snowflake(order)

# Graficar el copo de Koch
plt.figure(figsize=(6, 6))
plt.plot(snowflake[:, 0], snowflake[:, 1], color="blue")
plt.title(f'Copo de Koch de orden {order}')
plt.axis('equal')
plt.show()

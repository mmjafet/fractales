import matplotlib.pyplot as plt
import numpy as np

# Función para generar el Triángulo de Sierpinski
def sierpinski_triangle(order, p1, p2, p3):
    if order == 0:
        # Dibujar un triángulo básico en el orden 0
        plt.fill([p1[0], p2[0], p3[0]], [p1[1], p2[1], p3[1]], 'b')
    else:
        # Calcular los puntos medios de cada lado del triángulo
        mid12 = (p1 + p2) / 2
        mid23 = (p2 + p3) / 2
        mid31 = (p3 + p1) / 2
        
        # Llamada recursiva para los tres triángulos más pequeños
        sierpinski_triangle(order - 1, p1, mid12, mid31)
        sierpinski_triangle(order - 1, mid12, p2, mid23)
        sierpinski_triangle(order - 1, mid31, mid23, p3)

# Parámetros de los vértices iniciales del triángulo equilátero
p1 = np.array([0, 0])
p2 = np.array([1, 0])
p3 = np.array([0.5, np.sqrt(3) / 2])  # Altura del triángulo equilátero

# Parámetro del orden (puedes cambiarlo para más detalle)
order = 6

# Crear la gráfica
plt.figure(figsize=(6, 6))
sierpinski_triangle(order, p1, p2, p3)
plt.gca().set_aspect('equal')
plt.axis('off')  # Ocultar los ejes
plt.title(f'Triángulo de Sierpinski de orden {order}')
plt.show()

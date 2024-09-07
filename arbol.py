import matplotlib.pyplot as plt
import numpy as np

# Función para dibujar el Árbol Fractal
def draw_tree(x, y, angle, length, depth):
    if depth == 0:
        return
    
    # Calcular la posición final de la rama usando trigonometría
    x_end = x + length * np.cos(angle)
    y_end = y + length * np.sin(angle)
    
    # Dibujar la rama
    plt.plot([x, x_end], [y, y_end], color="brown", lw=2*depth)

    # Ángulo de separación entre ramas
    angle_variation = np.pi / 6  # 30 grados
    
    # Llamadas recursivas para las dos ramas nuevas
    draw_tree(x_end, y_end, angle - angle_variation, length * 0.7, depth - 1)
    draw_tree(x_end, y_end, angle + angle_variation, length * 0.7, depth - 1)

# Parámetros iniciales del árbol
x_start = 0  # Coordenada x inicial
y_start = 0  # Coordenada y inicial
initial_angle = np.pi / 2  # El ángulo inicial apunta hacia arriba (90 grados)
initial_length = 1  # Longitud de la primera rama
depth = 9  # Número de niveles de profundidad del árbol

# Crear la gráfica
plt.figure(figsize=(6, 6))
draw_tree(x_start, y_start, initial_angle, initial_length, depth)
plt.title(f'Árbol Fractal de profundidad {depth}')
plt.gca().set_aspect('equal')
plt.axis('off')  # Ocultar los ejes
plt.show()

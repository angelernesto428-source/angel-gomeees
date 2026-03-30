
import matplotlib.pyplot as plt

# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]


plt.figure(figsize=(8, 4)) # Tamaño de la figura
plt.plot(x, y, label='Datos Lineales')

plt.title("Mi Primer Gráfico")
plt.xlabel("Eje X (Tiempo)")
plt.ylabel("Eje Y (Valor)")
plt.legend() # Muestra la leyenda
plt.grid(True) # Muestra la cuadrícula

plt.show()



y2 = [1, 4, 9, 16, 25]

plt.plot(x, y, color='green', marker='o', linestyle='--', label='Lineal')
plt.plot(x, y2, color='red', marker='s', linestyle='-', label='Cuadrática')

plt.title("Comparación de Funciones")
plt.legend()
plt.show()


categorias = ['A', 'B', 'C', 'D']
valores = [15, 24, 12, 30]

plt.bar(categorias, valores, color=['blue', 'orange', 'green', 'red'])
plt.title("Ventas por Categoría")
plt.show()
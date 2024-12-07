import matplotlib.pyplot as plt
import numpy as np

# Datos para el gráfico
outer_labels = ["Servicio General", "QBar", "Ingresos Netos"]
outer_sizes = [280_000, 240_500, 88_350]

inner_labels = [
    "Sueldos", "Gasolina", "Utilidad bruta",
    "Sueldos", "Insumos", "Utilidad bruta",
    "Material comprado", "Utilidad neta"
]
inner_sizes = [
    200_000, 19_400, 60_600,  # Servicio General
    111_000, 101_750, 27_750, # QBar
    16_786.5, 71_563.5        # Ingresos Netos
]
total=sum(outer_sizes)
outer_dis=100*np.array(outer_sizes)/total
outer_dis = np.around(outer_dis, 2)
outer_dis = [f'{i}%' for i in outer_dis]
# Colores consistentes
colors_outer = ['green', 'lightgreen', 'darkcyan']  # Tres colores principales para el anillo externo
colors_inner = [
    "indianred", "lightcoral", "springgreen",  # Servicio General
    "indianred", "salmon", "springgreen",  # QBar
    "paleturquoise", "#2ca02c"              # Ingresos Netos
]

# Crear el gráfico
fig, ax = plt.subplots(figsize=(9, 9))
fig.patch.set_alpha(0)
ax.patch.set_alpha(0)
# Anillo externo
sns.set(font_scale=2)
wedges_outer, _ = ax.pie(
    outer_sizes,
    labels=outer_labels,  # Etiquetas para el anillo externo
    colors=colors_outer,
    radius=1,
    wedgeprops=dict(width=0.3, edgecolor='w'),
    startangle=90,
    textprops={'fontsize': 12},
    labeldistance=.9
)

# Anillo interno
wedges_inner, texts,na = ax.pie(
    inner_sizes,
    labels=None,  # Desactivamos las etiquetas por ahora
    colors=colors_inner,
    radius=0.7,
    autopct='%.2f',
    wedgeprops=dict(width=0.4, edgecolor='w'),
    startangle=90
)

# Añadir etiquetas internas centradas en su respectivo sector
center_labels = ["Sueldos (SG)", "Sueldos (QBar)", "Insumos", "Utilidad neta"]
center_indices = [0, 3, 4, 7]  # Índices de las secciones que requieren etiquetas centradas

# Añadir flechas para las demás etiquetas
for i, (wedge, label) in enumerate(zip(wedges_inner, inner_labels)):
    ang = (wedge.theta2 + wedge.theta1) / 2
    x = 0.6 * np.cos(np.radians(ang))  # Coordenada x para el label
    y = 0.6 * np.sin(np.radians(ang))  # Coordenada y para el label
    # Condición para determinar si el label se coloca dentro o fuera
    if (wedge.theta2 - wedge.theta1) < 20:  # Si el ángulo es pequeño
        ax.annotate(
        label,
        xy=(x, y),
        xytext=(1.5*x,1.5*y),
        arrowprops=dict(facecolor='black', arrowstyle='->', lw=0.8),
        fontsize=12,
        ha='center'
    )
    else:
        # Colocar la etiqueta dentro
        ax.text(
            x, y, label,
            ha='center', va='center', fontsize=12, color="black"
        )
plt.style.use('dark_background')
# Añadir título
plt.title("Distribución de ingresos 2024", fontsize=25)
ax.legend(wedges_outer, outer_dis,
          title="Distribución",
          loc="upper left",
          bbox_to_anchor=(0.39, 0.585),
          fontsize=12,
          title_fontsize=15)
# Ajustar y mostrar el gráfico
plt.tight_layout()

plt.show()
plt.savefig('imaget.png')

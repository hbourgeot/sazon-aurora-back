from fastapi import APIRouter, Response
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

graph = APIRouter()

@graph.get('/ventas')
async def obtener_grafico_ventas():
    # Generando datos aleatorios para el gráfico
    dias = np.arange(1, 31)  # Días del mes
    ventas = np.random.randint(100, 500, size=len(dias))  # Ventas aleatorias

    # Creando el gráfico de barras con líneas
    plt.figure(figsize=(12, 6))
    plt.bar(dias, ventas, color='#ff8186', label='Ventas')  # Cambiado a 'firebrick'
    plt.plot(dias, ventas, color='darkred', marker='o', linestyle='-', linewidth=2, markersize=6)  # Cambiado a 'crimson'
    plt.xlabel('Días')
    plt.ylabel('Ventas')
    plt.title('Ventas por Día')
    plt.xticks(dias)
    plt.legend()
    plt.grid(True)

    # Guardando el gráfico en un buffer de memoria
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    # Devolviendo la imagen como respuesta
    return Response(content=buf.getvalue(), media_type="image/png")


@graph.get('/productos')
async def obtener_grafico_ventas():
    # Generando datos aleatorios para el gráfico
    dias = np.arange(1, 31)  # Días del mes
    ventas = np.random.randint(100, 500, size=len(dias))  # Ventas aleatorias

    # Creando el gráfico de barras con líneas
    plt.figure(figsize=(12, 6))
    plt.bar(dias, ventas, color='#ff8186', label='Ventas')  # Cambiado a 'firebrick'
    plt.plot(dias, ventas, color='darkred', marker='o', linestyle='-', linewidth=2, markersize=6)  # Cambiado a 'crimson'
    plt.xlabel('Días')
    plt.ylabel('Ventas')
    plt.title('Ventas por Día')
    plt.xticks(dias)
    plt.legend()
    plt.grid(True)

    # Guardando el gráfico en un buffer de memoria
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    print("aa")

    # Devolviendo la imagen como respuesta
    return Response(content=buf.getvalue(), media_type="image/png")

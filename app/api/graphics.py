from fastapi import APIRouter, Response
from app.supabase.functions.invoice import get_sales
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

graph = APIRouter()

@graph.get('/ventas')
async def obtener_grafico_ventas():
    # Generando datos aleatorios para el gráfico
    dias = []  # Días del mes
    ventas = [] 
    sales = get_sales()  # Ventas aleatorias
    for sale in sales:
        fecha = sale['fecha']
        fecha = fecha.strftime("%d-%m-%Y")
        dias.append(fecha)
        
        venta = sale['ventas']
        ventas.append(venta)

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
    dias = []  # Días del mes
    ventas = []
    sales = get_sales()  # Ventas aleatorias
    for sale in sales:
        fecha = sale['fecha']
        fecha = fecha.strftime("%d-%m-%Y")
        dias.append(fecha)

        venta = sale['ventas']
        ventas.append(venta)

    # Creando el gráfico de barras con líneas
    plt.figure(figsize=(12, 6))
    # Cambiado a 'firebrick'
    plt.bar(dias, ventas, color='#ff8186', label='Ventas')
    plt.plot(dias, ventas, color='darkred', marker='o', linestyle='-',
             linewidth=2, markersize=6)  # Cambiado a 'crimson'
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

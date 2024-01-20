# Imagen base de Python con una etiqueta que especifica la versión de Python.
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor.
WORKDIR /app

# Copiar el archivo de requisitos y instalar los paquetes necesarios.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código fuente del proyecto al directorio de trabajo.
COPY . .

# Exponer el puerto en el que se ejecutará la aplicación.
EXPOSE 8000

# Comando para ejecutar la aplicación usando Uvicorn.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

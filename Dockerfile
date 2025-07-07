# Dockerfile para microservice-order-create
FROM python:3.12-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requerimientos e instala dependencias
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación
COPY . .

# Expone el puerto de la aplicación
EXPOSE 4000

# Comando para ejecutar el servicio
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "4000"]

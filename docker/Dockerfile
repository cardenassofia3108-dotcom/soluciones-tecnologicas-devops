# ETAPA 1: Builder (Imagen pesada para instalar dependencias)
FROM python:3.9-slim AS builder
WORKDIR /app
COPY app.py .
# Instalamos flask en una carpeta local del usuario
RUN pip install --user flask

# ETAPA 2: Final (Imagen ligera solo con lo necesario para ejecutar)
FROM python:3.9-slim
WORKDIR /app

# Copiamos solo los paquetes instalados de la etapa anterior
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app/app.py .

# Aseguramos que Python encuentre los paquetes instalados y usamos el puerto 5000
ENV PATH=/root/.local/bin:$PATH
EXPOSE 5000

CMD ["python", "app.py"]
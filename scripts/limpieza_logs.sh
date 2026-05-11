#!/bin/bash
echo "Iniciando limpieza de logs antiguos para Brenda..."
mkdir -p ../logs
find ../logs -name "*.log" -type f -mtime +7 -delete
echo "Limpieza finalizada con éxito."

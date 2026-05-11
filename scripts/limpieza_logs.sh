#!/bin/bash
echo "Limpiando logs antiguos..."
find ./logs -name "*.log" -type f -mtime +7 -delete
echo "Limpieza lista."

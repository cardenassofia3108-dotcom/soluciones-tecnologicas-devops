import boto3
s3 = boto3.client('s3')
bucket_name = 'proyecto-final-brenda-1778544412'
file_name = 'evidencia_final.txt'
with open(file_name, 'w') as f:
    f.write('Archivo de prueba para Soluciones Tecnológicas del Futuro - Brenda')
s3.upload_file(file_name, bucket_name, f'pruebas/{file_name}')
print(f"Éxito: Archivo subido al bucket {bucket_name}")

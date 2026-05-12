import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

def ejecutar():
    print("Iniciando operaciones en DynamoDB...")
    try:
        # Crear tabla (simulado o verificación)
        table = dynamodb.create_table(
            TableName='devops-tabla',
            KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
            AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
            ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
        )
        print("Creando tabla devops-tabla...")
        table.meta.client.get_waiter('table_exists').wait(TableName='devops-tabla')
        print("Tabla creada exitosamente.")
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceInUseException':
            print("La tabla ya existe, procediendo...")
        else:
            print(f"Error: {e}")

    table = dynamodb.Table('devops-tabla')
    table.put_item(Item={'id': '1', 'nombre': 'Brenda', 'status': 'Activo'})
    print("Registro insertado con éxito.")

if __name__ == "__main__":
    ejecutar()

import boto3

def crear_usuarios():
    iam = boto3.client('iam')
    usuarios = ['Brenda-Admin', 'Brenda-Dev']
    print("--- Iniciando creación de usuarios ---")
    for nombre in usuarios:
        try:
            iam.create_user(UserName=nombre)
            print(f"✅ Usuario {nombre} creado con éxito.")
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    crear_usuarios()
import boto3

def revisar_infraestructura():
    # Clientes de AWS (Punto 4)
    ec2 = boto3.client('ec2', region_name='us-east-1')
    s3 = boto3.client('s3')
    cw = boto3.client('cloudwatch', region_name='us-east-1')
    asg = boto3.client('autoscaling', region_name='us-east-1')

    print("--- REVISIÓN DE INSTANCIAS EC2 ---")
    # describe_instances (Punto 4)
    instancias = ec2.describe_instances()
    for reserva in instancias['Reservations']:
        for i in reserva['Instances']:
            print(f"ID: {i['InstanceId']} - Estado: {i['State']['Name']}")

    print("\n--- REVISIÓN DE BUCKETS S3 ---")
    # list_buckets (Punto 4)
    buckets = s3.list_buckets()
    for b in buckets['Buckets']:
        print(f"Nombre: {b['Name']}")
        # list_objects_v2 (Punto 4)
        objetos = s3.list_objects_v2(Bucket=b['Name'])
        print(f"  Archivos encontrados: {objetos.get('KeyCount', 0)}")

    print("\n--- GRUPOS DE AUTO SCALING ---")
    # describe_auto_scaling_groups (Punto 4)
    grupos = asg.describe_auto_scaling_groups()
    for g in grupos['AutoScalingGroups']:
        print(f"Grupo: {g['AutoScalingGroupName']} - Capacidad: {g['DesiredCapacity']}")

if __name__ == "__main__":
    revisar_infraestructura()
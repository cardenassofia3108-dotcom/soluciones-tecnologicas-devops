import boto3
ec2 = boto3.resource('ec2', region_name='us-east-1')
print("--- Listado de Instancias EC2 ---")
for instance in ec2.instances.all():
    print(f"ID: {instance.id} | Tipo: {instance.instance_type} | Estado: {instance.state['Name']}")

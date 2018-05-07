import boto3

ec2_c = boto3.client('ec2')
_list_instances = ec2_c.describe_instances()['Reservations']

#range→存在するインスタンス数で回す
for i, name in enumerate(_list_instances):
    _instance_id = name['Instances'][0]['InstanceId']
    print(_instance_id)



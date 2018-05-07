import boto3

ec2_c = boto3.client('ec2')



_list_instances = ec2_c.describe_instances()['Reservations']

#range→存在するインスタンス数で回す
for i, _dict_name in enumerate(_list_instances):
    _dict_instances = _dict_name['Instances'][0]
    _instance_id = _dict_instances['InstanceId']
    print (_instance_id)




import boto3

ec2_c = boto3.client('ec2')



_list_instances = ec2_c.describe_instances()['Reservations']

#range→存在するインスタンス数で回す
for i, _dict_name in enumerate(_list_instances):
    _dict_instances = _dict_name['Instances'][0]
    _instance_id = _dict_instances['InstanceId']
    _state = _dict_instances['State']['Name']
#    _tags = parse_keyvalue_sets(instance['Tags'])
    print (_instance_id)
    print (_state)




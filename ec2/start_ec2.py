import boto3

ec2_c = boto3.client('ec2')


#    _state = __dict__['Instances'][0]['State']['Name']

instances = ec2_c.describe_instances()
#range→存在するインスタンス数で回す
#

#ec2_c.describe_instances()['Reservations'][0]['Instances'][0]

#def list_instances():
#    instances = ec2_c.describe_instances()
#    for _dict_reservation in instances['Reservations']:
#        for _dict_instance in _dict_reservation['Instances']:
#            instance_id = _dict_instance['InstanceId']
#            state = _dict_instance['State']['Name']
#            instance_name = _dict_instance['Tags']
#            print (type(instance_name)
#            #print (instance_id + ":" + state + ":" )
#
#list_instances()




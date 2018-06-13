import boto3

ec2_c = boto3.client('ec2')
a = ec2_c.describe_instances()




instanceId = a["Reservations"][2]["Instances"][0]['InstanceId']

print(instanceId)

import boto3

ec2_c = boto3.client('ec2')
a = ec2_c.describe_instances()


イメージとしては
no,instanceId,status(stop/start/terminated),tagsname,publicDNS,privateIP


instanceId = a["Reservations"][0]["Instances"][0]['InstanceId']


print(instanceId)

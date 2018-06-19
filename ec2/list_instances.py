import boto3

ec2_c = boto3.client('ec2')
instances = ec2_c.describe_instances()


#イメージとしては
#no,instanceId,status(stop/start/terminated),tagsname,publicDNS,privateIP


#instanceId = a["Reservations"][0]["Instances"][0]['InstanceId']

list_instances = instances["Reservations"]
for i in list_instances:
    a = i["Instances"][0]['InstanceId']
    b = i["Instances"][0]['State']['Name']
    c = i["Instances"][0]['Tags']
    print(a)
    print(b)
    print(c)
    
c


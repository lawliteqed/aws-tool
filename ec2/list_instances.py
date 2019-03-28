import boto3

ec2_c = boto3.client('ec2')
instances = ec2_c.describe_instances()
list_instances = instances["Reservations"]
#list_instances = instances["Reservations"]

for i in list_instances:
    instance_id = i["Instances"][0]['InstanceId']
    status = i["Instances"][0]['State']['Name']
    for j in i["Instances"][0]['Tags']:
        if ("Name" in j.values()):
            tag_name =j['Value']
#    private_ip = i["Instances"][0]['PrivateIpAddress']

    #print(instance_id,status,tag_name,private_ip, sep='\t')
    print(instance_id,status,tag_name, sep='\t')


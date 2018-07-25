#!/home/ec2-user/.pyenv/shims/python
import boto3
import sys

args = sys.argv
instace_id = args[1]

ec2_c = boto3.client('ec2')
instances = ec2_c.describe_instances(InstanceIds=[
          instace_id
      ])

list_instances = instances["Reservations"]
for i in list_instances:
    private_ip = i["Instances"][0]['PrivateIpAddress']
    print(private_ip, sep='\t')

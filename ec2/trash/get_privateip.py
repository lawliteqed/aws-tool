#!/home/ec2-user/.pyenv/shims/python
import sys
import boto3

ec2_c = boto3.client('ec2')
args = sys.argv

def usage():
    print( args[0] + " [instanceid]" )

def get_private_ip(instace_id):
    instances = ec2_c.describe_instances(InstanceIds=[instace_id])
    list_instances = instances["Reservations"]
    for i in list_instances:
        private_ip = i["Instances"][0]['PrivateIpAddress']
    print(private_ip)

try:
    get_private_ip(args[1])
except:
    usage()

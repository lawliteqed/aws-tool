#!/home/ec2-user/.pyenv/shims/python
import boto3

ec2_c = boto3.client('ec2')
list_nic = ec2_c.describe_network_interfaces()['NetworkInterfaces']

want_list = ["PrivateIpAddress", "NetworkInterfaceId", "SubnetId", "Status"]

def get_list_key(obj_list, get_list):
    for i in obj_list:
        for j in get_list:
            print(i[j], end='\t')
        print('\n', end='')

get_list_key(list_nic, want_list)

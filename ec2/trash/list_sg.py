#!/home/ec2-user/.pyenv/shims/python
import boto3

def get_list_key(obj_list, get_list):
    for i in obj_list:
        for j in get_list:
            print(i[j], end='\t')
        print('\n', end='')

ec2_c = boto3.client("ec2")
list_sg = ec2_c.describe_security_groups()['SecurityGroups']

want_list = ["GroupId", "VpcId","GroupName"]
get_list_key(list_sg, want_list)

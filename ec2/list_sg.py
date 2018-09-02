#!/home/ec2-user/.pyenv/shims/python
import boto3
ec2_c = boto3.client("ec2")

list_sg = ec2_c.describe_security_groups()['SecurityGroups']

#for i in list_sg:
#    group_id = i['GroupId']
#    vpc_id = i['VpcId']
#    group_name = i['GroupName']
#    print(group_id, vpc_id, group_name, sep='\t')
#



def get_list_key(list, key):
    for i in list:
        print (i[key])

    

want_list = ["GroupId", "VpcId","GroupName"]

for k in want_list:
    get_list_key(list_sg, k)


#list,key


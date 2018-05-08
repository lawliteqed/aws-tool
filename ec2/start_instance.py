import boto3
r_ec2 = boto3.resource('ec2')

responce = cli_ec2.describe_instances()
print (responce)
AMI_ID = "ami-8fbab2f3"


ec2 = boto3.session.Session.client('ec2')
ec2.

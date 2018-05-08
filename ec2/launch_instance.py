import boto3
ec2_r = boto3.resource('ec2')




#ec2_r.create_instances(
#    MaxCount=1,
#    MinCount=1,
#    ImageId='ami-28ddc154',
#    InstanceType='t2.micro',
#    SecurityGroupIds=[
#        'sg-8b3a32f2'
#    ],
#    SubnetId='subnet-109fbf59',
#    DryRun=True,
#    TagSpecifications=[
#        {
#            'ResourceType': 'instance',
#            'Tags':[
#                {
#                    'Key': 'Name',
#                    'Value': 'sakai-test'
#                }
#            ]
#        }
#    ]
#)

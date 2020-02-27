#!/home/ec2-user/.pyenv/shims/python
import sys
import boto3
import json
import logging
import uuid
logging.basicConfig(level=logging.INFO)


ec2_r = boto3.resource('ec2')

def create_instances(name_tag):
    try:
        ec2_r.create_instances(

            MaxCount          = 1,
            MinCount          = 1,
            DryRun            = False,
            ImageId           = 'ami-084f057267119f805',
            KeyName           = 'sakai-key',
            SubnetId          = 'subnet-109fbf59',
            InstanceType      = 't3.micro',
            SecurityGroupIds  = ['sg-8b3a32f2'],
            TagSpecifications = [
                {
                    'ResourceType': 'instance',
                    'Tags':[
                        {'Key':'Name', 'Value':name_tag}
                    ]
                }
            ]

        )

        logging.info('complete create instance [' + name_tag + ']')
    except Exception as e:
        raise e


if __name__ == '__main__':

    with open('./ec2.json', 'r') as f:
        inst_info = json.load(f)
    print(inst_info)
    # ec2_r.create_instances(**inst_info)

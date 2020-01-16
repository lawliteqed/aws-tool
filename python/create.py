import sys
import boto3
import logging
import uuid
logging.basicConfig(level=logging.INFO)


ec2_r = boto3.resource('ec2')

def insts(name_tag):
    try:
        ec2_r.create_instances(
            MaxCount          = 1,
            MinCount          = 1,
            DryRun            = False,
            ImageId           = 'ami-e99f4896',
            KeyName           = 'sakai-key',
            SubnetId          = 'subnet-109fbf59',
            InstanceType      = 't2.micro',
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

def listes(**hoge_list):
    for i in hoge_list:
        print(i)

if __name__ == '__main__':
    # for i in range(int(sys.argv[1])):
    #     create_instances(str(uuid.uuid4()))
        # print("a")
    listes(['huga', 'hoge'])

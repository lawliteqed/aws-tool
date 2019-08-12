#!/home/ec2-user/.pyenv/shims/python
import sys
import yaml
import boto3


def usage():
    print("usage: " + __file__ + " config.yaml"  )

def read_yaml(read_file):
    f = open(read_file, 'r')
    read_data = yaml.load(f)
    f.close()
    return read_data

def create_instances(r):
    ec2_r = boto3.resource('ec2')

    try:
        ec2_r.create_instances(
            MaxCount=1,
            MinCount=1,
            DryRun=False,
            ImageId = r['image_id'],
            KeyName = r['key_name'],
            SubnetId = r['subnet_id'],
            InstanceType = r['type'],
            SecurityGroupIds = r['sg_ids'],
            TagSpecifications = [
                {
                    'ResourceType': 'instance',
                    'Tags':r['tags']
                }
            ]
        )
        print("[INFO] instance create successful ")
    except:
        print("[ERROR] instance create failed")


if __name__ == '__main__':

    if (len(sys.argv) -1) == 1:
        f = open(sys.argv[1], 'r')
        inst_config = yaml.load(f)
        f.close()
    else:
        usage()

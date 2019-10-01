import boto3
import json

ssm_c = boto3.client('ssm')
a = ssm_c.list_command_invocations(MaxResults=10)

def send_command(iid, doc_name):
    ssm_c.send_command(
        InstanceIds=[
            iid
        ],
        DocumentName=doc_name,
        DocumentVersion='1',
        TimeoutSeconds=300,
        Parameters={
            'commands': [
                'echo "hello world"'
            ]
        }
    )

if __name__ == '__main__':

    for i in a['CommandInvocations']:
        print(
            '{InstanceName:10}'
            '{StatusDetails:10}'
            '{DocumentName:17}'.format(**i)
        )

    print(ssm_c.send_command)


    # send_command('i-0651e0df9ec67345b', 'AWS-RunShellScript')

# {'CommandId': '47d966c4-d718-41d8-9e9f-4f35e44b87ef', 'InstanceId': 'i-0651e0df9ec67345b', 'InstanceName': 'lin2', 'Comment': '', 'DocumentName': 'AWS-ApplyAnsiblePlaybooks', 'DocumentVersion': '1', 'RequestedDateTime': datetime.datetime(2019, 10, 1, 15, 21, 26, 380000, tzinfo=tzlocal()), 'Status': 'Failed', 'StatusDetails': 'Failed', 'StandardOutputUrl': '', 'StandardErrorUrl': '', 'CommandPlugins': [], 'ServiceRole': '', 'NotificationConfig': {'NotificationArn': '', 'NotificationEvents': [], 'NotificationType': ''}, 'CloudWatchOutputConfig': {'CloudWatchLogGroupName': '', 'CloudWatchOutputEnabled': False}}

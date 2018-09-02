import boto3
from boto3.session import Session
import json
 
# 異なるAWSアカウント/ロールのクレデンシャル取得を実行する
def sts_assume_role(account_id,role_name):
    role_arn = "arn:aws:iam::" + account_id + ":role/" + role_name
    session_name = "foobar"
    region = "ap-northeast-1"
 
    client = boto3.client('sts')
 
    # AssumeRoleで一時クレデンシャルを取得
    response = client.assume_role(
        RoleArn=role_arn,
        RoleSessionName=session_name
    )
 
    session = Session(
        aws_access_key_id=response['Credentials']['AccessKeyId'],
        aws_secret_access_key=response['Credentials']['SecretAccessKey'],
        aws_session_token=response['Credentials']['SessionToken'],
        region_name=region
    )
 
    return session
 
def lambda_handler(event,context):
    account_id = ""
    role_name = ""
 
    # イベントで指定されたAWSアカウント/ロールのクレデンシャルを取得
    session = sts_assume_role(account_id,role_name)
 
    sts = session.client('sts')
 
    # 取得したクレデンシャルを使って処理を実行
    
    r_ddb = session.resource('dynamodb')
    c_ddb = session.client('dynamodb')
    
    list_tables = c_ddb.list_tables()
    
    return list_tables

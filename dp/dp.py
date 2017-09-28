#coding: UTF-8

import yaml
import sys
import boto3
dp_c = boto3.client('datapipeline')

import ast


#read config file
try:
    config = yaml.load(file("/home/ec2-user/aws-tool/dp/conf/input.yml", 'r'))
except Exception, e:
    sys.stderr.write("Error")
    sys.exit(1)

#get param
try:
    dp_name = config['dp_name']
    dp_id = config['dp_id']
    ami = config['ami']
    instanceType = config['instanceType']
    pipelineLogUri = config['pipelineLogUri']
    myShellCmd = config['myShellCmd']
    myS3OutputLoc = config['myS3OutputLoc']
    myS3InputLoc = config['myS3InputLoc']
    profile = config["profile"]
except Exception, e:
    sys.stderr.write("Error")
    sys.exit(1)




#responce = dp_c.get_pipeline_definition(
#    pipelineId=dp_id,
#    version='latest'
#)
#
#print responce

f = open('output.dict')
before_dp_str = f.read()
f.close()

#辞書型に変換
bp_dict = ast.literal_eval(before_dp_str)

keys = bp_dict.keys()


def update_parameterValues():
    pv_list[0]["stringValue"] = myShellCmd
    pv_list[1]["stringValue"] = myS3InputLoc
    pv_list[2]["stringValue"] = myS3OutputLoc
    print "hoge"




#parameterValuesのリストを取得



#for k in range(len(keys)):
#    i = keys[k]
#    print i
#    if i in {"parameterValues"}:
#        pv_list = bp_dict[i]
#        print pv_list
#        update_parameterValues

pv_list = bp_dict["pipelineObjects"]

for i in range(len(pv_list)):
    k = pv_list[i]
    print k.keys()

#update_parameterValues()

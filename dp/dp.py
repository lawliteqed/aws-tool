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

#sample
def update_parameterValues():
    pv_list = bp_dict["pipelineObjects"]
    pv_list[0]["stringValue"] = myShellCmd
    pv_list[1]["stringValue"] = myS3InputLoc
    pv_list[2]["stringValue"] = myS3OutputLoc
 
def update_pipelineobjects():
    if id_name == "S3OutputLocation":
        print "hoge"

##listから、key=valueのdictを抜き出す
def getValueFromDictInList(l, k, v):
    for i in range(len(l)):
        o = l[i][k]
        if o == v:
            return l[i]


pv_list = bp_dict["pipelineObjects"]


getValueFromDictInList(bp_dict["parameterValues"], "id", "myS3OutputLoc")["stringValue"] = myS3OutputLoc
getValueFromDictInList(bp_dict["parameterValues"], "id", "myS3InputLoc")["stringValue"] = myS3InputLoc
getValueFromDictInList(bp_dict["parameterValues"], "id", "myShellCmd")["stringValue"] = myShellCmd




#schedule変更
# bp_dict["pipelineObjects"][0]
scheduleList = getValueFromDictInList(bp_dict["pipelineObjects"], "id", "DefaultSchedule")["fields"]
getValueFromDictInList(scheduleList, "key", "period")["stringValue"] = "2 Hour"
getValueFromDictInList(scheduleList, "key", "startDateTime")["stringValue"] = "2017-10-04T06:00:00"

# bp_dict["pipelineObjects"][1]
getValueFromDictInList(bp_dict["pipelineObjects"], "id", "S3OutputLocation")["name"] = "hogege"


# bp_dict["pipelineObjects"][2]
EC2resourceList = getValueFromDictInList(bp_dict["pipelineObjects"], "id", "EC2ResourceObj")["fields"]
getValueFromDictInList(EC2resourceList, "key", "subnetId")["stringValue"] = "hogenet"
getValueFromDictInList(EC2resourceList, "key", "imageId")["stringValue"]
getValueFromDictInList(EC2resourceList, "key", "securityGroupIds")["stringValue"]
getValueFromDictInList(EC2resourceList, "key", "instanceType")["stringValue"]
getValueFromDictInList(EC2resourceList, "key", "terminateAfter")["stringValue"]





#bp_dict.keys()
#u'parameterValues',
#u'pipelineObjects',
#'ResponseMetadata',
#u'parameterObjects']




#for i in range(len(pv_list)):
#    k = pv_list[i]
#    print k.keys()

#update_parameterValues()


#sample

#for i in keys:
#    if i == "parameterValues":
#        pv_list = bp_dict[i]
#        update_parameterValues()
#        print "hoge"
#    elif i == "pipelineObjects":
#        pv_list = bp_dict[i]
#        print "huga"
#    else:
#        print "end"

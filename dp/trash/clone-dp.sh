PROFILE=studies

ORG_NAME=$2
NEW_NAME=$3
#NEW_ID=""
NEW_JSON=conf/$3.json


function usage()
{
   echo "usage:  $0 <profile> <original-dp-name> <new-dp-name>"
}

#$1に与えられたDPの存在チェック
function dp_check()
{
   local check=$1
   if [ "$check" = "" ]; then
      echo "pipeline $1 does not exsits"
      exit
   else 
      return 0
   fi
}


function get_pipeline_id(){
  aws --profile ${PROFILE} datapipeline list-pipelines \
      --query "pipelineIdList[?name==\`$1\`].id" \
      --output text
  echo $?
}

get_pipeline_id $ORG_NAME
#ORG_ID=`get_pipeline_id $ORG_NAME`


#echo $ORG_ID

#echo ${ret}

#if [ $# -eq 3 ]; then
#   echo "ok"
#else
#   usage
#   exit 1
#fi
#
#ORG_ID=$(aws --profile ${PROFILE} datapipeline list-pipelines --query "pipelineIdList[?name==\`$ORG_NAME\`].id" --output text)
#

#
#
#aws --profile ${PROFILE} datapipeline get-pipeline-definition --pipeline-id $ORG_ID > $NEW_JSON
#
#
#aws --profile ${PROFILE} datapipeline create-pipeline --name ${NEW_NAME} --unique-id hojoji
#
##fixme
##すでに同名のpipelineが存在するとエラー。コピー先のpipelineがひとつであることを確認
##同名のpipeline作成はあまりないので問題無いかと。
#NEW_ID=$(aws --profile ${PROFILE} datapipeline list-pipelines --query "pipelineIdList[?name==\`$NEW_NAME\`].id" --output text)
#
##dpで起動しているEC2インスタンスを区別するためタグ付け
#aws --profile ${PROFILE} datapipeline add-tags --pipeline-id ${NEW_ID} --tags key=datapipeline,value=${NEW_NAME}
#
#
#aws --profile ${PROFILE} datapipeline put-pipeline-definition --pipeline-id ${NEW_ID} --pipeline-definition file://${NEW_JSON}

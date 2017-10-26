PROFILE=$1

ORG_DP_NAME=$2
ORG_DP_ID=$(aws --profile ${PROFILE} datapipeline list-pipelines --query "pipelineIdList[?name==\`$ORG_DP_NAME\`].id" --output text)
NEW_DP_NAME=$3
NEW_DP_ID=""
NEW_DP_JSON=conf/$3.json

if [ $# -eq 3 ]; then
   echo "ok"
else
   usage
   exit 1
fi

function usage ()
{
   echo "usage:  $0 <profile> <original-dp-name> <new-dp-name>"
}

#$1に与えられたDPの存在チェック

function dp_check()
{
   local check=$(aws --profile ${PROFILE} datapipeline list-pipelines  --query "pipelineIdList[?name==\`$1\`]" --output text)
   if [ "$check" = "" ]; then
      echo "pipeline $1 does not exsits"
      exit
   else 
      return 0
   fi
}



aws --profile ${PROFILE} datapipeline get-pipeline-definition --pipeline-id $ORG_DP_ID > $NEW_DP_JSON


aws --profile ${PROFILE} datapipeline create-pipeline --name ${NEW_DP_NAME} --unique-id hojoji

#fixme
#すでに同名のpipelineが存在するとエラー。コピー先のpipelineがひとつであることを確認
#同名のpipeline作成はあまりないので問題無いかと。
NEW_DP_ID=$(aws --profile ${PROFILE} datapipeline list-pipelines --query "pipelineIdList[?name==\`$NEW_DP_NAME\`].id" --output text)

#dpで起動しているEC2インスタンスを区別するためタグ付け
aws --profile ${PROFILE} datapipeline add-tags --pipeline-id ${NEW_DP_ID} --tags key=datapipeline,value=${NEW_DP_NAME}


aws --profile ${PROFILE} datapipeline put-pipeline-definition --pipeline-id ${NEW_DP_ID} --pipeline-definition file://${NEW_DP_JSON}

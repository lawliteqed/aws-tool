PROFILE=$1

ORG_DP_NAME=$2
ORG_DP_ID=$(aws --profile ${PROFILE} datapipeline list-pipelines --query "pipelineIdList[?name==\`$ORG_DP_NAME\`].id" --output text)
NEW_DP_NAME=$3


function usage ()
{
   echo "usage:  $0 <profile> <original-dp-name> <new-dp-name>"
}

#引数に与えられたDPの存在チェック
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



function get_dp_difenition()
{
   aws --profile ${PROFILE} datapipeline get-pipeline-definition --pipeline-id $ORG_DP_ID > conf/${NEW_DP_NAME}.json
   echo "hoge"
}


#dp_check $ORG_DP_NAME
get_dp_difenition

if [ $# -eq 3 ]; then
   echo "ok"
   exit 0
else
   usage
   exit 1
fi

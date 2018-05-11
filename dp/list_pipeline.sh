#/bin/sh
PROFILE=$1

function usage (){
   echo "usage: $0 <profile>"
}

function check_env() {
   if [ ` echo $1 | grep '\-stg' ` ] ; then
      echo "STAGING"
   else
      echo "PRODUCTION"
   fi
}

function get_pipeline_name(){
   local _id=$1
   aws --profile $PROFILE datapipeline describe-pipelines \
    --pipeline-ids $_id | jq -r '.pipelineDescriptionList[].name'
}

function get_status() {
   local _id=$1
   aws --profile $PROFILE datapipeline describe-pipelines \
   --pipeline-ids $_id \
   | jq -r '.pipelineDescriptionList[].fields[] | select(.key == "@pipelineState") | .stringValue '
}

function get_ami_id() {
   local _id=$1
   local _status=$2
   if [ $_status = 'SCHEDULED' ] ; then
      aws --profile $PROFILE datapipeline get-pipeline-definition --pipeline-version active \
         --pipeline-id $_id --query "objects[*].imageId" | jq -r '.[]'
   else
      aws --profile $PROFILE datapipeline get-pipeline-definition --pipeline-version latest \
         --pipeline-id $_id --query "objects[*].imageId" | jq -r '.[]'
   fi
}

function get_proc() {
   local _status=$1
   if [ $_status = 'SCHEDULED' ] ; then
      echo "activate"
   else
      echo "save"
   fi
}

if [ $# -ne 1 ]; then
   usage
   exit 2
fi

for pipeline_id in  `aws --profile $PROFILE datapipeline list-pipelines | jq -r '.pipelineIdList[].id'`
   do
      pipeline_name=`get_pipeline_name $pipeline_id`
      pipeline_status=`get_status $pipeline_id`
      env=`check_env $pipeline_name`
      ami_id=`get_ami_id $pipeline_id $pipeline_status`
      proc=`get_proc $pipeline_status`

      echo $pipeline_id,$pipeline_name,$env,$ami_id,,$pipeline_status,$proc
   done

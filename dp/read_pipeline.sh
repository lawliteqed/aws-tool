#/bin/sh

PROFILE=$1
PIPELINEID=$2
ARGUMENT=2

function usage() {
  echo "usage : $0 <profile> <pipeline-id>"
}

function read_pipeline() {
  local _id=$1
  local _output_file=$2
  aws --profile $PROFILE datapipeline get-pipeline-definition \
      --pipeline-id $_id > $_output_file
}

function get_pipeline_name(){
   local _id=$1
   aws --profile $PROFILE datapipeline describe-pipelines \
       --pipeline-ids $_id | jq -r '.pipelineDescriptionList[].name'
}

pipeline_name=`get_pipeline_name $PIPELINEID`
output_file=$pipeline_name.json

#引数チェック
if [ $# -ne $ARGUMENT ]; then
  usage
  exit 2
fi

#出力先ファイルが存在する場合は処理終了
if [ -f $output_file ]; then
  echo "$output_file is exists!  It suspends processing."
  exit 2
fi

#実行
read_pipeline $PIPELINEID $output_file

#実行成否の判断
if [ $? = 0 ]; then
  echo "success"
  exit 0
else
  echo "get $pipeline_name definition failed"
  exit 2
fi

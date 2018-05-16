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

function file_exists_check() {
  local _file=$1
  #ファイルが存在したら処理を終了。
  if [ -f $_file ]; then
    echo "$1 is exists!  It suspends processing."
    exit 2
  fi
}

#引数チェック
if [ $# -ne $ARGUMENT ]; then
   usage
   exit 2
fi

##todo
#エラー処理(awsコマンドが失敗した場合)
#ファイル存在チェックのステータスによる分岐

#ファイル名取得
#pipeline_name=`get_pipeline_name $PIPELINEID`
#
#output_file=$pipeline_name.json
#
##出力ファイル存在チェック
#file_exists_check $output_file
#
#read_pipeline $PIPELINEID $output_file

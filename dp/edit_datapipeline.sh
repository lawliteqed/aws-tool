#/bin/sh

PROFILE=$1
PIPELINEID="df-07789541GILC12XXMID5"
FILE="dp.json"

function usage() {
  echo "usage : $0 -p <profile> -r <pipeline-id>                #<pipeline-name>.jsonにpipeline情報を出力する"
  echo "        $0 -p <profile> -w <pipeline-id> -f <json-file> #指定したjsonファイルの情報をpipelineに反映する"
}

function read_pipeline() {
  local _id=$1
  local _output_file=$2
  aws --profile $PROFILE datapipeline get-pipeline-definition \
      --pipeline-id $_id > $_output_file
}

function write_pipeline() {
  local _id=$1
  local _input_file=$2
  aws --profile $PROFILE datapipeline put-pipeline-definition \
      --pipeline-id $_id \
      --pipeline-definition file://$_input_file
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
    echo "$1 is exists!"
    echo "It suspends processing"
    exit 2
  fi
}


output_file=`get_pipeline_name $PIPELINEID`.json
echo $output_file

read_pipeline $PIPELINEID $output_file

#OPTIND=1
#while getopts ":p:r:w:f" OPT
#do
#  case $OPT in
#  p)
#    PROFILE="${OPTARG}" ;;
#  r)
#    READ="${OPTARG}" ;;
#  w)
#    WRITE="${OPTARG}" ;;
#  f)
#    JSONFILE="${OPTARG}" ;;
#  :|\?)
#    usage
#    exit 2 ;;
#  esac
#done

#read_pipeline_defintion
#write_pipeline_defintion

#if [ "${PROFILE}" ] && [ "${READ}" ]; then
#  read_pipeline_defintion
#elif [ "${PROFILE}" ] && [ "${WRITE}" ] && [ "${JSONFILE}"]; then
#  write_pipeline_defintion
#fi

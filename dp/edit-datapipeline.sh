#/bin/sh

usage() {
  echo "usage : $0 -p <profile> -r <pipeline-id>                #jsonにpipeline情報を出力する"
  echo "        $0 -p <profile> -w <pipeline-id> -f <json-file> #jsonの情報をpipelineに反映する"
}


OPTIND=1
while getopts ":p:r:w:f" OPT
do
  case $OPT in
  p)
    PROFILE="${OPTARG}" ;;
  r)
    READ="${OPTARG}" ;;
  w)
    WRITE="${OPTARG}" ;;
  f)
    JSONFILE="${OPTARG}" ;;
  :|\?)
    usage
    exit 2 ;;
  esac
done

read_pipeline_defintion() {
  ID=$READ
  aws --profile $PROFILE \
  datapipeline get-pipeline-definition \
  --pipeline-id $ID
}

write_pipeline_defintion() {
  ID=$WRITE
  aws --profile $PROFILE \
  datapipeline put-pipeline-definition \
  --pipeline-id $ID \
  --pipeline-definition file://${JSONFILE}
}

#read_pipeline_defintion
#write_pipeline_defintion


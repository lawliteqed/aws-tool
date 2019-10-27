#!/bin/bash

#const
FILE=`basename $0`
DUMMY_YAML="/home/ec2-user/repo/coe_tool/cfn/dummy.yaml"

#function
usage() {
cat << EOT
Usage:
  List tables
    ${FILE} -p profile -l
  Create new table
    ${FILE} -p profile -c -f schema.json
  Put new items
    ${FILE} -p profile -w -f item_ope.json
  Delete table
    ${FILE} -p profile -d -t table_name
EOT
  exit 1
}

function list_tables(){
  aws dynamodb list-tables \
    --profile ${1} \
    --query 'TableNames[]' --output text
  return 0;
}

function delete_table(){
  aws dynamodb delete-table \
    --profile ${1} \
    --table-name ${2}
  return 0;
}

function create_table(){
  aws dynamodb create-table \
    --profile ${1} \
    --cli-input-json file://${2}
  return 0;
}

function write_item(){
  aws dynamodb batch-write-item \
    --profile ${1} \
    --request-items file://${2}
  return 0;
}

#getopts
while getopts p:cldwf:t:h OPT
do
  case $OPT in
    "p" ) FLG_P="TRUE" ; PROFILE="$OPTARG" ;;
    "c" ) FLG_C="TRUE" ;;
    "l" ) FLG_L="TRUE" ;;
    "d" ) FLG_D="TRUE" ;;
    "w" ) FLG_W="TRUE" ;;
    "f" ) FLG_F="TRUE" ; FILE="$OPTARG" ;;
    "t" ) FLG_T="TRUE" ; TABLE="$OPTARG" ;;
    "h" ) usage ;;
      * ) usage ;;
  esac
done

#opts-check
[ "${FLG_P}" != "TRUE" ] && usage

if [ "${FLG_C}" == "TRUE" -a "${FLG_F}" == "TRUE" ]; then
  create_table ${PROFILE} ${FILE}
elif [ "${FLG_W}" == "TRUE" -a "${FLG_F}" == "TRUE" ]; then
  write_item ${PROFILE} ${FILE}
elif [ "${FLG_L}" == "TRUE" ]; then
  list_tables ${PROFILE}
elif [ "${FLG_D}" == "TRUE" -a "${FLG_T}" == "TRUE" ]; then
  delete_table ${PROFILE} ${TABLE}
else
  usage
fi

exit 0

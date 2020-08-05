#!/bin/bash
#const
FILE=`basename $0`
DUMMY_YAML="./XX.dummy.yaml"
STACK_STATUS="CREATE_IN_PROGRESS CREATE_FAILED CREATE_COMPLETE ROLLBACK_IN_PROGRESS ROLLBACK_FAILED ROLLBACK_COMPLETE DELETE_IN_PROGRESS DELETE_FAILED UPDATE_IN_PROGRESS UPDATE_COMPLETE_CLEANUP_IN_PROGRESS UPDATE_COMPLETE UPDATE_ROLLBACK_IN_PROGRESS UPDATE_ROLLBACK_FAILED UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS UPDATE_ROLLBACK_COMPLETE REVIEW_IN_PROGRESS"
#function
usage() {
cat << EOT
Usage:
  List stack
    ${FILE} -p profile -l
  Get stack-yaml
    ${FILE} -p profile -g -s stack-name
  Create new dummy stack
    ${FILE} -p profile -c -s stack-name
  Update stack
    ${FILE} -p profile -u -s stack-name -f yaml-file
EOT
  exit 0
}
function list_stacks(){
  aws cloudformation list-stacks --profile ${1} \
    --stack-status-filter ${STACK_STATUS} --query 'StackSummaries[].[StackStatus,StackName]' \
    --output text | sort
  return 0;
}
function get_stack_template(){
  aws cloudformation get-template \
    --profile ${1} \
    --stack-name ${2} \
    | jq -r '.TemplateBody' \
    | sed -e 's/\\n/\n/g' -e 's/\\r/\r/g' \
    | sed -e 's/\r//g' \
    | sed -e 's/^M//g'
  return 0;
}
function create_stack(){
  aws cloudformation create-stack --profile ${1} \
    --stack-name ${2} --template-body file://${3}
  return 0;
}
function update_stack(){
  aws cloudformation update-stack --profile ${1} \
    --stack-name ${2} --template-body file://${3} --capabilities CAPABILITY_NAMED_IAM
  return 0;
}
#getopts
while getopts p:lgcus:f:h OPT
do
  case $OPT in
    "p" ) FLG_P="TRUE" ; PROFILE="$OPTARG" ;;
    "l" ) FLG_L="TRUE" ;;
    "g" ) FLG_G="TRUE" ;;
    "c" ) FLG_C="TRUE" ;;
    "u" ) FLG_U="TRUE" ;;
    "s" ) FLG_S="TRUE" ; STACK="$OPTARG" ;;
    "f" ) FLG_F="TRUE" ; FILE="$OPTARG" ;;
    "h" ) usage ;;
      * ) usage ;;
  esac
done
#opts-check
[ "${FLG_P}" != "TRUE" ] && usage
# [ "${FLG_S}" != "TRUE" ] && usage
if [ "${FLG_P}" == "TRUE" -a "${FLG_C}" == "TRUE" -a "${FLG_S}" == "TRUE" ]; then
  create_stack ${PROFILE} ${STACK} ${DUMMY_YAML}
elif [ "${FLG_P}" == "TRUE" -a "${FLG_L}" == "TRUE" ]; then
  list_stacks ${PROFILE}
elif [ "${FLG_P}" == "TRUE" -a "${FLG_G}" == "TRUE" -a "${FLG_S}" == "TRUE" ]; then
  get_stack_template ${PROFILE} ${STACK}
elif [ "${FLG_P}" == "TRUE" -a "${FLG_U}" == "TRUE" -a "${FLG_S}" == "TRUE" -a "${FLG_F}" == "TRUE" ]; then
  update_stack ${PROFILE} ${STACK} ${FILE}
else
  usage
fi
exit 0

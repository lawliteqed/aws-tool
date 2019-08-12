#!/bin/sh

#function
usage() {
  echo "Usage: ${FILE} -p profile [-f filter] " 1>&2
  exit 1
}

function list_stacks(){
  aws cloudformation list-stacks \
    --profile ${1} \
    --stack-status-filter ${STACK_STATUS} \
    --query 'StackSummaries[].[StackStatus,StackName]' \
    --output text | sort
  return 0;
}

#getopts
while getopts p:f:h OPT
do
  case $OPT in
    "p" ) FLG_P="TRUE" ; PROFILE="$OPTARG" ;;
    "f" ) FLG_F="TRUE" ; FILTER="$OPTARG" ;;
    "h" ) usage ;;
      * ) usage ;;
  esac
done

#opts-check
[ "${FLG_P}" != "TRUE" ] && usage

#main
if [ "${FLG_F}" == "TRUE" ]; then
  list_stacks ${PROFILE} | grep ${FILTER}
else
  list_stacks ${PROFILE}
fi

exit 0

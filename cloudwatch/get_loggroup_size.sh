#!/bin/bash
### Thanks -> https://dev.classmethod.jp/cloud/aws/check-cloudwatch-logs-incomigbytes-by-aws-cli/

PROFILE=$1
LOG_GROUP_NAME=$2

### LogGroup単位で前日分からDAYSAGOに指定した日数だけ処理する
DAYSAGO=1
STARTDAY=$((ENDDAY+${DAYSAGO}))
ENDDAY=0
STARTTIME="$(date -u --date "${STARTDAY} days ago" +%Y-%m-%dT00:00:00Z)"
ENDTIME="$(date -u --date "${ENDDAY} days ago" +%Y-%m-%dT00:00:00Z)"

function usage(){
   echo "usage: $0 <profile> <log_group>"
}
 
### LogGroup1日分のIncomingBytesの合計を出力
function get_log_byte(){
  LOG_GROUP=$1
  echo "### LogGroup: ${LOG_GROUP} ###"
  aws --profile ${PROFILE} cloudwatch get-metric-statistics \
    --namespace "AWS/Logs" \
    --dimensions Name=LogGroupName,Value="${LOG_GROUP}" \
    --metric-name "IncomingBytes" \
    --statistics "Sum" \
    --start-time "${STARTTIME}" \
    --end-time "${ENDTIME}" \
    --period 86400 \
    --query "reverse(sort_by(Datapoints,&Timestamp)[?Sum>\`0\`].{Sum:Sum,Timestamp:Timestamp})" \
    --output text
}

if [ $# -eq 2 ]; then
  get_log_byte ${LOG_GROUP_NAME}
  exit 0
else
  usage
   exit 2
fi

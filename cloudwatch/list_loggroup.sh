#!/bin/bash
### AWS認証情報は設定済の前提
### 何日分遡って確認するかを指定
DAYSAGO=1
PROFILE=$1


function usage ()
{
   echo "usage:  $0 <profile>"
}
 
### LogGroupの一覧を取得
LOG_GROUPS=$(aws --profile ${PROFILE} cloudwatch list-metrics \
  --namespace "AWS/Logs" \
  --metric-name "IncomingLogEvents" \
  --query "Metrics[].Dimensions[?Name==\`LogGroupName\`].Value" \
  --output text)
 
### LogGroup単位で前日分からDAYSAGOに指定した日数だけ処理する
for LOG_GROUP in ${LOG_GROUPS}
do
  ENDDAY=0
  STARTDAY=$((ENDDAY+${DAYSAGO}))
 
  STARTTIME="$(date -u --date "${STARTDAY} days ago" +%Y-%m-%dT00:00:00Z)"
  ENDTIME="$(date -u --date "${ENDDAY} days ago" +%Y-%m-%dT00:00:00Z)"
 
  ### LogGroupごとに1日分のIncomingBytesの合計を出力
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
done

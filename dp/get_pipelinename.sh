NAME=$1
ID=`aws --profile studies datapipeline list-pipelines | jq -r '.pipelineIdList[] | select(.name == "'$NAME'") | .id'`

echo $NAME:$ID

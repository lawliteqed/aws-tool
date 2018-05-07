LISTFILE=list

cnt=0
while read line
do
   cnt=`expr $cnt + 1`
   id=`echo $line | cut -d: -f1`
   dpname=`echo $line | cut -d: -f2`
   #READ
   #aws --profile hoge datapipeline get-pipeline-definition --pipeline-id $id > dp/$dpname.json

   #WRITE
   #aws --profile hoge datapipeline put-pipeline-definition --pipeline-id $id --pipeline-definition file://dp/$dpname.json

done < $LISTFILE

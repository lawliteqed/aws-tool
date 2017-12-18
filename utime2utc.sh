UNIXTIME=$1
MAXTIME=`date +%s`

function usage ()
{
   echo "usage:  $0 <unixtime(~$MAXTIME)>"
}


function exchange ()
{
   date --date "@$UNIXTIME" +"%Y/%m/%d %T"
}

#if test $# -eq 1 && test $UNIXTIME -lt $MAXTIME ; then
if test $# -eq 1  ; then
   exchange
   exit 0
else
   usage
   exit 2
fi

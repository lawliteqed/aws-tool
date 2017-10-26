for i in `seq 1 30` ; do time=`date +"%Y/%m/"`; time2=`date +"%Y%m"` ; touch -d $time$i logfile.$time2$i ; done

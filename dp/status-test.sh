#/bin/sh

FILE=test.json

function file_exists_check() {
  local _file=$1
  #ファイルが存在したら処理を終了。
  if [ -f $_file ]; then
    echo "TRUE"
  else
    echo "FALSE"
  fi
}


file_exists=`file_exists_check $FILE`


echo $file_exists

#/bin/sh

FILE=test.json

function file_exists_check() {
  local _file=$1
  #ファイルが存在したら処理を終了。
  if [ -f $_file ]; then
    echo "$1 is exists!  It suspends processing."
    exit 2
  fi
}


file_exists_check $FILE


echo huga

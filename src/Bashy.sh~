#!/bin/bash

ABSOLUTE_PATH=$(cd `dirname "${BASH_SOURCE[0]}"` && pwd)
Bashy (){

case $1 in
install ) python3 $ABSOLUTE_PATH"/Bashy.py" "${@:2}" 
;;
* ) echo "Not a valid command"
esac
cd ~/
}

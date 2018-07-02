#! /bin/bash

DIR=$(pushd $(dirname $BASH_SOURCE{0}) > /dev/null && pwd  && popd > /dev/null)

export SATA_INS=${DIR}/sata/install.py
export SATA_BIN=${DIR}/sata/ape.py


adb_kill_process(){
    if [[ $PROCESS_NAME == "" ]]
    then
        return
    fi
    M_PID=$(adb -s $SERIAL shell ps | grep $PROCESS_NAME | awk '{print $2}')
    if [[ $M_PID != "" ]]
    then
        adb -s $SERIAL shell kill $M_PID
    fi
}

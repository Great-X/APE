#! /bin/bash

DIR=$(pushd $(dirname $BASH_SOURCE{0}) > /dev/null && pwd  && popd > /dev/null)

export TOOL=sata
export PKG=$1

if [[ "x$PKG" == "x" ]]
then
    echo "Please specify an pkg"
fi

source ${DIR}/envsetup.sh

adb -s $SERIAL shell ls /sdcard/
RET=$?
if [[ $RET != 0 ]];
then
    echo "Device $SERIAL may not be online."
    exit
fi

source ${DIR}/pre-testing.sh


# get pkg name and version information.
array=(${PKG//_/ })
PKG=${array[0]}
VERSION=${array[1]}


PROCESS_NAME=com.android.commands.monkey
adb_kill_process
PROCESS_NAME=com.github.uiautomator
adb_kill_process
PROCESS_NAME=com.android.commands.motifcore
adb_kill_process

python $SATA_INS
python $SATA_BIN -p $PKG --running-minutes $TESTING_TIME --ape sata > ${DIR}/cur_logs/${TOOL}-${PKG}.log 2>&1


PROCESS_NAME=com.android.commands.monkey
adb_kill_process
PROCESS_NAME=com.github.uiautomator
adb_kill_process
PROCESS_NAME=com.android.commands.motifcore
adb_kill_process

source ${DIR}/post-testing.sh


grep CRASH ${DIR}/cur_logs/${TOOL}-${PKG}.log
RET=$?
echo "RET=$RET"
SATA_OUTPUT_DIR=sata-${PKG}-ape-sata-running-time-$TESTING_TIME
if [[ $RET == 0 ]]
then
    adb -s $SERIAL pull /sdcard/$SATA_OUTPUT_DIR ${DIR}/
fi
adb -s $SERIAL shell rm -rf /sdcard/$SATA_OUTPUT_DIR ${DIR}

PKG=${PKG}_${VERSION}
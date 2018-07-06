#! /bin/bash

DIR=$(pushd $(dirname $BASH_SOURCE{0}) > /dev/null && pwd  && popd > /dev/null)

## cut timeline
#python ${DIR}/cut-timeline.py ${DIR}/cur_logs

# move logs.
for log in $(ls ${DIR}/cur_logs/*.log)
do
    mv ${log} ${DIR}/all_logs/${log##*/}
done

# remove sate-.*-ape-sata-.*
for d in $(ls -d ${DIR}/cur_logs/*-ape-sata-running-time-60)
do
    rm -rf ${d}
done
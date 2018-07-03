#! /bin/bash

DIR=$(pushd $(dirname $BASH_SOURCE{0}) > /dev/null && pwd  && popd > /dev/null)

# cut timeline
for dir in $(ls ${DIR})
do
    python ${DIR}/cut-timeline.py ${DIR}/${dir}
done
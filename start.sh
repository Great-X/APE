#! /bin/bash

DIR=$(pushd $(dirname $BASH_SOURCE{0}) > /dev/null && pwd  && popd > /dev/null)

export SERIAL_1=${SERIAL_1:-067125a40acc819e}
export SERIAL_2=${SERIAL_2:-09434d61255da52f}


# update packages.txt
python ${DIR}/update_packages.py


bash ${DIR}/crash-detection.sh ${SERIAL_1} packages1.txt &
bash ${DIR}/crash-detection.sh ${SERIAL_2} packages2.txt &
wait

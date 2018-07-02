#! /bin/bash

DIR=$(pushd $(dirname $BASH_SOURCE{0}) > /dev/null && pwd  && popd > /dev/null)

# uninstall apk at last
echo "Uninstall apk"
adb -s $SERIAL uninstall $PKG
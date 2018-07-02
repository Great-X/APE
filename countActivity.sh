#! /bin/bash

aapt d xmltree $1 AndroidManifest.xml | grep "E: activity" | wc -l

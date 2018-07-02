#! /usr/bin/python

import os, sys, traceback, subprocess

DIR=os.path.abspath(os.path.dirname(__file__))

ADB=os.getenv('ADB', 'adb')

APE_ROOT='/data/local/tmp/'



def run_cmd(*args):
    print('Run cmd: ' + (' '.join(*args)))
    subprocess.check_call(*args)


if __name__ == '__main__':
    try:
        SERIAL=os.getenv('SERIAL')
        if SERIAL:
            run_cmd([ADB, '-s', SERIAL, 'push', os.path.join(DIR, 'ape.jar'), APE_ROOT])
        else:
            run_cmd([ADB, '-d', 'push', os.path.join(DIR, 'ape.jar'), APE_ROOT])
    except:
        traceback.print_exc()


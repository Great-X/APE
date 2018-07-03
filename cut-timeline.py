#! /usr/bin/python

import sys, os, traceback, shutil, re



######



'''
[APE] // CRASH: com.sudyapp (pid 18373) (elapsed nanos: 51594460461728)
[APE] // Short Msg: java.lang.NullPointerException
[APE] // Long Msg: java.lang.NullPointerException: Attempt to read from field 'java.lang.String com.sudy.app.model.User.coins_num' on a null object reference
[APE] // Build Label: google/hammerhead/hammerhead:6.0.1/M4B30Z/3437181:user/release-keys
[APE] // Build Changelist: 3437181
[APE] // Build Time: 1478203422000
[APE] // java.lang.RuntimeException: Unable to start activity ComponentInfo{com.sudyapp/com.sudy.app.activities.GetCoinsActivity}: java.lang.NullPointerException: Attempt to read from field 'java.lang.String com.sudy.app.model.User.coins_num' on a null object reference
[APE] // 	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2416)
[APE] // 	at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:2476)
[APE] // 	at android.app.ActivityThread.-wrap11(ActivityThread.java)
[APE] // 	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1344)
[APE] // 	at android.os.Handler.dispatchMessage(Handler.java:102)
[APE] // 	at android.os.Looper.loop(Looper.java:148)
[APE] // 	at android.app.ActivityThread.main(ActivityThread.java:5417)
[APE] // 	at java.lang.reflect.Method.invoke(Native Method)
[APE] // 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
[APE] // 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)
[APE] // Caused by: java.lang.NullPointerException: Attempt to read from field 'java.lang.String com.sudy.app.model.User.coins_num' on a null object reference
[APE] // 	at com.sudy.app.activities.GetCoinsActivity.onCreate(Unknown Source)
[APE] // 	at android.app.Activity.performCreate(Activity.java:6251)
[APE] // 	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1107)
[APE] // 	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2369)
[APE] // 	... 9 more
[APE] // 
'''


APE_TAG= '\[APE] '
CRASH_LINE= '// CRASH: (?P<pkg>[^ ]+) .*\n'
SHORT_MSG_LINE= '// Short Msg: (?P<shortmsg>.*)\n'
LONG_MSG_LINE= '// Long Msg: (?P<longmsg>.*)\n'
BUILD_LABEL_LINE= '// Build Label: (?P<buildlabel>.*)\n'
BUILD_CHANGE_LIST_LINE= '// Build Changelist: (?P<buildchangelist>.*)\n'
BUILD_TIME_LINE= '// Build Time: (?P<buildtime>.*)\n'
TOP_EXP_LINE = '// (?P<topexp>[^:]+)(?P<topfullmsg>: .*)?\n'
STACK_FRAME_LINE = '// 	at .+\n'
CAUSED_BY_LINE = '// (?P<norm>Caused by: (?P<causedexp>[^:]+))(?P<causedfullmsg>: .*)?\n'
MORE_LINE = '// 	... [0-9]+ more\n'
END_LINE = '// \n'


CAUSED_BY_PATTERN = re.compile(CAUSED_BY_LINE)
TOP_EXP_PATTERN = re.compile(TOP_EXP_LINE)

STACK_TRACE_PATTERN = re.compile(
        CRASH_LINE \
        + SHORT_MSG_LINE \
        + LONG_MSG_LINE \
        + BUILD_LABEL_LINE \
        + BUILD_CHANGE_LIST_LINE \
        + BUILD_TIME_LINE \
        + '(?P<trace>('
        + '(' + TOP_EXP_LINE + '|' + CAUSED_BY_LINE + ')?'\
        + '(' + STACK_FRAME_LINE + ')+'\
        + '(' + MORE_LINE + ')?'\
        + ')+)'
        + END_LINE
        , re.MULTILINE)


NORMALIZED_TRACE = True

def grep(log):
    log = log.replace('[APE] ', '').replace('\r', '')
    # print(log)
    # print(re.search(CRASH_LINE, log, re.MULTILINE))
    # print(re.search(SHORT_MSG_LINE, log, re.MULTILINE))
    # print(re.search(LONG_MSG_LINE, log, re.MULTILINE))
    # print(re.search(BUILD_LABEL_LINE, log, re.MULTILINE))
    # print(re.search(BUILD_CHANGE_LIST_LINE, log, re.MULTILINE))
    # print(re.search(BUILD_TIME_LINE, log, re.MULTILINE))
    # print(re.search(TOP_EXP_LINE, log, re.MULTILINE))
    # print(re.search(STACK_FRAME_LINE, log, re.MULTILINE))
    # print(re.search(CAUSED_BY_LINE, log, re.MULTILINE))
    # print(re.search(STACK_FRAME_LINE, log, re.MULTILINE))
    # print(re.search(MORE_LINE, log, re.MULTILINE))
    # print(re.search(END_LINE, log, re.MULTILINE))
    results = []
    for m in STACK_TRACE_PATTERN.finditer(log):
        trace = m.group('trace')
        if NORMALIZED_TRACE:
            trace = CAUSED_BY_PATTERN.sub('\g<norm>\n', trace)
            trace = TOP_EXP_PATTERN.sub('\g<topexp>\n', trace)
            trace = trace.replace('// ', '')
        results.append(trace)

    return results

######


class Slice(object):
    def __init__(self, step, stack_trace):
        self.step = step
        begin_step = step - SLICE_SIZE
        if begin_step < 1:
            begin_step = 1
        self.begin_step = begin_step
        self.stack_trace = stack_trace

SLICE_SIZE = 20

EVENT_LINE = re.compile('new Date\(([0-9]+)\).*id: ([0-9]+),')
START_LINE = re.compile('var startTime = new Date\(([0-9]+)\)')
END_LINE = re.compile('var endTime = new Date\(([0-9]+)\)')

PKG_LINE = re.compile('sata-([^-]+)-ape-sata.*')

# [APE] >>>>>>>> SATA end step [425][38918807171355]
#begin step [654]
LOG_STEP_START_LINE = re.compile('^.*begin step \[([0-9]+)\].*$')

DIR=os.path.dirname(os.path.abspath(__file__))


LOG_TMPL = '''title: {title}

# {title}

[Timeline](./vis-timeline.html)

```
{log}
```

'''

def expand_to(array, size):
    delta = size - len(array)
    if delta > 0:
        array = array + list(range(delta))

    return array

def slice_stdout(log):
    s = []
    all_crashes = set()
    results = []
    with open(log, 'r') as f:
        for line in f:
            m = LOG_STEP_START_LINE.match(line)
            if m:
                step = int(m.group(1))
                log = ''.join(s)
                crashes = grep(log)
                if len(crashes) > 0:
                    for crash in crashes:
                        if crash not in all_crashes:
                            o = Slice(step - 1, crash)
                            results.append(o)
                            all_crashes.add(crash)
                s = []
            s.append(line)

    return results


def makedir(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    return folder


def split(log_dir):
    if log_dir.endswith(os.path.sep):
        base_name = os.path.basename(log_dir.rstrip(os.path.sep))
    else:
        base_name = os.path.basename(log_dir)

    m = PKG_LINE.match(base_name)
    if not m:
        print('Cannot determine package name from log directory: ' + log_dir)
        return

    package = m.group(1)

    stdout_log = os.path.abspath(os.path.join(log_dir, '..', 'logs', 'sata-' + package + '.log'))

    if not os.path.exists(stdout_log):
        print('Cannot determine stdout from log directory: ' + log_dir)
        return


    log_slice = slice_stdout(stdout_log)

    report_dir = makedir(os.path.join(DIR, 'reports', 'report-' + package))

    local_names = []
    for s in log_slice:
        #print(str(s.step))
        #print(s.stack_trace)
        local_name = package + '-' + str(s.step)
        local_names.append('* [{local_name}](./{local_name}/)'.format(local_name=local_name))
        output_dir = makedir(os.path.abspath(os.path.join(report_dir, local_name)))
        output(log_dir, output_dir, package, s)

    with open(os.path.join(report_dir, 'index.md'), 'w') as f:
        f.write('''title: {title}\n# {title}\n{content}'''.format(title=package, content = '\n'.join(local_names)))


def output(log_dir, output_dir, package, s):
    begin_step = s.begin_step
    step = s.step

    print('steps: %d - %d' % (begin_step, step))


    sataTimeline = os.path.join(log_dir, 'sataTimeline.vis.js')
    newTimeline = os.path.join(output_dir, 'sataTimeline.vis.js')


    with open(os.path.join(output_dir, 'index.md'), 'w') as f:
        f.write(LOG_TMPL.format(title=package, log=s.stack_trace))

    shutil.copy(os.path.join(DIR, 'vis-timeline.html'), output_dir)
    shutil.copy(os.path.join(DIR, 'vis.min.css'), output_dir)
    shutil.copy(os.path.join(DIR, 'vis.min.js'), output_dir)

    for i in range(begin_step, step + 1):
        shutil.copy(os.path.join(log_dir, 'step-' + str(i) + '.png'), output_dir)


    begin_time = None
    end_time = None

    with open(sataTimeline) as r, open(newTimeline, 'w') as w:
        for line in r:
            m = EVENT_LINE.search(line)
            if m:
                if end_time:
                    continue

                id_step = int(m.group(2)) + 1 # id starts from 0 while step starts from 1
                if id_step >= begin_step:
                    w.write(line)
                    if begin_time is None:
                        begin_time = m.group(1)

                    if id_step == step:
                        #w.write(line)
                        end_time = m.group(1)

                continue

            m = START_LINE.search(line)
            if m:
                newline = line.replace(m.group(1), begin_time)
                w.write(newline)
                continue


            m = END_LINE.search(line)
            if m:
                newline = line.replace(m.group(1), end_time)
                w.write(newline)
                continue


            w.write(line)


if __name__ == '__main__':
    try:
        split(sys.argv[1])
    except:
        traceback.print_exc()

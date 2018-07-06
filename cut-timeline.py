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
TOP_EXP_LINE = '// (?P<topexp>[^:\s]+)(?P<topfullmsg>: .*)?\n'
STACK_FRAME_LINE = '// 	at .+\n'
CAUSED_BY_LINE = '// (?P<norm>Caused by: (?P<causedexp>[^:]+))(?P<causedfullmsg>: .*)?\n'
MORE_LINE = '// 	... [0-9]+ more\n'
END_LINE = '// \n'


NATIVE_SHORT_MSG_LINE= '// Short Msg: Native crash\n'


CAUSED_BY_PATTERN = re.compile(CAUSED_BY_LINE, re.MULTILINE)
TOP_EXP_PATTERN = re.compile(TOP_EXP_LINE, re.MULTILINE)

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


NATIVE_STACK_TRACE_PATTERN = re.compile(
        CRASH_LINE \
        + NATIVE_SHORT_MSG_LINE \
        + LONG_MSG_LINE \
        + BUILD_LABEL_LINE \
        + BUILD_CHANGE_LIST_LINE \
        + BUILD_TIME_LINE \
        + '(?P<trace>(' \
        + '.+\n' \
        + ')+)' \
        + END_LINE \
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
        pkg = m.group('pkg')
        exp = m.group('shortmsg')
        trace = m.group('trace')
        original_trace = trace
        if NORMALIZED_TRACE:
            trace = CAUSED_BY_PATTERN.sub('\g<norm>\n', trace)
            trace = TOP_EXP_PATTERN.sub('\g<topexp>\n', trace)
            trace = trace.replace('// ', '')
            # print(trace)
        results.append(Crash(pkg, exp, trace, original_trace))


    for m in NATIVE_STACK_TRACE_PATTERN.finditer(log):
        pkg = m.group('pkg')
        exp = 'Native crash'
        trace = m.group('trace')
        original_trace = trace
        if NORMALIZED_TRACE:
            trace = m.group('longmsg')
        results.append(Crash(pkg, exp, trace, original_trace))



    return results

######


class Crash(object):
    def __init__(self, pkg, exp, stack_trace, original_trace):
        self.pkg = pkg
        self.exp = exp
        self.stack_trace = stack_trace
        self.original_trace = original_trace

class Slice(object):
    def __init__(self, step, crash):
        self.step = step
        begin_step = step - SLICE_SIZE
        if begin_step < 1:
            begin_step = 1
        self.begin_step = begin_step
        self.exp = crash.exp
        self.stack_trace = crash.stack_trace
        self.original_trace = crash.original_trace

SLICE_SIZE = 10

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

[Google Play Store](https://play.google.com/store/apps/details?id={title})

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
{log}
```



'''

LOG_TMPL_NO_TIMELINE = '''title: {title}

# {title}

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
                for crash in crashes:
                    if crash.stack_trace not in all_crashes:
                        o = Slice(step - 1, crash)
                        results.append(o)
                        all_crashes.add(crash.stack_trace)
                s = []
            s.append(line)

    return results


def makedir(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    return folder

def rename_if_exists(folder):
    subfix = 1
    while os.path.exists(folder):
        folder = folder + '-' + str(subfix)
        subfix = subfix + 1
    os.makedirs(folder)
    return folder


def split(package, stdout_log, log_dir):
    log_slice = slice_stdout(stdout_log)

    if len(log_slice) == 0:
        return log_slice

    # report_dir = makedir('report-' + package)
    report_dir = makedir(os.path.join(DIR, 'reports', 'report-' + package))

    local_names = []
    for s in log_slice:
        #print(str(s.step))
        #print(s.stack_trace)
        local_name = package + '-' + str(s.step)
        output_dir = rename_if_exists(os.path.abspath(os.path.join(report_dir, local_name)))
        try:
            output(log_dir, output_dir, package, s)
        except:
            traceback.print_exc()
            with open(os.path.join(output_dir, 'index.md'), 'w') as f:
                f.write(LOG_TMPL_NO_TIMELINE.format(title=package, log=s.original_trace))

        local_name = os.path.basename(output_dir)
        local_names.append('* [{local_name}](./{local_name}/)'.format(local_name=local_name))
        s.local_name = local_name

    with open(os.path.join(report_dir, 'index.md'), 'w') as f:
        f.write('''title: {title}\n# {title}\n\n\n[Google Play Store](https://play.google.com/store/apps/details?id={title})\n\n\n{content}'''.format(title=package, content = '\n'.join(local_names)))


    return log_slice

def output(log_dir, output_dir, package, s):
    if not log_dir or not os.path.isdir(log_dir):
        raise RuntimeError('Missing data for package ' + package)

    begin_step = s.begin_step
    step = s.step

    # print('steps: %d - %d' % (begin_step, step))


    sataTimeline = os.path.join(log_dir, 'sataTimeline.vis.js')
    newTimeline = os.path.join(output_dir, 'sataTimeline.vis.js')


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


    with open(os.path.join(output_dir, 'index.md'), 'w') as f:
        f.write(LOG_TMPL.format(title=package, log=s.original_trace))



SATA_LOG_FILE_PATTERN = re.compile('sata-([^-]+)[.]log')

def find_sata_data_dir_for_pkg(data_dir, pkg):
    prefix = 'sata-' + pkg + '-ape-sata-'
    for log_dir in os.listdir(data_dir):
        pkg_data_dir = os.path.join(data_dir, log_dir)
        if not os.path.isdir(pkg_data_dir):
            continue

        if log_dir.startswith(prefix):
            return pkg_data_dir

    data_dir = os.path.join(data_dir, pkg, 'sata-' + pkg)
    if not os.path.exists(data_dir):
        return None
    for log_dir in os.listdir(data_dir):
        pkg_data_dir = os.path.join(data_dir, log_dir)
        if not os.path.isdir(pkg_data_dir):
            continue

        if log_dir.startswith(prefix):
            return pkg_data_dir
    return None

class Counter(object):
    def __init__(self):
        self.counter = dict()
        self.total = 0

    def inc(self, key):
        if key in self.counter:
            self.counter[key] = self.counter[key] + 1
        else:
            self.counter[key] = 1
        self.total = self.total + 1

    def to_markdown_table(self, key_header, val_header):
        max_key_length = len(key_header)
        max_val_length = len(val_header)

        key = 'Total'
        val = self.total
        key_length = len(str(key))
        val_length = len(str(val))
        max_key_length = max_key_length if max_key_length > key_length else key_length
        max_val_length = max_val_length if max_val_length > val_length else val_length

        for key,val in self.counter.iteritems():
            key_length = len(str(key))
            val_length = len(str(val))
            max_key_length = max_key_length if max_key_length > key_length else key_length
            max_val_length = max_val_length if max_val_length > val_length else val_length


        max_key_length = max_key_length + 1 # space
        max_val_length = max_val_length + 1

        line_tpl = '{0: <%d} | {1: >%d}' % (max_key_length, max_val_length)
        lines = []
        lines.append(line_tpl.format(key_header, val_header))
        lines.append(line_tpl.format('-' * max_key_length, '-' * max_val_length))
        lines.append(line_tpl.format('Total', self.total))
        for key,val in sorted(self.counter.iteritems(), key = lambda (k,v): (v,k), reverse=True):
            lines.append(line_tpl.format(key, val))

        return '\n'.join(lines)

def split_directory(data_dirs):
    total_crash = 0
    total_pkg = 0
    total_crashed_pkg = 0
    indexmd_tpl = '''title: Report

# Report

!!! note
    Ape found {total_crash} crashes in {total_crashed_pkg} of {total_pkg} apps in Google Play Store.

## Errors

{table}

## Crash List

{content}



~~~{{.customjs}}
// add Bootstrap css class via jQuery
$('table').addClass('table-responsive').addClass('table').addClass('table-bordered').css('width', '100%')
~~~
'''

    counter = Counter()
    content = []
    for data_dir in data_dirs:
        data_dir = os.path.abspath(data_dir)
        for log in os.listdir(data_dir):
            if not os.path.isfile(os.path.join(data_dir, log)):
                continue
            m = SATA_LOG_FILE_PATTERN.match(log)
            if m:
                # print(log)
                total_pkg = total_pkg + 1
                pkg = m.group(1)
                pkg_data_dir = find_sata_data_dir_for_pkg(data_dir, pkg)
                log_slice = split(pkg, os.path.join(data_dir, log), pkg_data_dir)
                if len(log_slice) == 0:
                    continue
                for s in log_slice:
                    counter.inc(s.exp)
                total_crash = total_crash + len(log_slice)
                total_crashed_pkg = total_crashed_pkg + 1
                content.append('* [{0} ({1})](report-{0})'.format(pkg, len(log_slice)))

    # content = sorted(content)
    # with open('index.md', 'w') as f:
    #     f.write(indexmd_tpl.format(total_crash = total_crash, total_crashed_pkg = total_crashed_pkg, total_pkg = total_pkg, table = counter.to_markdown_table('Error Type', '\\#'), \
    #         content = '\n'.join(content)))

if __name__ == '__main__':
    try:
        split_directory(sys.argv[1:])
    except:
        traceback.print_exc()

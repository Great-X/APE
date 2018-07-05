title: com.amaze.filemanager

# com.amaze.filemanager

[Timeline](./vis-timeline.html)

```
java.lang.RuntimeException
	at android.os.AsyncTask$3.done(AsyncTask.java:309)
	at java.util.concurrent.FutureTask.finishCompletion(FutureTask.java:354)
	at java.util.concurrent.FutureTask.setException(FutureTask.java:223)
	at java.util.concurrent.FutureTask.run(FutureTask.java:242)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1113)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:588)
	at java.lang.Thread.run(Thread.java:818)
Caused by: java.lang.StringIndexOutOfBoundsException
	at java.lang.AbstractStringBuilder.startEndAndLength(AbstractStringBuilder.java:211)
	at java.lang.AbstractStringBuilder.substring(AbstractStringBuilder.java:616)
	at java.lang.StringBuilder.substring(StringBuilder.java)
	at com.amaze.filemanager.filesystem.HFile.getParentName(HFile.java:395)
	at com.amaze.filemanager.utils.MainActivityHelper.isNewDirectoryRecursive(MainActivityHelper.java:675)
	at com.amaze.filemanager.filesystem.Operations$1.doInBackground(Operations.java:98)
	at com.amaze.filemanager.filesystem.Operations$1.doInBackground(Operations.java:91)
	at android.os.AsyncTask$2.call(AsyncTask.java:295)
	at java.util.concurrent.FutureTask.run(FutureTask.java:237)
	... 3 more

```


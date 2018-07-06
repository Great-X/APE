title: de.digisocken.anotherrss

# de.digisocken.anotherrss

[Google Play Store](https://play.google.com/store/apps/details?id=de.digisocken.anotherrss)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.RuntimeException: An error occurred while executing doInBackground()
// 	at android.os.AsyncTask$3.done(AsyncTask.java:309)
// 	at java.util.concurrent.FutureTask.finishCompletion(FutureTask.java:354)
// 	at java.util.concurrent.FutureTask.setException(FutureTask.java:223)
// 	at java.util.concurrent.FutureTask.run(FutureTask.java:242)
// 	at android.os.AsyncTask$SerialExecutor$1.run(AsyncTask.java:234)
// 	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1113)
// 	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:588)
// 	at java.lang.Thread.run(Thread.java:818)
// Caused by: java.lang.NullPointerException: Attempt to invoke interface method 'int android.database.Cursor.getColumnIndex(java.lang.String)' on a null object reference
// 	at de.digisocken.anotherrss.FeedListFragment$ContextTask.doInBackground(FeedListFragment.java:200)
// 	at de.digisocken.anotherrss.FeedListFragment$ContextTask.doInBackground(FeedListFragment.java:191)
// 	at android.os.AsyncTask$2.call(AsyncTask.java:295)
// 	at java.util.concurrent.FutureTask.run(FutureTask.java:237)
// 	... 4 more

```




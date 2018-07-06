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
// Caused by: android.database.StaleDataException: Attempting to access a closed CursorWindow.Most probable cause: cursor is deactivated prior to calling this method.
// 	at android.database.AbstractWindowedCursor.checkPosition(AbstractWindowedCursor.java:139)
// 	at android.database.AbstractWindowedCursor.getString(AbstractWindowedCursor.java:50)
// 	at android.database.CursorWrapper.getString(CursorWrapper.java:137)
// 	at de.digisocken.anotherrss.FeedListFragment$ContextTask.doInBackground(FeedListFragment.java:235)
// 	at de.digisocken.anotherrss.FeedListFragment$ContextTask.doInBackground(FeedListFragment.java:191)
// 	at android.os.AsyncTask$2.call(AsyncTask.java:295)
// 	at java.util.concurrent.FutureTask.run(FutureTask.java:237)
// 	... 4 more

```




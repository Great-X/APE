title: com.nextcloud.android.beta

# com.nextcloud.android.beta

[Timeline](./vis-timeline.html)

```
java.lang.RuntimeException
	at android.os.AsyncTask$3.done(AsyncTask.java:309)
	at java.util.concurrent.FutureTask.finishCompletion(FutureTask.java:354)
	at java.util.concurrent.FutureTask.setException(FutureTask.java:223)
	at java.util.concurrent.FutureTask.run(FutureTask.java:242)
	at android.os.AsyncTask$SerialExecutor$1.run(AsyncTask.java:234)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1113)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:588)
	at java.lang.Thread.run(Thread.java:818)
Caused by: java.lang.IllegalArgumentException
	at com.owncloud.android.lib.common.OwnCloudAccount.<init>(OwnCloudAccount.java:65)
	at com.owncloud.android.ui.activities.data.activities.ActivitiesServiceApiImpl$GetActivityListTask.doInBackground(ActivitiesServiceApiImpl.java:75)
	at com.owncloud.android.ui.activities.data.activities.ActivitiesServiceApiImpl$GetActivityListTask.doInBackground(ActivitiesServiceApiImpl.java:54)
	at android.os.AsyncTask$2.call(AsyncTask.java:295)
	at java.util.concurrent.FutureTask.run(FutureTask.java:237)
	... 4 more

```


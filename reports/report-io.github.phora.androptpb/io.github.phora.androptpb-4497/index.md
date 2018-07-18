title: io.github.phora.androptpb

# io.github.phora.androptpb

[Google Play Store](https://play.google.com/store/apps/details?id=io.github.phora.androptpb)

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
// Caused by: java.lang.ClassCastException: com.android.okhttp.internal.huc.HttpURLConnectionImpl cannot be cast to javax.net.ssl.HttpsURLConnection
// 	at io.github.phora.androptpb.network.NetworkUtils.openConnection(NetworkUtils.java:78)
// 	at io.github.phora.androptpb.activities.MainActivity$ShortenURLTask.doInBackground(MainActivity.java:204)
// 	at io.github.phora.androptpb.activities.MainActivity$ShortenURLTask.doInBackground(MainActivity.java:182)
// 	at android.os.AsyncTask$2.call(AsyncTask.java:295)
// 	at java.util.concurrent.FutureTask.run(FutureTask.java:237)
// 	... 4 more

```




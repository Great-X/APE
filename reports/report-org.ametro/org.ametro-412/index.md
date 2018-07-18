title: org.ametro

# org.ametro

[Google Play Store](https://play.google.com/store/apps/details?id=org.ametro)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String java.lang.Throwable.getMessage()' on a null object reference
// 	at org.ametro.ui.tasks.TaskHelpers.displayFailReason(TaskHelpers.java:14)
// 	at org.ametro.ui.activities.CityList.onMapDownloadingFailed(CityList.java:110)
// 	at org.ametro.ui.tasks.MapInstallerAsyncTask.onCancelled(MapInstallerAsyncTask.java:104)
// 	at org.ametro.ui.tasks.MapInstallerAsyncTask.onCancelled(MapInstallerAsyncTask.java:26)
// 	at android.os.AsyncTask.finish(AsyncTask.java:649)
// 	at android.os.AsyncTask.-wrap1(AsyncTask.java)
// 	at android.os.AsyncTask$InternalHandler.handleMessage(AsyncTask.java:668)
// 	at android.os.Handler.dispatchMessage(Handler.java:102)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)

```




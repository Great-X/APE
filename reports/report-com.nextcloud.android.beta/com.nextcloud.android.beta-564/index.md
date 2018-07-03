title: com.nextcloud.android.beta

# com.nextcloud.android.beta

[Timeline](./vis-timeline.html)

```
java.lang.RuntimeException
	at android.app.ActivityThread.deliverResults(ActivityThread.java:3699)
	at android.app.ActivityThread.handleSendResult(ActivityThread.java:3742)
	at android.app.ActivityThread.-wrap16(ActivityThread.java)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1393)
	at android.os.Handler.dispatchMessage(Handler.java:102)
	at android.os.Looper.loop(Looper.java:148)
	at android.app.ActivityThread.main(ActivityThread.java:5417)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)
Caused by: java.lang.NullPointerException
	at com.owncloud.android.ui.activity.FileDisplayActivity.requestUploadOfFilesFromFileSystem(FileDisplayActivity.java:999)
	at com.owncloud.android.ui.activity.FileDisplayActivity.onActivityResult(FileDisplayActivity.java:962)
	at android.app.Activity.dispatchActivityResult(Activity.java:6456)
	at android.app.ActivityThread.deliverResults(ActivityThread.java:3695)
	... 9 more

```


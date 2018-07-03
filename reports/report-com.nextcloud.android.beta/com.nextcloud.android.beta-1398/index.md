title: com.nextcloud.android.beta

# com.nextcloud.android.beta

[Timeline](./vis-timeline.html)

```
java.lang.RuntimeException
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2416)
	at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:2476)
	at android.app.ActivityThread.-wrap11(ActivityThread.java)
	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1344)
	at android.os.Handler.dispatchMessage(Handler.java:102)
	at android.os.Looper.loop(Looper.java:148)
	at android.app.ActivityThread.main(ActivityThread.java:5417)
	at java.lang.reflect.Method.invoke(Native Method)
	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)
Caused by: java.lang.IllegalArgumentException
	at android.accounts.AccountManager.getUserData(AccountManager.java:360)
	at com.owncloud.android.ui.trashbin.RemoteTrashbinRepository.<init>(RemoteTrashbinRepository.java:62)
	at com.owncloud.android.ui.trashbin.TrashbinActivity.onCreate(TrashbinActivity.java:93)
	at android.app.Activity.performCreate(Activity.java:6251)
	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1107)
	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2369)
	... 9 more

```


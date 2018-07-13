title: com.teamdc.stephendiniz.autoaway

# com.teamdc.stephendiniz.autoaway

[Google Play Store](https://play.google.com/store/apps/details?id=com.teamdc.stephendiniz.autoaway)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.RuntimeException: Unable to stop service com.teamdc.stephendiniz.autoaway.Service_Away@772b7b1: java.lang.IllegalArgumentException: Receiver not registered: null
// 	at android.app.ActivityThread.handleStopService(ActivityThread.java:3059)
// 	at android.app.ActivityThread.-wrap21(ActivityThread.java)
// 	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1447)
// 	at android.os.Handler.dispatchMessage(Handler.java:102)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)
// Caused by: java.lang.IllegalArgumentException: Receiver not registered: null
// 	at android.app.LoadedApk.forgetReceiverDispatcher(LoadedApk.java:780)
// 	at android.app.ContextImpl.unregisterReceiver(ContextImpl.java:1195)
// 	at android.content.ContextWrapper.unregisterReceiver(ContextWrapper.java:576)
// 	at com.teamdc.stephendiniz.autoaway.Service_Away.onDestroy(Service_Away.java:260)
// 	at android.app.ActivityThread.handleStopService(ActivityThread.java:3040)
// 	... 8 more

```




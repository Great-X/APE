title: io.github.phora.aeondroid

# io.github.phora.aeondroid

[Google Play Store](https://play.google.com/store/apps/details?id=io.github.phora.aeondroid)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.RuntimeException: Unable to start service io.github.phora.aeondroid.workers.AeonDroidService@c4c2717 with null: java.lang.NumberFormatException: Invalid double: ""
// 	at android.app.ActivityThread.handleServiceArgs(ActivityThread.java:3027)
// 	at android.app.ActivityThread.-wrap17(ActivityThread.java)
// 	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1442)
// 	at android.os.Handler.dispatchMessage(Handler.java:102)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)
// Caused by: java.lang.NumberFormatException: Invalid double: ""
// 	at java.lang.StringToReal.invalidReal(StringToReal.java:63)
// 	at java.lang.StringToReal.parseDouble(StringToReal.java:267)
// 	at java.lang.Double.parseDouble(Double.java:301)
// 	at java.lang.Double.valueOf(Double.java:338)
// 	at io.github.phora.aeondroid.workers.AeonDroidService.recheckGps(AeonDroidService.java:251)
// 	at io.github.phora.aeondroid.workers.AeonDroidService.onStartCommand(AeonDroidService.java:343)
// 	at android.app.ActivityThread.handleServiceArgs(ActivityThread.java:3010)
// 	... 8 more

```




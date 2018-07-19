title: info.lamatricexiste.network

# info.lamatricexiste.network

[Google Play Store](https://play.google.com/store/apps/details?id=info.lamatricexiste.network)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.RuntimeException: Unable to start activity ComponentInfo{info.lamatricexiste.network/info.lamatricexiste.network.ActivityPortscan}: java.lang.NumberFormatException: Invalid int: ""
// 	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2416)
// 	at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:2476)
// 	at android.app.ActivityThread.-wrap11(ActivityThread.java)
// 	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1344)
// 	at android.os.Handler.dispatchMessage(Handler.java:102)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)
// Caused by: java.lang.NumberFormatException: Invalid int: ""
// 	at java.lang.Integer.invalidInt(Integer.java:138)
// 	at java.lang.Integer.parseInt(Integer.java:358)
// 	at java.lang.Integer.parseInt(Integer.java:334)
// 	at info.lamatricexiste.network.ActivityPortscan.getTimeout(ActivityPortscan.java:592)
// 	at info.lamatricexiste.network.ActivityPortscan.startScan(ActivityPortscan.java:561)
// 	at info.lamatricexiste.network.ActivityPortscan.onCreate(ActivityPortscan.java:192)
// 	at android.app.Activity.performCreate(Activity.java:6251)
// 	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1107)
// 	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2369)
// 	... 9 more

```




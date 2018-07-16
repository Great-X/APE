title: org.glucosio.android

# org.glucosio.android

[Google Play Store](https://play.google.com/store/apps/details?id=org.glucosio.android)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.RuntimeException: Unable to start activity ComponentInfo{org.glucosio.android/org.glucosio.android.activity.ExternalLinkActivity}: java.lang.SecurityException: ConnectivityService: Neither user 10187 nor current process has android.permission.ACCESS_NETWORK_STATE.
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
// Caused by: java.lang.SecurityException: ConnectivityService: Neither user 10187 nor current process has android.permission.ACCESS_NETWORK_STATE.
// 	at android.os.Parcel.readException(Parcel.java:1620)
// 	at android.os.Parcel.readException(Parcel.java:1573)
// 	at android.net.IConnectivityManager$Stub$Proxy.getActiveNetworkInfo(IConnectivityManager.java:1021)
// 	at android.net.ConnectivityManager.getActiveNetworkInfo(ConnectivityManager.java:656)
// 	at vj.a(Unknown Source)
// 	at up.a(Unknown Source)
// 	at org.glucosio.android.activity.ExternalLinkActivity.o(Unknown Source)
// 	at org.glucosio.android.activity.ExternalLinkActivity.m(Unknown Source)
// 	at org.glucosio.android.activity.ExternalLinkActivity.onCreate(Unknown Source)
// 	at android.app.Activity.performCreate(Activity.java:6251)
// 	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1107)
// 	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2369)
// 	... 9 more

```




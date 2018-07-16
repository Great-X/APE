title: org.pulpdust.lesserpad

# org.pulpdust.lesserpad

[Google Play Store](https://play.google.com/store/apps/details?id=org.pulpdust.lesserpad)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.RuntimeException: Unable to start activity ComponentInfo{org.pulpdust.lesserpad/org.pulpdust.lesserpad.LesserPadActivity}: java.lang.NullPointerException: Attempt to get length of null array
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
// Caused by: java.lang.NullPointerException: Attempt to get length of null array
// 	at java.util.ComparableTimSort.sort(ComparableTimSort.java:142)
// 	at java.util.Arrays.sort(Arrays.java:1957)
// 	at org.pulpdust.lesserpad.libLesserPad.listDir(libLesserPad.java:52)
// 	at org.pulpdust.lesserpad.LesserPadActivity.onCreate(LesserPadActivity.java:305)
// 	at android.app.Activity.performCreate(Activity.java:6251)
// 	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1107)
// 	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2369)
// 	... 9 more

```




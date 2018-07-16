title: org.liberty.android.fantastischmemo

# org.liberty.android.fantastischmemo

[Google Play Store](https://play.google.com/store/apps/details?id=org.liberty.android.fantastischmemo)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.RuntimeException: Unable to start activity ComponentInfo{org.liberty.android.fantastischmemo/org.liberty.android.fantastischmemo.ui.StudyActivity}: java.lang.NullPointerException: Attempt to invoke virtual method 'int java.lang.String.compareTo(java.lang.String)' on a null object reference
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
// Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'int java.lang.String.compareTo(java.lang.String)' on a null object reference
// 	at org.liberty.android.fantastischmemo.common.AnyMemoDBOpenHelperManager$1.compare(AnyMemoDBOpenHelperManager.java:30)
// 	at org.liberty.android.fantastischmemo.common.AnyMemoDBOpenHelperManager$1.compare(AnyMemoDBOpenHelperManager.java:24)
// 	at java.util.TreeMap.find(TreeMap.java:279)
// 	at java.util.TreeMap.findByObject(TreeMap.java:351)
// 	at java.util.TreeMap.containsKey(TreeMap.java:182)
// 	at java.util.Collections$SynchronizedMap.containsKey(Collections.java:682)
// 	at org.liberty.android.fantastischmemo.common.AnyMemoDBOpenHelperManager.getHelper(AnyMemoDBOpenHelperManager.java:54)
// 	at org.liberty.android.fantastischmemo.ui.QACardActivity.startInit(QACardActivity.java:150)
// 	at org.liberty.android.fantastischmemo.ui.StudyActivity.onCreate(StudyActivity.java:119)
// 	at android.app.Activity.performCreate(Activity.java:6251)
// 	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1107)
// 	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2369)
// 	... 9 more

```




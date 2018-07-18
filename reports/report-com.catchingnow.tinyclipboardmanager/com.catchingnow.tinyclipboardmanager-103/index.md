title: com.catchingnow.tinyclipboardmanager

# com.catchingnow.tinyclipboardmanager

[Google Play Store](https://play.google.com/store/apps/details?id=com.catchingnow.tinyclipboardmanager)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.RuntimeException: Unable to start activity ComponentInfo{com.catchingnow.tinyclipboardmanager/com.catchingnow.tinyclipboardmanager.ActivityBackupNew}: java.lang.ClassCastException: android.widget.HorizontalScrollView$SavedState cannot be cast to android.widget.ScrollView$SavedState
// 	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2416)
// 	at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:2476)
// 	at android.app.ActivityThread.handleRelaunchActivity(ActivityThread.java:4077)
// 	at android.app.ActivityThread.-wrap15(ActivityThread.java)
// 	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1350)
// 	at android.os.Handler.dispatchMessage(Handler.java:102)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)
// Caused by: java.lang.ClassCastException: android.widget.HorizontalScrollView$SavedState cannot be cast to android.widget.ScrollView$SavedState
// 	at android.widget.ScrollView.onRestoreInstanceState(ScrollView.java:1807)
// 	at android.view.View.dispatchRestoreInstanceState(View.java:14752)
// 	at android.view.ViewGroup.dispatchRestoreInstanceState(ViewGroup.java:3121)
// 	at android.view.ViewGroup.dispatchRestoreInstanceState(ViewGroup.java:3127)
// 	at android.view.ViewGroup.dispatchRestoreInstanceState(ViewGroup.java:3127)
// 	at android.view.ViewGroup.dispatchRestoreInstanceState(ViewGroup.java:3127)
// 	at android.view.ViewGroup.dispatchRestoreInstanceState(ViewGroup.java:3127)
// 	at android.view.View.restoreHierarchyState(View.java:14730)
// 	at com.android.internal.policy.PhoneWindow.restoreHierarchyState(PhoneWindow.java:2035)
// 	at android.app.Activity.onRestoreInstanceState(Activity.java:1008)
// 	at android.app.Activity.performRestoreInstanceState(Activity.java:963)
// 	at android.app.Instrumentation.callActivityOnRestoreInstanceState(Instrumentation.java:1163)
// 	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2389)
// 	... 10 more

```




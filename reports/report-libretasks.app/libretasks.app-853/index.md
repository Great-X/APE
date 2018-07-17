title: libretasks.app

# libretasks.app

[Google Play Store](https://play.google.com/store/apps/details?id=libretasks.app)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.RuntimeException: Unable to start activity ComponentInfo{libretasks.app/libretasks.app.view.simple.ActivitySavedRules}: java.lang.IllegalStateException: UIDbHelperStore singleton must be initialized via init() before use!
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
// Caused by: java.lang.IllegalStateException: UIDbHelperStore singleton must be initialized via init() before use!
// 	at libretasks.app.view.simple.UIDbHelperStore.instance(UIDbHelperStore.java:82)
// 	at libretasks.app.view.simple.ActivitySavedRules$RuleListAdapter.<init>(ActivitySavedRules.java:288)
// 	at libretasks.app.view.simple.ActivitySavedRules.onCreate(ActivitySavedRules.java:93)
// 	at android.app.Activity.performCreate(Activity.java:6251)
// 	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1107)
// 	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2369)
// 	... 9 more

```




title: net.nullsum.audinaut

# net.nullsum.audinaut

[Google Play Store](https://play.google.com/store/apps/details?id=net.nullsum.audinaut)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.NullPointerException: Attempt to invoke virtual method 'android.view.View android.view.View.findViewById(int)' on a null object reference
// 	at net.nullsum.audinaut.fragments.SubsonicFragment.setProgressVisible(SubsonicFragment.java:444)
// 	at net.nullsum.audinaut.util.TabBackgroundTask.execute(TabBackgroundTask.java:20)
// 	at net.nullsum.audinaut.fragments.SearchFragment.search(SearchFragment.java:203)
// 	at net.nullsum.audinaut.activity.SubsonicFragmentActivity.onNewIntent(SubsonicFragmentActivity.java:322)
// 	at android.app.Instrumentation.callActivityOnNewIntent(Instrumentation.java:1212)
// 	at android.app.Instrumentation.callActivityOnNewIntent(Instrumentation.java:1224)
// 	at android.app.ActivityThread.deliverNewIntents(ActivityThread.java:2545)
// 	at android.app.ActivityThread.performNewIntents(ActivityThread.java:2557)
// 	at android.app.ActivityThread.handleNewIntent(ActivityThread.java:2566)
// 	at android.app.ActivityThread.-wrap12(ActivityThread.java)
// 	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1416)
// 	at android.os.Handler.dispatchMessage(Handler.java:102)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)

```




title: com.teleca.jamendo

# com.teleca.jamendo

[Google Play Store](https://play.google.com/store/apps/details?id=com.teleca.jamendo)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.RuntimeException: Unable to pause activity {com.teleca.jamendo/com.teleca.jamendo.activity.SearchActivity}: java.lang.NullPointerException: Attempt to invoke virtual method 'java.util.ArrayList com.teleca.jamendo.adapter.AlbumAdapter.getList()' on a null object reference
// 	at android.app.ActivityThread.performPauseActivity(ActivityThread.java:3381)
// 	at android.app.ActivityThread.performPauseActivity(ActivityThread.java:3340)
// 	at android.app.ActivityThread.handleRelaunchActivity(ActivityThread.java:4047)
// 	at android.app.ActivityThread.-wrap15(ActivityThread.java)
// 	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1350)
// 	at android.os.Handler.dispatchMessage(Handler.java:102)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)
// Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'java.util.ArrayList com.teleca.jamendo.adapter.AlbumAdapter.getList()' on a null object reference
// 	at com.teleca.jamendo.activity.SearchActivity.onSaveInstanceState(SearchActivity.java:159)
// 	at android.app.Activity.performSaveInstanceState(Activity.java:1302)
// 	at android.app.Instrumentation.callActivityOnSaveInstanceState(Instrumentation.java:1289)
// 	at android.app.ActivityThread.callCallActivityOnSaveInstanceState(ActivityThread.java:4088)
// 	at android.app.ActivityThread.performPauseActivity(ActivityThread.java:3363)
// 	... 10 more

```




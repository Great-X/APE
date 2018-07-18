title: org.bobstuff.bobball

# org.bobstuff.bobball

[Google Play Store](https://play.google.com/store/apps/details?id=org.bobstuff.bobball)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.RuntimeException: Unable to start activity ComponentInfo{org.bobstuff.bobball/org.bobstuff.bobball.Menus.menuSinglePlayer}: java.lang.NullPointerException: Attempt to invoke interface method 'java.lang.String android.content.SharedPreferences.getString(java.lang.String, java.lang.String)' on a null object reference
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
// Caused by: java.lang.NullPointerException: Attempt to invoke interface method 'java.lang.String android.content.SharedPreferences.getString(java.lang.String, java.lang.String)' on a null object reference
// 	at org.bobstuff.bobball.Preferences.loadValue(Preferences.java:29)
// 	at org.bobstuff.bobball.Statistics.getHighestLevel(Statistics.java:23)
// 	at org.bobstuff.bobball.Menus.menuSinglePlayer.onStart(menuSinglePlayer.java:45)
// 	at android.app.Instrumentation.callActivityOnStart(Instrumentation.java:1237)
// 	at android.app.Activity.performStart(Activity.java:6268)
// 	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2379)
// 	... 9 more

```




title: com.tomer.alwayson

# com.tomer.alwayson

[Google Play Store](https://play.google.com/store/apps/details?id=com.tomer.alwayson)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.RuntimeException: Unable to resume activity {com.tomer.alwayson/com.tomer.alwayson.activities.Intro}: java.lang.NullPointerException: Attempt to write to null array
// 	at android.app.ActivityThread.performResumeActivity(ActivityThread.java:3103)
// 	at android.app.ActivityThread.handleResumeActivity(ActivityThread.java:3134)
// 	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1388)
// 	at android.os.Handler.dispatchMessage(Handler.java:102)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)
// Caused by: java.lang.NullPointerException: Attempt to write to null array
// 	at com.tomer.alwayson.activities.Intro$First.onResume(Unknown Source)
// 	at android.support.v4.app.Fragment.performResume(Fragment.java:2126)
// 	at android.support.v4.app.FragmentManagerImpl.moveToState(FragmentManager.java:1151)
// 	at android.support.v4.app.FragmentManagerImpl.moveToState(FragmentManager.java:1290)
// 	at android.support.v4.app.FragmentManagerImpl.moveToState(FragmentManager.java:1272)
// 	at android.support.v4.app.FragmentManagerImpl.dispatchResume(FragmentManager.java:2159)
// 	at android.support.v4.app.FragmentController.dispatchResume(FragmentController.java:223)
// 	at android.support.v4.app.FragmentActivity.onResumeFragments(FragmentActivity.java:507)
// 	at android.support.v4.app.FragmentActivity.onPostResume(FragmentActivity.java:496)
// 	at android.support.v7.app.AppCompatActivity.onPostResume(AppCompatActivity.java:172)
// 	at android.app.Activity.performResume(Activity.java:6351)
// 	at android.app.ActivityThread.performResumeActivity(ActivityThread.java:3092)
// 	... 8 more

```




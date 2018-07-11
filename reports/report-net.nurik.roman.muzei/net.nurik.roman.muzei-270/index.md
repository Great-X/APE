title: net.nurik.roman.muzei

# net.nurik.roman.muzei

[Google Play Store](https://play.google.com/store/apps/details?id=net.nurik.roman.muzei)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.RuntimeException: Unable to stop activity {kiwi.root.an2linuxclient/kiwi.root.an2linuxclient.activities.CustomNotificationSettingsActivity}: java.lang.IllegalStateException: Can not perform this action after onSaveInstanceState
// 	at android.app.ActivityThread.performStopActivityInner(ActivityThread.java:3500)
// 	at android.app.ActivityThread.handleStopActivity(ActivityThread.java:3550)
// 	at android.app.ActivityThread.-wrap20(ActivityThread.java)
// 	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1373)
// 	at android.os.Handler.dispatchMessage(Handler.java:102)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)
// Caused by: java.lang.IllegalStateException: Can not perform this action after onSaveInstanceState
// 	at android.app.FragmentManagerImpl.checkStateLoss(FragmentManager.java:1411)
// 	at android.app.FragmentManagerImpl.enqueueAction(FragmentManager.java:1429)
// 	at android.app.BackStackRecord.commitInternal(BackStackRecord.java:687)
// 	at android.app.BackStackRecord.commit(BackStackRecord.java:663)
// 	at android.app.DialogFragment.dismissInternal(DialogFragment.java:301)
// 	at android.app.DialogFragment.dismiss(DialogFragment.java:267)
// 	at kiwi.root.an2linuxclient.activities.CustomNotificationSettingsActivity.onStop(Unknown Source)
// 	at android.app.Instrumentation.callActivityOnStop(Instrumentation.java:1278)
// 	at android.app.Activity.performStop(Activity.java:6395)
// 	at android.app.ActivityThread.performStopActivityInner(ActivityThread.java:3497)
// 	... 9 more

```




title: org.pulpdust.lesserpad

# org.pulpdust.lesserpad

[Google Play Store](https://play.google.com/store/apps/details?id=org.pulpdust.lesserpad)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.RuntimeException: Failure delivering result ResultInfo{who=null, request=2, result=0, data=null} to activity {org.pulpdust.lesserpad/org.pulpdust.lesserpad.LesserPadListActivity}: java.lang.NullPointerException: Attempt to get length of null array
// 	at android.app.ActivityThread.deliverResults(ActivityThread.java:3699)
// 	at android.app.ActivityThread.handleSendResult(ActivityThread.java:3742)
// 	at android.app.ActivityThread.-wrap16(ActivityThread.java)
// 	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1393)
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
// 	at org.pulpdust.lesserpad.LesserPadListActivity.onActivityResult(LesserPadListActivity.java:406)
// 	at android.app.Activity.dispatchActivityResult(Activity.java:6456)
// 	at android.app.ActivityThread.deliverResults(ActivityThread.java:3695)
// 	... 9 more

```




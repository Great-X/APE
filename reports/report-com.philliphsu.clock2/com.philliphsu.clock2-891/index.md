title: com.philliphsu.clock2

# com.philliphsu.clock2

[Google Play Store](https://play.google.com/store/apps/details?id=com.philliphsu.clock2)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.RuntimeException: Unable to start service com.philliphsu.clock2.stopwatch.StopwatchNotificationService@93ee65d with Intent { act=com.philliphsu.clock2.timers.action.START_PAUSE cmp=com.philliphsu.clock2/.stopwatch.StopwatchNotificationService }: java.lang.NullPointerException: Attempt to invoke virtual method 'void com.philliphsu.clock2.stopwatch.Lap.pause()' on a null object reference
// 	at android.app.ActivityThread.handleServiceArgs(ActivityThread.java:3027)
// 	at android.app.ActivityThread.-wrap17(ActivityThread.java)
// 	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1442)
// 	at android.os.Handler.dispatchMessage(Handler.java:102)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)
// Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'void com.philliphsu.clock2.stopwatch.Lap.pause()' on a null object reference
// 	at com.philliphsu.clock2.stopwatch.StopwatchNotificationService.handleStartPauseAction(StopwatchNotificationService.java:137)
// 	at com.philliphsu.clock2.chronometer.ChronometerNotificationService.onStartCommand(ChronometerNotificationService.java:207)
// 	at com.philliphsu.clock2.stopwatch.StopwatchNotificationService.onStartCommand(StopwatchNotificationService.java:94)
// 	at android.app.ActivityThread.handleServiceArgs(ActivityThread.java:3010)
// 	... 8 more

```




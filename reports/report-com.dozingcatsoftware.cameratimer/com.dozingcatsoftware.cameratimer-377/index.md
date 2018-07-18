title: com.dozingcatsoftware.cameratimer

# com.dozingcatsoftware.cameratimer

[Google Play Store](https://play.google.com/store/apps/details?id=com.dozingcatsoftware.cameratimer)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.NullPointerException: Attempt to invoke virtual method 'void android.hardware.Camera.autoFocus(android.hardware.Camera$AutoFocusCallback)' on a null object reference
// 	at com.dozingcatsoftware.cameratimer.MainActivity.savePictureNow(MainActivity.java:253)
// 	at com.dozingcatsoftware.cameratimer.MainActivity.savePicture(MainActivity.java:233)
// 	at com.dozingcatsoftware.cameratimer.MainActivity.onShutterButtonClick(MainActivity.java:434)
// 	at com.dozingcatsoftware.util.ShutterButton.performClick(ShutterButton.java:107)
// 	at android.view.View$PerformClick.run(View.java:21153)
// 	at android.os.Handler.handleCallback(Handler.java:739)
// 	at android.os.Handler.dispatchMessage(Handler.java:95)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)

```




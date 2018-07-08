title: us.koller.cameraroll

# us.koller.cameraroll

[Google Play Store](https://play.google.com/store/apps/details?id=us.koller.cameraroll)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.IllegalStateException: Could not execute method for android:onClick
// 	at android.support.v7.app.AppCompatViewInflater$a.onClick(SourceFile:389)
// 	at android.view.View.performClick(View.java:5204)
// 	at android.view.View$PerformClick.run(View.java:21153)
// 	at android.os.Handler.handleCallback(Handler.java:739)
// 	at android.os.Handler.dispatchMessage(Handler.java:95)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)
// Caused by: java.lang.reflect.InvocationTargetException
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at android.support.v7.app.AppCompatViewInflater$a.onClick(SourceFile:384)
// 	... 9 more
// Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'android.net.Uri us.koller.cameraroll.data.a.b.a(android.content.Context)' on a null object reference
// 	at us.koller.cameraroll.ui.ItemActivity.v(SourceFile:503)
// 	at us.koller.cameraroll.ui.ItemActivity.a(SourceFile:791)
// 	at us.koller.cameraroll.ui.ItemActivity.bottomBarOnClick(SourceFile:781)
// 	... 11 more

```




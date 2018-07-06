title: com.fr3ts0n.ecu.gui.androbd

# com.fr3ts0n.ecu.gui.androbd

[Google Play Store](https://play.google.com/store/apps/details?id=com.fr3ts0n.ecu.gui.androbd)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.IllegalStateException: Could not execute method for android:onClick
// 	at android.view.View$DeclaredOnClickListener.onClick(View.java:4458)
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
// 	at android.view.View$DeclaredOnClickListener.onClick(View.java:4453)
// 	... 9 more
// Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'void com.fr3ts0n.androbd.plugin.mgr.PluginHandler.clear()' on a null object reference
// 	at com.fr3ts0n.androbd.plugin.mgr.PluginManager.sendIdentify(PluginManager.java:50)
// 	... 11 more

```




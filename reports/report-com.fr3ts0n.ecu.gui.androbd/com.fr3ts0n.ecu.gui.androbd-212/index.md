title: com.fr3ts0n.ecu.gui.androbd

# com.fr3ts0n.ecu.gui.androbd

[Google Play Store](https://play.google.com/store/apps/details?id=com.fr3ts0n.ecu.gui.androbd)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.RuntimeException: Unable to destroy activity {com.fr3ts0n.ecu.gui.androbd/com.fr3ts0n.ecu.gui.androbd.MainActivity}: java.lang.NullPointerException: Attempt to invoke virtual method 'void com.fr3ts0n.androbd.plugin.mgr.PluginHandler.closeAllPlugins()' on a null object reference
// 	at android.app.ActivityThread.performDestroyActivity(ActivityThread.java:3831)
// 	at android.app.ActivityThread.handleDestroyActivity(ActivityThread.java:3849)
// 	at android.app.ActivityThread.handleRelaunchActivity(ActivityThread.java:4053)
// 	at android.app.ActivityThread.-wrap15(ActivityThread.java)
// 	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1350)
// 	at android.os.Handler.dispatchMessage(Handler.java:102)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)
// Caused by: java.lang.NullPointerException: Attempt to invoke virtual method 'void com.fr3ts0n.androbd.plugin.mgr.PluginHandler.closeAllPlugins()' on a null object reference
// 	at com.fr3ts0n.androbd.plugin.mgr.PluginManager.onDestroy(PluginManager.java:33)
// 	at com.fr3ts0n.ecu.gui.androbd.MainActivity.onDestroy(MainActivity.java:482)
// 	at android.app.Activity.performDestroy(Activity.java:6422)
// 	at android.app.Instrumentation.callActivityOnDestroy(Instrumentation.java:1142)
// 	at android.app.ActivityThread.performDestroyActivity(ActivityThread.java:3818)
// 	... 10 more

```




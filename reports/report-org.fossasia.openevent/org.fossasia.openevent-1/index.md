title: org.fossasia.openevent

# org.fossasia.openevent

[Google Play Store](https://play.google.com/store/apps/details?id=org.fossasia.openevent)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.NullPointerException: Attempt to invoke virtual method 'float org.fossasia.openevent.data.Event.getLatitude()' on a null object reference
// 	at org.fossasia.openevent.fragments.OSMapFragment.populateMap(OSMapFragment.java:113)
// 	at org.fossasia.openevent.fragments.OSMapFragment.onViewCreated(OSMapFragment.java:184)
// 	at android.support.v4.app.FragmentManagerImpl.moveToState(FragmentManager.java:1315)
// 	at android.support.v4.app.FragmentManagerImpl.moveFragmentsToInvisible(FragmentManager.java:2323)
// 	at android.support.v4.app.FragmentManagerImpl.executeOpsTogether(FragmentManager.java:2136)
// 	at android.support.v4.app.FragmentManagerImpl.optimizeAndExecuteOps(FragmentManager.java:2092)
// 	at android.support.v4.app.FragmentManagerImpl.execPendingActions(FragmentManager.java:1998)
// 	at android.support.v4.app.FragmentManagerImpl$1.run(FragmentManager.java:709)
// 	at android.os.Handler.handleCallback(Handler.java:739)
// 	at android.os.Handler.dispatchMessage(Handler.java:95)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)

```




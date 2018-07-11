title: com.nhellfire.kerneladiutor

# com.nhellfire.kerneladiutor

[Google Play Store](https://play.google.com/store/apps/details?id=com.nhellfire.kerneladiutor)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String android.content.Context.getPackageName()' on a null object reference
// 	at android.preference.PreferenceManager.getDefaultSharedPreferencesName(PreferenceManager.java:375)
// 	at android.preference.PreferenceManager.getDefaultSharedPreferences(PreferenceManager.java:370)
// 	at com.grarak.kerneladiutor.utils.Prefs.getBoolean(Prefs.java:43)
// 	at com.grarak.kerneladiutor.fragments.RecyclerViewFragment.hideBanner(RecyclerViewFragment.java:749)
// 	at com.grarak.kerneladiutor.fragments.RecyclerViewFragment.onViewFinished(RecyclerViewFragment.java:339)
// 	at com.grarak.kerneladiutor.fragments.BaseFragment$1.onGlobalLayout(BaseFragment.java:56)
// 	at android.view.ViewTreeObserver.dispatchOnGlobalLayout(ViewTreeObserver.java:912)
// 	at android.view.ViewRootImpl.performTraversals(ViewRootImpl.java:1969)
// 	at android.view.ViewRootImpl.doTraversal(ViewRootImpl.java:1107)
// 	at android.view.ViewRootImpl$TraversalRunnable.run(ViewRootImpl.java:6013)
// 	at android.view.Choreographer$CallbackRecord.run(Choreographer.java:858)
// 	at android.view.Choreographer.doCallbacks(Choreographer.java:670)
// 	at android.view.Choreographer.doFrame(Choreographer.java:606)
// 	at android.view.Choreographer$FrameDisplayEventReceiver.run(Choreographer.java:844)
// 	at android.os.Handler.handleCallback(Handler.java:739)
// 	at android.os.Handler.dispatchMessage(Handler.java:95)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)

```




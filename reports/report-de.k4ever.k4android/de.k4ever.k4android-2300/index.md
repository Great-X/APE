title: de.k4ever.k4android

# de.k4ever.k4android

[Google Play Store](https://play.google.com/store/apps/details?id=de.k4ever.k4android)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.IllegalStateException: Content view not yet created
// 	at android.support.a.a.be.b(Unknown Source)
// 	at android.support.a.a.be.a(Unknown Source)
// 	at de.k4ever.k4android.fragments.ac.c(Unknown Source)
// 	at android.support.a.f.q.onTouchEvent(Unknown Source)
// 	at android.view.View.dispatchTouchEvent(View.java:9300)
// 	at android.view.ViewGroup.dispatchTransformedTouchEvent(ViewGroup.java:2521)
// 	at android.view.ViewGroup.dispatchTouchEvent(ViewGroup.java:2240)
// 	at android.view.ViewGroup.dispatchTransformedTouchEvent(ViewGroup.java:2523)
// 	at android.view.ViewGroup.dispatchTouchEvent(ViewGroup.java:2254)
// 	at android.view.ViewGroup.dispatchTransformedTouchEvent(ViewGroup.java:2523)
// 	at android.view.ViewGroup.dispatchTouchEvent(ViewGroup.java:2254)
// 	at android.view.ViewGroup.dispatchTransformedTouchEvent(ViewGroup.java:2523)
// 	at android.view.ViewGroup.dispatchTouchEvent(ViewGroup.java:2254)
// 	at android.view.ViewGroup.dispatchTransformedTouchEvent(ViewGroup.java:2523)
// 	at android.view.ViewGroup.cancelAndClearTouchTargets(ViewGroup.java:2373)
// 	at android.view.ViewGroup.dispatchDetachedFromWindow(ViewGroup.java:3045)
// 	at android.view.ViewRootImpl.dispatchDetachedFromWindow(ViewRootImpl.java:3068)
// 	at android.view.ViewRootImpl.doDie(ViewRootImpl.java:5606)
// 	at android.view.ViewRootImpl.die(ViewRootImpl.java:5583)
// 	at android.view.WindowManagerGlobal.removeViewLocked(WindowManagerGlobal.java:397)
// 	at android.view.WindowManagerGlobal.removeView(WindowManagerGlobal.java:352)
// 	at android.view.WindowManagerImpl.removeViewImmediate(WindowManagerImpl.java:116)
// 	at android.app.ActivityThread.handleDestroyActivity(ActivityThread.java:3867)
// 	at android.app.ActivityThread.-wrap5(ActivityThread.java)
// 	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1398)
// 	at android.os.Handler.dispatchMessage(Handler.java:102)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)

```




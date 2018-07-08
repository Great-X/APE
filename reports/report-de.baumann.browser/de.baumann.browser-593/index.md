title: de.baumann.browser

# de.baumann.browser

[Google Play Store](https://play.google.com/store/apps/details?id=de.baumann.browser)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.RuntimeException: Unable to start activity ComponentInfo{de.baumann.browser/de.baumann.browser.Activity.BrowserActivity}: java.lang.IllegalStateException: The specified child already has a parent. You must call removeView() on the child's parent first.
// 	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2416)
// 	at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:2476)
// 	at android.app.ActivityThread.-wrap11(ActivityThread.java)
// 	at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1344)
// 	at android.os.Handler.dispatchMessage(Handler.java:102)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)
// Caused by: java.lang.IllegalStateException: The specified child already has a parent. You must call removeView() on the child's parent first.
// 	at android.view.ViewGroup.addViewInner(ViewGroup.java:4309)
// 	at android.view.ViewGroup.addView(ViewGroup.java:4145)
// 	at android.view.ViewGroup.addView(ViewGroup.java:4103)
// 	at de.baumann.browser.Activity.BrowserActivity.pinAlbums(BrowserActivity.java:2451)
// 	at de.baumann.browser.Activity.BrowserActivity.dispatchIntent(BrowserActivity.java:1385)
// 	at de.baumann.browser.Activity.BrowserActivity.onCreate(BrowserActivity.java:415)
// 	at android.app.Activity.performCreate(Activity.java:6251)
// 	at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1107)
// 	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2369)
// 	... 9 more

```




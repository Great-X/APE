title: com.wangdaye.mysplash

# com.wangdaye.mysplash

[Google Play Store](https://play.google.com/store/apps/details?id=com.wangdaye.mysplash)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.RuntimeException: Unable to start activity ComponentInfo{com.wangdaye.mysplash/com.wangdaye.mysplash.common.ui.activity.IntroduceActivity}: java.lang.NegativeArraySizeException: -1
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
// Caused by: java.lang.NegativeArraySizeException: -1
// 	at com.pixelcan.inkpageindicator.InkPageIndicator.resetState(InkPageIndicator.java:259)
// 	at com.pixelcan.inkpageindicator.InkPageIndicator.setPageCount(InkPageIndicator.java:222)
// 	at com.pixelcan.inkpageindicator.InkPageIndicator.setViewPager(InkPageIndicator.java:173)
// 	at com.wangdaye.mysplash.common.ui.activity.IntroduceActivity.g(IntroduceActivity.java:221)
// 	at com.wangdaye.mysplash.common.ui.activity.IntroduceActivity.onStart(IntroduceActivity.java:127)
// 	at android.app.Instrumentation.callActivityOnStart(Instrumentation.java:1237)
// 	at android.app.Activity.performStart(Activity.java:6268)
// 	at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2379)
// 	... 9 more

```




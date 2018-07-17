title: com.crazyhitty.chdev.ks.munch

# com.crazyhitty.chdev.ks.munch

[Google Play Store](https://play.google.com/store/apps/details?id=com.crazyhitty.chdev.ks.munch)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.NullPointerException: Attempt to invoke virtual method 'android.content.res.Resources android.content.Context.getResources()' on a null object reference
// 	at android.widget.Toast.<init>(Toast.java:102)
// 	at android.widget.Toast.makeText(Toast.java:259)
// 	at com.crazyhitty.chdev.ks.munch.ui.activities.SettingsActivity$SettingsFragment.onFeedsLoadingFailure(SettingsActivity.java:316)
// 	at com.crazyhitty.chdev.ks.munch.curatedfeeds.CuratedFeedsPresenter.onFailure(CuratedFeedsPresenter.java:31)
// 	at com.crazyhitty.chdev.ks.munch.curatedfeeds.CuratedFeedsInteractor$1.run(CuratedFeedsInteractor.java:61)
// 	at android.os.Handler.handleCallback(Handler.java:739)
// 	at android.os.Handler.dispatchMessage(Handler.java:95)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)

```




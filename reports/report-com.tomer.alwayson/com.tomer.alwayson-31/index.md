title: com.tomer.alwayson

# com.tomer.alwayson

[Google Play Store](https://play.google.com/store/apps/details?id=com.tomer.alwayson)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.NullPointerException: Attempt to invoke virtual method 'int android.content.Context.getColor(int)' on a null object reference
// 	at android.support.v4.content.ContextCompatApi23.getColor(ContextCompatApi23.java:31)
// 	at android.support.v4.content.ContextCompat.getColor(ContextCompat.java:404)
// 	at com.tomer.alwayson.activities.Intro$Third.onCreateView(Unknown Source)
// 	at android.support.v4.app.Fragment.performCreateView(Fragment.java:2080)
// 	at android.support.v4.app.FragmentManagerImpl.moveToState(FragmentManager.java:1108)
// 	at android.support.v4.app.FragmentManagerImpl.moveToState(FragmentManager.java:1290)
// 	at android.support.v4.app.BackStackRecord.run(BackStackRecord.java:801)
// 	at android.support.v4.app.FragmentManagerImpl.execSingleAction(FragmentManager.java:1638)
// 	at android.support.v4.app.BackStackRecord.commitNowAllowingStateLoss(BackStackRecord.java:679)
// 	at android.support.v4.app.FragmentPagerAdapter.finishUpdate(FragmentPagerAdapter.java:143)
// 	at android.support.v4.view.ViewPager.populate(ViewPager.java:1240)
// 	at android.support.v4.view.ViewPager.setCurrentItemInternal(ViewPager.java:670)
// 	at android.support.v4.view.ViewPager.setCurrentItemInternal(ViewPager.java:632)
// 	at android.support.v4.view.ViewPager.setCurrentItem(ViewPager.java:613)
// 	at com.github.paolorotolo.appintro.AppIntroViewPager.setCurrentItem(AppIntroViewPager.java:61)
// 	at com.github.paolorotolo.appintro.AppIntroBase$NextButtonOnClickListener.onClick(AppIntroBase.java:776)
// 	at android.view.View.performClick(View.java:5204)
// 	at android.view.View$PerformClick.run(View.java:21153)
// 	at android.os.Handler.handleCallback(Handler.java:739)
// 	at android.os.Handler.dispatchMessage(Handler.java:95)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)

```




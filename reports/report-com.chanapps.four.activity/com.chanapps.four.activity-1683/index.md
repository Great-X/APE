title: com.chanapps.four.activity

# com.chanapps.four.activity

[Google Play Store](https://play.google.com/store/apps/details?id=com.chanapps.four.activity)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.ArrayIndexOutOfBoundsException: length=8; index=8
// 	at com.chanapps.four.activity.AbstractDrawerActivity$2$1.isEnabled(AbstractDrawerActivity.java:169)
// 	at android.widget.AbsListView.setItemViewLayoutParams(AbsListView.java:2398)
// 	at android.widget.AbsListView.obtainView(AbsListView.java:2367)
// 	at android.widget.ListView.makeAndAddView(ListView.java:1876)
// 	at android.widget.ListView.fillDown(ListView.java:702)
// 	at android.widget.ListView.fillFromTop(ListView.java:763)
// 	at android.widget.ListView.layoutChildren(ListView.java:1671)
// 	at android.widget.AbsListView.onLayout(AbsListView.java:2148)
// 	at android.view.View.layout(View.java:16636)
// 	at android.view.ViewGroup.layout(ViewGroup.java:5437)
// 	at android.support.v4.widget.DrawerLayout.onLayout(DrawerLayout.java:714)
// 	at android.view.View.layout(View.java:16636)
// 	at android.view.ViewGroup.layout(ViewGroup.java:5437)
// 	at android.widget.FrameLayout.layoutChildren(FrameLayout.java:336)
// 	at android.widget.FrameLayout.onLayout(FrameLayout.java:273)
// 	at android.view.View.layout(View.java:16636)
// 	at android.view.ViewGroup.layout(ViewGroup.java:5437)
// 	at com.android.internal.widget.ActionBarOverlayLayout.onLayout(ActionBarOverlayLayout.java:493)
// 	at android.view.View.layout(View.java:16636)
// 	at android.view.ViewGroup.layout(ViewGroup.java:5437)
// 	at android.widget.FrameLayout.layoutChildren(FrameLayout.java:336)
// 	at android.widget.FrameLayout.onLayout(FrameLayout.java:273)
// 	at android.view.View.layout(View.java:16636)
// 	at android.view.ViewGroup.layout(ViewGroup.java:5437)
// 	at android.widget.FrameLayout.layoutChildren(FrameLayout.java:336)
// 	at android.widget.FrameLayout.onLayout(FrameLayout.java:273)
// 	at com.android.internal.policy.PhoneWindow$DecorView.onLayout(PhoneWindow.java:2678)
// 	at android.view.View.layout(View.java:16636)
// 	at android.view.ViewGroup.layout(ViewGroup.java:5437)
// 	at android.view.ViewRootImpl.performLayout(ViewRootImpl.java:2171)
// 	at android.view.ViewRootImpl.performTraversals(ViewRootImpl.java:1931)
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




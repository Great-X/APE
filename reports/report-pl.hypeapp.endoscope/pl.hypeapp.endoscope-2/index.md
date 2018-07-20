title: pl.hypeapp.endoscope

# pl.hypeapp.endoscope

[Google Play Store](https://play.google.com/store/apps/details?id=pl.hypeapp.endoscope)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.IllegalStateException: subscription handling doesn't work when the presenter has reached the DESTROYED state
// 	at net.grandcentrix.thirtyinch.rx.RxTiPresenterSubscriptionHandler.manageSubscription(RxTiPresenterSubscriptionHandler.java:67)
// 	at pl.hypeapp.endoscope.presenter.SplashScreenPresenter.delayRunActivity(SplashScreenPresenter.java:33)
// 	at pl.hypeapp.endoscope.ui.activity.SplashScreenActivity$1.onAnimationEnd(SplashScreenActivity.java:55)
// 	at xyz.hanks.library.SmallBang$3.onAnimationEnd(SmallBang.java:188)
// 	at android.animation.ValueAnimator.endAnimation(ValueAnimator.java:1239)
// 	at android.animation.ValueAnimator$AnimationHandler.doAnimationFrame(ValueAnimator.java:766)
// 	at android.animation.ValueAnimator$AnimationHandler$1.run(ValueAnimator.java:801)
// 	at android.view.Choreographer$CallbackRecord.run(Choreographer.java:858)
// 	at android.view.Choreographer.doCallbacks(Choreographer.java:670)
// 	at android.view.Choreographer.doFrame(Choreographer.java:603)
// 	at android.view.Choreographer$FrameDisplayEventReceiver.run(Choreographer.java:844)
// 	at android.os.Handler.handleCallback(Handler.java:739)
// 	at android.os.Handler.dispatchMessage(Handler.java:95)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)

```




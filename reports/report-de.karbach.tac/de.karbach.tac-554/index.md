title: de.karbach.tac

# de.karbach.tac

[Google Play Store](https://play.google.com/store/apps/details?id=de.karbach.tac)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.IllegalStateException: Fragment LocalBoard{cbdb982} not attached to Activity
// 	at android.support.v4.app.Fragment.getResources(Fragment.java:639)
// 	at de.karbach.tac.ui.fragments.LocalBoard.isOrientationLandscape(LocalBoard.java:110)
// 	at de.karbach.tac.ui.BoardControl.startActionOnPoint(BoardControl.java:336)
// 	at de.karbach.tac.ui.BoardControl.onSingleTapConfirmed(BoardControl.java:493)
// 	at android.view.GestureDetector$GestureHandler.handleMessage(GestureDetector.java:300)
// 	at android.os.Handler.dispatchMessage(Handler.java:102)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)

```




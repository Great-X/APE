title: com.commonsware.android.arXiv

# com.commonsware.android.arXiv

[Google Play Store](https://play.google.com/store/apps/details?id=com.commonsware.android.arXiv)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.IllegalArgumentException: View=com.android.internal.policy.PhoneWindow$DecorView{82f1440 V.E...... R......D 0,0-1154,288} not attached to window manager
// 	at android.view.WindowManagerGlobal.findViewLocked(WindowManagerGlobal.java:424)
// 	at android.view.WindowManagerGlobal.removeView(WindowManagerGlobal.java:350)
// 	at android.view.WindowManagerImpl.removeViewImmediate(WindowManagerImpl.java:116)
// 	at android.app.Dialog.dismissDialog(Dialog.java:362)
// 	at android.app.Dialog$1.run(Dialog.java:135)
// 	at android.os.Handler.handleCallback(Handler.java:739)
// 	at android.os.Handler.dispatchMessage(Handler.java:95)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)

```



